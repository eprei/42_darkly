## Exploit

Lack of server-side file validation allows uploading any type of file.
http://[Darkly IP]/?page=upload#

create a script.php.jpg file\
upload it to the site\
intercept the request between the browser and the server\
modify the file name to script.php\

## Patch

## Resources

[PortSwigger File Upload Vulnerability](https://portswigger.net/web-security/file-upload)
