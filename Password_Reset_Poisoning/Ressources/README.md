# Password reset poisoning

## Exploit

See the file 42_darkly/13/Ressources/exploit.sh

Reading the request sent by the password recovery page (/?page=recover) during the password recovery process shows that the site is vulnerable to a `password reset poisoning` attack.

This is because the `mail` parameter is sent directly by `POST` and there does not seem to be any proper verification of the identity of the user requesting the reset.

By simply modifying the `mail` parameter in the body of the request we can choose where we want to send the password recovery mail to.

## Patch

- Properly verify the identity of the user requesting the reset
- Require current password for critical changes
- Multifactor verification

## Resources

[PortSwigger Password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning)
