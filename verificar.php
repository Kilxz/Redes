<?php
$mail = $_POST["email"];
$condition = false;
echo "hola";

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

    $opcion = $_POST["opcion"];
    $file = fopen("votos.txt", "r+");
    echo $opcion . " ";
    while (($line = fgets($file)) !== false) {
        $lista = explode(": ", $line);
        if (trim($lista[0]) == $opcion) {
            $valor = intval($lista[1]) + 1;
            echo $valor . "  ";
            break;
            
        }
    }
    fclose($file);

    echo $opcion . ": " . $lista[1] . "   ";
    echo $opcion . ": " . strval($valor);
    file_put_contents("votos.txt", str_replace($opcion . ": " . $lista[1] , $opcion . ": " . strval($valor) . PHP_EOL, file_get_contents("votos.txt")));
}

?>