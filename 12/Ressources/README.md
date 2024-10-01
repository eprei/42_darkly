## Exploit

Lack of server-side file validation allows uploading any type of file.
http://[Darkly IP]/?page=upload#

create a script.php.jpg file<br>
upload it to the site<br>
intercept the request between the browser and the server<br>
modify the file name to script.php<br>


## Patch


## Resources
[PortSwigger File Upload Vulnerability](https://portswigger.net/web-security/file-upload)