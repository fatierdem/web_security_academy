# SQL Injection Lab 02 - SQL injection vulnerability allowing login bypass

## Manual Solution

### 1. Open the lab in Web Security Academy.
### 2. Open the login page.
### 3. Log in with the username `administrator` and any password you want.
- When we click the login button, the following SQL query is executed in the background: 
```sql 
SELECT * FROM users WHERE username = 'administrator' and password = 'your_password'
```

### 4. Log in with the username `administrator'--` and any password you want.
- When we click the login button, the following SQL query is executed in the background: 
```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = 'your_password'
```
- As you can see, the password verification in the SQL query is bypassed due to the comment sequence.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_02.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

