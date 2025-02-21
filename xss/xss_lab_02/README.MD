# XSS LAB 02 - Stored XSS into HTML context with nothing encoded

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Open a post in the blog

### 3. Make a comment
- Comment: `<script>alert('XSS')</script>`
- Name: `Anything`
- Email: `Anything@anything.com`
- Website: `https://www.anything.com`

### 4. Submit the comment

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python xss_lab_02.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)





