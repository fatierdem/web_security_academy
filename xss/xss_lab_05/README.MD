# XSS LAB 05 - DOM XSS in jQuery anchor href attribute sink using location.search source

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Understanding the lab
- Click the Submit Feedback button.
- Notice how the URL turns into this `web-security-academy.net/feedback?returnPath=/`
- Right-click the back button and select inspect.
- Notice the jQuery function. This function gets the URL return path=`[YOUR_QUERY]` part in the URL and changes the href of the back link.
```javascript
$(function() {
    $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
});
```

### 3. Change the URL
- Change the URL to `feedback?returnPath=abc`
- Right-click the back button and select inspect.
- Notice the back button turns into this: `<a id="backLink" href="abc">Back</a>`

### 4. Make a new search
- Change the URL to `feedback?returnPath=javascript:alert(document.cookie)` and click the back button.
- You'll see the cookie and a congratulations message.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_05.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```





