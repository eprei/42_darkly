## Exploit

On the login page: "/?page=signin" there is no mechanism to prevent a brute force attack.<br>
We assume that there is a admin username.<br>
We take a list of most common passwords : https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt <br>
and brute force the login get request with the python script.
We login with admin and the password found.


## Patch
