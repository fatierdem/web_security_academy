# SQL Injection Lab 14 - Blind SQL injection with time delays

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Initial Setup
- Open Burp Suite and intercept a GET request to the website.
- Send the captured request to the Repeater for testing.

### 3. Add the time delay payload to the trackingId parameter
- ' || (SELECT pg_sleep(10))-- 
- pg_sleep(10) is a function that sleeps for 10 seconds.
- || is the string concatenation operator in PostgreSQL that allows chaining multiple SQL expressions

### 4. Send the request
- Send the request to the Repeater.
- You will see the congratulations message after 10 seconds.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_14.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

