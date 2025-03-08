# XSS LAB 16 - Reflected XSS with some SVG markup allowed

## Manual Solution

### 1. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 2. Perform a search.
- Try the following payload: `<script>alert(1)</script>`.
- Notice that the tag is being filtered.
- In this lab, most XSS payloads are filtered by the WAF.

### 3. Open Burp intruder.
- Open Burp Suite and capture the search request.
- Set the payload position as follows: `search=<§§>`.
- Copy XSS tags from the PortSwigger XSS Cheat Sheet and paste them into the payload list.
- Start the attack
- Any tag that returns a 200 status code is not being filtered by the WAF.

### 4. Find a Bypass
- Set the payload position as follows: `/?search=<svg><animatetransform+§§=alert(1)>`.
- Copy XSS event attributes from the PortSwigger XSS Cheat Sheet and paste them into the payload list.
- Start the attack.
- Any event that returns a 200 status code is not being filtered by the WAF.

### 5. Execute the XSS Attack
- Perform a search using the following query `<svg><animatetransform onbegin=alert(1)>`.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_16.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
``` 