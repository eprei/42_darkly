## Exploit
On the page "/index.php?page=survey#" we can select a grade between 1 and 10 for a subject. <br>
But the backend doesn't check that the value is between 1 and 10.<br>
Sending a value higher than 10 is triggering the flag to be shown.

`curl 'http://172.20.10.3/index.php?page=survey#' --data 'sujet=2&valeur=11' | grep 'The flag is'`


## Patch
All data coming from the frontend should be treated as untrusted because it can potentially be manipulated by users.
For proper security, you should always validate and sanitize inputs on the backend, regardless of whether the same validation is performed on the frontend.