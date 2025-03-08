# XSS LAB 19 - Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Analyze the Vulnerability
- Perform a search with the following query: ` ' " / \ < > `
- Open the inspect and locate the script.
```js
<script>
    var searchTerms = ' \' &quot; / \ &lt; &gt; ';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>
```
- We can see that the single quote (') is escaped but the backslash and slash (/) are not escaped.

### 3. Inject the XSS payload
- Perform a search with the following query: `\'-alert(1)//`
- An alert pop-up appears.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_19.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```