# Flawed validation of uploaded file


## Exploit

See the file 42_darkly/12/Ressources/exploit.sh

The /?page=upload page allows to upload files whose content is not properly validated.
The server validates the files by relying on the `Content-Type` specified in the request.
This allows uploading any type of file simply by specifying `Content-Type: image/jpeg` in the request.

## Patch

- Use an established framework for preprocessing file uploads rather than attempting to write your own validation mechanisms
- Verify certain intrinsic properties of an image, such as its dimensions
- Verify the fingerprint or signature of the files. JPEG files always begin with the bytes FF D8 FF
- No validation method is infallible by itself, so it is good to implement several validations
- Do not upload files to the server's permanent filesystem until they have been fully validated


## Resources

[PortSwigger File Upload Vulnerability](https://portswigger.net/web-security/file-upload)
