# XSS LAB 26 - Reflected XSS with AngularJS sandbox escape and CSP

## Manual Solution


### 1. Before you start:
- Some useful articles:
    - [Content Security Policy and XSS](https://portswigger.net/web-security/cross-site-scripting/content-security-policy)
    - [Event.composedPath() - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Event/composedPath)
    - [AngularJS ng-focus Directive - GeeksforGeeks](https://www.geeksforgeeks.org/angularjs-ng-focus-directive/)
    - [Window API - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window)

### 2. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 3. Perform a search.
- Open the Network tab and perform an ordinary search.
- Notice the CSP header. The CSP restricts scripts.
![Search Request Screenshot](./images/CSP.png)

### 4. Exploit Overview
- We can't execute script on the website but the website uses AngularJS. We can execute scripts using `ng-focus`. `ng-focus` triggers a script when focused on an HTML element
- We will create an input element.
- `<input id=x ng-focus=`(If there were no CSP everything we write here would be triggered when the user interacts the input field.) The CSP blocks JavaScript code.

### 5. Bypassing CSP with AngularJS
- To bypass the CSP we can use `$event.composedPath()`. `$event.composedPath()` returns an array that contains the DOM elements in the event's propagation path, with the last element being the window object.
- We will use `|orderBy` to execute script for each tag. The payload becomes:
    - `<input id=x ng-focus=$event.composedPath()|orderBy:'alert(1)'>` 
    - But this payload doesn't work because the CSP block the `'alert(1)'` part of the payload.
- `<input id=x ng-focus=$event.composedPath()|orderBy:'(z=alert)(1)'>`  
    - We will store the alert in z which manipulates the CSP.
- If you perform a search with `<input id=x ng-focus=$event.composedPath()|orderBy:'(z=alert)(1)'>` an input field will appear on the website. If you interacts with it the alert pop-up appear.

### 6. Executing the Exploit
- Paste the search path in the URL `<input id=x ng-focus=$event.composedPath()|orderBy:'(z=alert)(document.cookie)'>#x`
- Copy the URL. Go to the exploit server and insert the body field with the following payload:
```js
<script>
    location='[YOUR_COPY]';
</script>
```
- Deliver to exploit.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_26.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```