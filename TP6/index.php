<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Encuesta equipos de fútbol</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script src="code.js"></script>
</head>
<body>
    <div>
        <h1>Encuesta Equipos de Fútbol</h1>
    </div>
    <div>
        <img src="https://www.uncuyo.edu.ar/assets/imgs/logo_uncu23.png"> </img> 
    </div>
    <div id="formulario">
        <form name="form" id= "form1" action="verificar.php" method="POST" onsubmit="return validar();">
        <label for="email">Ingrese su email: </label>
        <input type="text" name="email" id=”email_en_email”>
        <br> <br>
        <input type="radio" id="boca" name="opcion" value="boca">
        <label for="boca">Boca</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/CABJ70.png/800px-CABJ70.png" class="logo"> </img> <br>
        <input type="radio" id="river" name="opcion" value="river">
        <label for="river">River</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_River_Plate.png" class="logo"> </img> <br>
        <input type="radio" id="racing" name="opcion" value="racing">
        <label for="racing">Racing</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Escudo_de_Racing_Club_%282014%29.svg" class="logo"> </img> <br>
        <input type="radio" id="sanlorenzo" name="opcion" value="sanlorenzo">
        <label for="sanlorenzo">San Lorenzo</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg/512px-Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg.png" class="logo"> </img> <br>
        <input type="radio" id="otro" name="opcion" value="otro">
        <label for="otro">Otro</label><br>
        <p><input type="submit" id = "enviar"></p>
    </div>
</form>
</body>
</html>