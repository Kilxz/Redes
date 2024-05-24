<?php
$mail = $_POST["email"];
$condition = false;
$opcion = null;

//Se verifica que el archivo de mails exista, si existe se verifica que el mail no este en el archivo. Si se encuentra, condition se vuelve true, caso contrario permanece en false
if (file_exists("email.txt")) {
    $file = fopen("email.txt", "r");
    while (($line = fgets($file)) !== false) {
        if (trim($line) == $mail) {
            $condition = true;
            break;
        }
    }
    fclose($file);
}

//Si el mail no fue encontrado (condition == false), se guarda el mail en el archivo email.txt y se verifica si existe el archivo de votos votos.txt.
//Si el archivo no existe, se procede a crearlo, insertando todos los equipos con los votos inicializados en 0.
if ($condition == false) {
    $file = fopen("email.txt", "a");
    fwrite($file, $mail . PHP_EOL);
    fclose($file);
    $mail = $_POST["opcion"];
    if (file_exists("votos.txt") == false) {
        $file = fopen("votos.txt", "a");
        fwrite($file, "Boca: 0" . PHP_EOL);
        fwrite($file, "River: 0" . PHP_EOL);
        fwrite($file, "Racing: 0" . PHP_EOL);
        fwrite($file, "San Lorenzo: 0" . PHP_EOL);
        fwrite($file, "Otro: 0" . PHP_EOL);
        fclose($file);
    }
    //Se procede a recuperar la opción elegida por el usuario en el formulario y se incrementa en 1 el voto correspondiente en el archivo votos.txt
    $opcion = $_POST["opcion"];
    $file = fopen("votos.txt", "r+");
    while (($line = fgets($file)) !== false) {
        $lista = explode(": ", $line);
        if (trim($lista[0]) == $opcion) {
            $valor = intval($lista[1]) + 1;
            break;
            
        }
    }
    //Se reemplaza en el archivo votos.txt el valor anterior por el nuevo valor
    fclose($file);
    file_put_contents("votos.txt", str_replace($opcion . ": " . $lista[1] , $opcion . ": " . strval($valor) . PHP_EOL, file_get_contents("votos.txt")));
}
//Se redirige al usuario a la página principal con el parametro redirected en true
header("Location: index.php?redirected=true");
?>