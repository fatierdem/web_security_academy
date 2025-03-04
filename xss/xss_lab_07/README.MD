# XSS LAB 07 - Reflected XSS into attribute with angle brackets HTML-encoded

## Manual Solution

### 1. Access the Lab
- Open the Web Security Academy lab environment in your browser.

### 2. Perform a Search
- For example, enter: asd
- Notice that our search query appear on the page `0 search results for 'asd'`

### 3. XSS Test
- Perform a new search using the XSS payload: `<script>alert(1)</script>`
- After clicking the search button, the alert does not appear.

### 4. Bypassing Character Restrictions in XSS
- This lab encodes certain special characters like / and \, preventing us from using traditional XSS payloads that rely on closing tags (</script>).
- Since angle brackets (< >) are HTML-encoded.
- Instead, we need to inject our payload into an attribute, such as an event handler (e.g., onmouseover).

### 5. Execution
- Enter the above payload into the search input field. `"onmouseover="alert(1)`


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_07.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```





