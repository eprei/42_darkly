# Reflected XSS

## Exploit

On the home, one of the nsa image is clickable.\
A `GET /?page=media&src=nsa HTTP/1.1` request is send and a new page is rendered with the image on it.\
The image is rendered inside a [object HTML tag](https://www.w3schools.com/tags/tag_object.asp) which shouldn't be used anymore.\
We change the request and add what we want to be send back to us. \
for example: `src=data:text/html;<script>alert("42");</script>`\
It works but it is html encoded so it doesn't trigger the script.\
`<object data="data:text/html;&lt;script&gt;alert(&quot;42&quot;);&lt;/script&gt;"></object>`\
The next step is to base64 encode the payload:
`/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiNDIiKTs8L3NjcmlwdD5g`\
The script is run and we get the flag.

## Patch

- Sanitize user inputs by removing or escaping any HTML tags or characters that can be interpreted as code.
- Use libraries like DOMPurify (for JavaScript) to sanitize HTML content.
- Encode data before rendering it on the page to prevent browsers from interpreting user inputs as HTML or JavaScript. In web frameworks, use built-in functions for safe output rendering, such as htmlspecialchars() in PHP or escapeHTML() in JavaScript.
- Many web frameworks (like Django, Ruby on Rails, and React) have built-in mechanisms to prevent HTML injection by default. For example, React automatically escapes any dynamic content to prevent script injection.

## Resources

[Portswinger Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected)

[OWASP Testing for Reflected XSS](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting.html)

[OWASP Prevention of XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
