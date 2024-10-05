# Cookie Poisoning

## Exploit

The cookie that we store in the browser has a name:\
I_am_admin and a value of: 68934a3e9455fa72420237eb05902327\
If we reverse the value [md5.gromweb.com](https://md5.gromweb.com/).\
We can see that it is the string "false".\
Let's convert "true" to a MD5 hash and we get: b326b5062b2f0e69046810717534cb09\
If we change the cookie value and send it on any page, we get the flag.

`curl -b "I_am_admin=b326b5062b2f0e69046810717534cb09" "http://172.20.10.3/" | grep 'Flag : '`

## Patch

MD5 hashes are theoretically impossible to reverse directly, ie, it is not possible to retrieve the original string from a given hash using only mathematical operations. \
Unfortunately, there is a way to decrypt a MD5 hash, using a dictionary populated with strings and their MD5 counterpart. As most users use very simple passwords (like "123456", "password", "abc123", etc), MD5 dictionaries make them very easy to retrieve. \
Consider using another way of generating hashes, like using stronger algorithms (SHA-2, Whirlpool, etc), combining algorithms, and using a "salt".

## Resources

[Cookie Poisoning](https://www.invicti.com/learn/cookie-poisoning/)
