## Exploit

On the login page: "/?page=feedback", when the user fill up the feedback form,<br>
there is a function validate_form() that is called.<br>
But it only checks that fields are not empty and don't do any sanitazation even thought the message is directly added to the frontend.
We can do a HTML injection:<br>
`name: toto, message: <alert>This will trigger an alert</alert>`<br>
This will trigger the flag.


## Patch
- Sanitize user inputs by removing or escaping any HTML tags or characters that can be interpreted as code.
- Use libraries like DOMPurify (for JavaScript) to sanitize HTML content.
- Encode data before rendering it on the page to prevent browsers from interpreting user inputs as HTML or JavaScript. In web frameworks, use built-in functions for safe output rendering, such as htmlspecialchars() in PHP or escapeHTML() in JavaScript.
- Many web frameworks (like Django, Ruby on Rails, and React) have built-in mechanisms to prevent HTML injection by default. For example, React automatically escapes any dynamic content to prevent script injection.