# Client Side URL Redirect

## Exploit

On the home page, in the footer there are social media icons that redirects user to facebook, twitter or instagram.\
The problem is that the value of the query parameter "site" can be changed by the user (directly in the html code or with curl).\
The back end doesn't check the value and redirect the user to whatever site we ask.\
`curl http://172.20.10.4/?page=redirect&site=google | grep "the flag"`

## Patch

- Do not allow user-controlled input to dictate the redirect destination directly without proper validation. This is the most common source of vulnerability.
- If possible, avoid the use of redirects based on user input altogether.
- Use a Whitelist of Allowed URLs

## Resources

[OWASP Client Side URL Redirect](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/04-Testing_for_Client_Side_URL_Redirect)
