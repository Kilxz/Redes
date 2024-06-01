<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Encuesta equipos de fútbol</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div>
        <img src="https://moodle.cuc.uncu.edu.ar/pluginfile.php/1/theme_academi/footerlogo/1713883854/escudo%20uncuyo%20color%202023.png" id="uncuyo"> </img> 
    </div>
    <div id="titulo">
        <h1> ¡Elige tu equipo favorito! </h1> 
    </div>
    <div id="titulo2">
        <h1> ¡Resultados! </h1> 
    </div>
    <div id="formulario">  
        <form name="form" id= "form1" action="verificar.php" method="POST" onsubmit="return validar();">
            <label for="email">Ingrese su email: </label>
            <input type="text" name="email" id=”email_en_email”> <br>
            <input type="radio" id="boca" name="opcion" value="Boca" class="opcionRadio">
            <label for="boca">Boca</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/CABJ70.png/800px-CABJ70.png" class="logo"> </img> <br>
            <input type="radio" id="river" name="opcion" value="River" class="opcionRadio">
            <label for="river">River</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_River_Plate.png" class="logo"> </img> <br>
            <input type="radio" id="racing" name="opcion" value="Racing" class="opcionRadio">
            <label for="racing">Racing</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Escudo_de_Racing_Club_%282014%29.svg" class="logo"> </img> <br>
            <input type="radio" id="sanlorenzo" name="opcion" value="San Lorenzo" class="opcionRadio">
            <label for="sanlorenzo">San Lorenzo</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg/512px-Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg.png" class="logo"> </img> <br>
            <input type="radio" id="otro" name="opcion" value="Otro" class="opcionRadio">
            <label for="otro">Otro</label> <br>
            <p><input type="submit" id ="enviar"></p>
        </form>
    </div>

    <div id="resultados">
        <label for="boca" class="resultadoLab">Boca</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/CABJ70.png/800px-CABJ70.png" class="logo"> </img> <span class="votos"> - Votos: <span id = "bocares">0</span> </span> <br>
        <label for="river" class="resultadoLab">River</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_River_Plate.png" class="logo"> </img> <span class="votos"> - Votos: <span id = "riverres">0</span> </span> <br>
        <label for="racing" class="resultadoLab">Racing</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Escudo_de_Racing_Club_%282014%29.svg" class="logo"> </img> <span class="votos"> - Votos: <span id = "racingres">0</span> </span> <br>
        <label for="sanlorenzo" class="resultadoLab">San Lorenzo</label>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg/512px-Escudo_del_Club_Atl%C3%A9tico_San_Lorenzo_de_Almagro.svg.png" class="logo"> </img> <span class="votos"> - Votos: <span id = "sanlorenzores">0</span> </span> <br>
        <label for="otro" class="resultadoLab">Otro</label> <span class="votos"> - Votos: <span id = "otrores">0</span> </span> <br>
    </div>
    <script src="code.js"></script>
</body>
</html>