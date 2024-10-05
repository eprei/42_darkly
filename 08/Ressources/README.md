# Information disclosure

## Exploit

go to <http://xxx.xx.xx.x/robots.txt>\
You find this: \
`User-agent: *`\
`Disallow: /whatever`\
`Disallow: /.hidden`\
In /whatever we find htpasswd :"root:437394baff5aa33daa618be47b75cb49"\
[md5.gromweb.com](https://md5.gromweb.com/) 437394baff5aa33daa618be47b75cb49 => qwerty123@\
Go to `http://172.20.10.6/admin/` username: root, password: qwerty@\

## Patch

The primary purpose of robots.txt is to instruct well-behaved crawlers about which parts of your website they should avoid indexing.
It is not a security feature and should not be used to hide sensitive or private data. Crawlers can still bypass the robots.txt rules, and anyone can view this file.

Do not list sensitive directories (e.g., admin panels, user data, configuration files) in robots.txt. Although this can prevent indexing, it publicly advertises these directories, making them easy for attackers to find.
Instead, sensitive content should be protected using proper authentication and authorization mechanisms or by placing them outside of the web root.

## Resources

[PortSwigger information-disclosure](https://portswigger.net/web-security/information-disclosure)
