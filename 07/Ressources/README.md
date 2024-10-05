## Exploit

go to <http://xxx.xx.xx.x/robots.txt>\
You find this: \
`User-agent: *`\
`Disallow: /whatever`\
`Disallow: /.hidden`\
In /.hidden we find a lot of links. When we follow theses links at the end we find README.\
The script getAllReadme.py collect all the README content and find the flag.\
(you will need to install beautifulsoup4 to use it)\
`pip install requests beautifulsoup4`

## Patch

The primary purpose of robots.txt is to instruct well-behaved crawlers about which parts of your website they should avoid indexing.
It is not a security feature and should not be used to hide sensitive or private data. Crawlers can still bypass the robots.txt rules, and anyone can view this file.

Do not list sensitive directories (e.g., admin panels, user data, configuration files) in robots.txt. Although this can prevent indexing, it publicly advertises these directories, making them easy for attackers to find.
Instead, sensitive content should be protected using proper authentication and authorization mechanisms or by placing them outside of the web root.

## Resources

[PortSwigger information-disclosure](https://portswigger.net/web-security/information-disclosure)
