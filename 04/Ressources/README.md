# Login brute force attack

## Exploit

On the login page: "/?page=signin" there is no mechanism to prevent a brute force attack.\
We assume that there is a admin username.\
We take a list of most common passwords : <https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt> \
and brute force the login get request with the python script.
We login with admin and the password found.

## Patch

There are many techniques to mitigate the risk of brute force attacks:

- limit the number of login attempts in a specific timeframe (e.g., 5 per minutes)
- Temporality lock the account after a certain number of failed attempts.
- Use of Captcha
- Two-Factor Authentication
- Password Complexity Requirements

## Resources

[OWASP Weak Password](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing/07-Testing_for_Weak_Password_Policy)
