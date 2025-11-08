<!DOCTYPE html>
<html>
<body>
    <h2>Secured Ping</h2>
    <form method="POST">
        Enter IP: <input type="text" name="ip" placeholder="127.0.0.1">
        <button type="submit">Submit</button>
    </form>

    <?php
    if (isset($_POST['ip'])) {
        $target = $_POST['ip'];

        // MITIGATION: Validate that the input is EXACTLY an IP address.
        if (filter_var($target, FILTER_VALIDATE_IP)) {
            $cmd = shell_exec('ping -c 4 ' . $target);
            echo "<pre>$cmd</pre>";
        } else {
            // If input contains characters like ';' or '&&', it fails validation.
            echo "<pre style='color:red;'>ERROR: Invalid IP address detected.</pre>";
        }
    }
    ?>
</body>
</html>