# XSS LAB 27 - Reflected XSS with event handlers and href attributes blocked

## Manual Solution


### 1. Before you start:
- Some useful articles:
    - [MDN Web Docs: Element.animate](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate)
    - [W3Schools: SVG Animation](https://www.w3schools.com/graphics/svg_animation.asp)
    - [MDN Web Docs: SVG `<text>` Element](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
    - [W3Schools: Introduction to SVG](https://www.w3schools.com/graphics/svg_intro.asp)
    
### 2. Access the Lab.
- Open the Web Security Academy lab environment in your browser.

### 3. Determining unblocked tags
- Open Burp Suite.
- Perform an regular search on the target website and capture the search request in Burp Suite. Then send the request to `Intruder`.
- Modify the search parameter like this `/?search=<§§`
- Visit the following URL and copy the list of tags: [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet).
- Add the following payload to the payload list in Burp Suite:
![payload](cross-site scripting/images/Payload.png)
- Paste the tags you copied into the payload list. Then click `Start attack`.
- The tags that return a 200 OK status code are considered unblocked.
![tags](cross-site scripting/images/Tags.png)

### 4. Solving the lab.
- In this lab We can use the `svg` tag. Perform a search with the following payload `<svg> </svg>` and notice that the tag is unblocked.
- Next, try creating an `<a>` tag inside the `<svg>` tag. Use the following payload: `<svg><a>Click Me</a></svg>`. If you inspect the page, you will see the following HTML in the DOM 
```html 
<svg> <a>click me </a> </svg>
``` 
- However the Click Me text is not visible on the page. This is because in SVG text content must be wrapped inside a `<text>` element.
- Try the following payload: `<svg> <a> <text x=30 y=30 > Click Me </text> </a> </svg>` The HTML DOM becomes: 
```html 
<svg> 
    <a> 
        <text x="50" y="50"> click me </text> 
    </a> 
</svg>
```
- Now we can use the `<animate>` tag to modify the href attribute of the `<a>` tag.
- Perform a search with the following payload: 
```html
<svg> 
    <a> 
        <animate attributeName=href values=javascript:alert() /> 
        <text x=30 y=30 > Click Me </text> 
    </a>
</svg>
```
- We place the `<animate>` tag inside the `<a>` tag because the `<animate>` element targets its parent tag.
If we don't place it inside the `<a>` tag we would need to use the `xlink:href` attribute but in this lab it is not allowed.

## Automated Solution

### 1. Download the script
### 2. Run the script with the following command:
```sh
python xss_lab_27.py -u <target_url> -p (if you want to use proxy 127.0.0.1:8080)
```