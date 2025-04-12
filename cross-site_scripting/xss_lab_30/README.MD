# XSS LAB 30 - Reflected XSS protected by CSP, with CSP bypass

## Manual Solution

- Open the Web Security Academy lab environment in your browser.
- Open the Network tab in Developer Tools (F12 → Network).
- Perform a search with the following payload: `<script>alert()</script>`
- Observe that the payload is reflected in the response but CSP prevents execution.
- Check the Content-Security-Policy (CSP) header in the response:
``content-security-policy: default-src 'self'; object-src 'none';script-src 'self'; style-src 'self'; report-uri /csp-report?token=``
- Notice that we can control the token parameter in the report-uri directive.
- Modify the URL to inject a new CSP rule that allows inline scripts:
`?search=<script>alert(1)</script>&token=;script-src-elem 'unsafe-inline'`
- Now, the CSP policy is bypassed, allowing the execution of the inline script.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_30.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```