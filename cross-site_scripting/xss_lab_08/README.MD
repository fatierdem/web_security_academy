# XSS LAB 08 - Stored XSS into anchor href attribute with double quotes HTML-encoded

## Manual Solution

### 1. Access the Lab
- Open the Web Security Academy lab environment in your browser.

### 2. XSS Test
- Click any post in the blog
- Create a new comment for xss test
- Example input:
    - `Comment: test` 
    - `Name: test`
    - `Email: test@test.com`
    - `Comment: javascript:alert(1)`
- Submit the comment and return to the post page.
- Your name should now be clickable. Click on it to trigger the alert.


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_08.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```





