# XSS LAB 28 - Reflected XSS in a JavaScript URL with some characters blocked

## Manual Solution

- Some useful articles:
    - [JavaScript `throw` Statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
    - [Window `onerror` Event](https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event)
    - [JavaScript `toString` Method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)

- Payload:

```perl
https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27
```
- Decoded version:

```bash
https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+''},{x:'
```
# Explanation:
- `&'}` is used to escape the `postId` parameter and break out of the existing JavaScript context.
- `throw/**/onerror=alert,1337`
    - The `throw` statement generates an error.
    - If `throw` receives two parameters it executes both but only throws the last one.
    - Here the last parameter (`1337`) is sent to `onerror`.

- `onerror = alert`
    - The `onerror` function is overridden with alert.
    - So whenever an error occurs instead of executing onerror the alert function is executed.
    - This works because throw passes its last parameter to `onerror`.
    - Example: ``throw 1337; ``triggers ``onerror`` which is now ``alert`` so ``alert(1337)`` is executed.

- ``/**/``
    - This is a comment block ``(/**/)`` used to create a space, since spaces cannot be directly included in the URL.

- ``x=x=>``
    - Defines an arrow function named ``x``.

- ``toString = x``
    - The ``toString`` method converts an object to a string.
    - Here ``toString`` is replaced with ``x``.

- ``window+''``
    - This triggers the ``toString`` function because adding an empty string (+'') forces JavaScript to call the ``toString`` method on window.

- ``{x:'``
    - This ensures the JavaScript syntax remains valid and prevents errors.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_28.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```