# XSS LAB 12 - Reflected DOM XSS
## Manual Solution

### 1. What is eval()?
- The eval function executes a string as JavaScript code.
```js
eval("console.log('Hello world')");
```
- This code outputs: Hello world

### 2. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 3. Open the Network tab.

### 4. Perform a test search.

### 5. search-results 
- In the Network tab, there is a GET request to search-results.
- The search-results response contains a JSON object, for example:
```json
{
    results: [],
    searchTerm: "abc"
}
```

### 6. searchResults.js
- In the Network tab, there is a GET request to searchResults.js.
- You can see the searchResults.js code in the response:
```js
if (this.readyState == 4 && this.status == 200) {
    eval('var searchResultsObj = ' + this.responseText);
    displaySearchResults(searchResultsObj);
}
```
- The eval function in this case is used to parse and execute the JSON response as JavaScript code.

### 7. Perform a search
- Perform a search using the following query: `abc\"};alert(1);//`
- The escape sequence \" allows the double quote (") to be included within a JSON string.


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_12.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 