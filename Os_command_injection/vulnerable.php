<!DOCTYPE html>
<html>
<body>
    <h2>Vulnerable Ping</h2>
    <form method="POST">
        Enter IP: <input type="text" name="ip" placeholder="127.0.0.1">
        <button type="submit">Submit</button>
    </form>

    <?php
    if (isset($_POST['ip'])) {
        $target = $_POST['ip'];

        // VULNERABILITY: User input is concatenated directly into the shell command.
        // Windows uses 'ping -n 4', Linux uses 'ping -c 4'. Adjust if needed.
        $cmd = shell_exec('ping -c 4 ' . $target);

        echo "<pre>$cmd</pre>";
    }
    ?>
</body>
</html>