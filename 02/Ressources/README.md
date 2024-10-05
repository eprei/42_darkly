# Sensitive info in comments

## Exploit

On the page \
`/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f` \
 there is some comments in the HTML code. \
`You must come from : "https://www.nsa.gov/"`.\
`Let's use this browser : "ft_bornToSec". It will help you a lot.`

So we add: \
User-Agent: ft_bornToSec \
Referer: <https://www.nsa.gov/> \
to the request Headers and we get the flag.

`curl -H "User-Agent: ft_bornToSec" -H "Referer: https://www.nsa.gov/" "http://172.20.10.3/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
| grep 'The flag is'`

## Patch

Leaving sensitive information in the code comments is a security risk.
It’s considered a best practice to avoid leaving such comments in production environments. Make sure to remove or sanitize any comments that might expose internal workings or security details of your application.
