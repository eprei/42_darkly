## Exploit

On the login page: "/?page=feedback", when the user fill up the feedback form,\
there is a function validate_form() that is called.\
But it only checks that fields are not empty and don't do any sanitization even thought the message is directly added to the frontend.
We can do a HTML injection:\
`name: toto, message: <scr<script>ipt>alert('XSS')</scr<script>ipt>`\
This will trigger the flag.

## Patch

- Sanitize user inputs by removing or escaping any HTML tags or characters that can be interpreted as code.
- Use libraries like DOMPurify (for JavaScript) to sanitize HTML content.
- Encode data before rendering it on the page to prevent browsers from interpreting user inputs as HTML or JavaScript. In web frameworks, use built-in functions for safe output rendering, such as htmlspecialchars() in PHP or escapeHTML() in JavaScript.
- Many web frameworks (like Django, Ruby on Rails, and React) have built-in mechanisms to prevent HTML injection by default. For example, React automatically escapes any dynamic content to prevent script injection.

## Resources

[Payloads list](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/Intruders/IntrudersXSS.txt)

[PortSwinger](https://portswigger.net/web-security/cross-site-scripting)

[OWASP](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)
