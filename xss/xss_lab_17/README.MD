# XSS LAB 17 - Reflected XSS in canonical link tag

## Manual Solution

### 1. What is accesskey?
- The accesskey attribute is used to assign a keyboard shortcut to an HTML element.
- When a key is assigned to an HTML element the user can focus on or activate the element using specific key combinations.
- If we add the onclick="alert(1)" attribute, alert(1) will be triggered automatically when the assigned key is pressed.

### 2. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 3. Analyze the Vulnerability
- Inspect the page source
- Locate the canonical link tag in the HTML header:
```html
<link rel="canonical" href='https://[YOUR_LAB_ID].web-security-academy.net/'/>
```
- Notice that the `href` attribute uses single quotes and its value includes the current URL
- The application reflects URL parameters in this tag without proper sanitization

### 4. Understanding the Protection
- Direct script injection is blocked
- Example: `?<script>alert(1)</script>` gets filtered
- Special characters like `<` and `>` are encoded by the WAF
- However, we can still inject attributes since quotes are allowed

### 5. Exploiting the Vulnerability
- The vulnerability can be exploited using HTML attributes
- We can use the `accesskey` attribute combined with `onclick`
- Payload: `?'accesskey='x'onclick='alert(1)`
- This creates the following HTML:
```html
<link rel="canonical" href='https://[YOUR_LAB_ID].web-security-academy.net/?'accesskey='x'onclick='alert(1)'/>
```
- When user presses 
    On Windows: ALT+SHIFT+X
    On MacOS: CTRL+ALT+X
    On Linux: Alt+X
the XSS triggers

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_17.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```