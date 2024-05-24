//Función utilizada para validar el mail ingresado. Se verifica la longitud, la arroba, caracteres especiales y la presencia de un punto.
//Se devuelve true si es correcta la forma ingresada y false si no lo es.
function validar() {
    var email = document.forms["form1"]["email"].value;
    if (email.length < 7) {
        alert("Email inválido. La longitud mínima es de 7 caracteres.");
        return false;
    } else {
        if (verificararroba(email)) {
            if (verificarespecial(email)) {
                if (verificarpunto(email)) {
                    enviarAServer(email);
                    return true;
                } else {
                    alert("Email inválido. Puntos incorrectos.");
                    return false;
                }
            } else {
                alert("Email inválido. No debe utilizar caracteres especiales.");
                return false;
            }
        } else {
            alert("Email inválido. Debe poseer solo una arroba.");
            return false;
        }
        
    }
}

//Función que verifica la presencia de una arroba, pero no al principio ni al final del mail. Devuelve true si se encuentra, false si no
function verificararroba(email) {
    len = email.length;
    count = 0;
    for (var i = 0; i < len; i++) {
        if (email[i] == "@") {
            count = count + 1;
            if (i == 0 || i == (len - 1)) {
                return false;
            }
        }
    }
    if (count == 1) {
        return true;
    } else {
        return false;
    }
}

//Función que verifica la presencia de un punto, pero no al principio ni al final del mail. Devuelve true si es correcto, false si no.
function verificarpunto(email) {
    var len = email.length;
    for (var i = 0; i < len; i++) {
        if (email[i] == ".") {
            if (i == 0 || i == (len - 1)) {
                return false;
            }
        }
    }
    return true;
}

//Función que verifica la presencia de caracteres especiales en el mail. Devuelve true si no hay caracteres especiales, false si los hay.
function verificarespecial(email) {
    var len = email.length;
    var especial = ["#", "$", "%", "&", "*", "/", "(", ")", "=", "?", "¡", "¿", "!", "¨", "´", "{", "}", "[", "]", ":", ";", ",", "<", ">", "+", "-", "_", "°", "|", "¬", "·", "~", "´"];
    for (var i = 0; i < especial.length; i++) {
        if (email.indexOf(especial[i]) !== -1) {
            return false;
        }
    }
    return true;
}

var socketCliente;
//Función que verifica si el ingreso a la página es de una redirección proveniente del servidor.
function verificarRedireccion() {
    const enlace = new URLSearchParams(window.location.search);
    if (enlace.has("redirected")) {
        definirSocket();
        irSegundaPagina();
    } else {
        //Se crea un websocket cliente para la comunicación con el servidor.
        socketCliente = new WebSocket("ws://192.168.1.47:60000");
    }
}
//Función que actualiza la página, ocultando elementos y mostrando otros con el objetivo de mostrar los resultados.
function irSegundaPagina() {
    const div1 = document.getElementById("formulario");
    div1.style.display = "none";
    const div2 = document.getElementById("resultados");
    div2.style.display = "block";
    const divtitulo2 = document.getElementById("titulo2");
    divtitulo2.style.display = "block";
    const divtitulo1 = document.getElementById("titulo");
    divtitulo1.style.display = "none";
}

//Función que envía el mail y la opción ingresada para ser procesados por el servidor.
function enviarAServer(email) {
    //Recupera el valor de la opción seleccionada.
    var opcionsel = document.querySelector('input[name="opcion"]:checked').value;
    if (opcionsel != null) {
        //Envía el mail y la opción seleccionada al servidor.
        socketCliente.send(email + "," + opcionsel);
    }
};

//Crea el socket cliente. Además, al conectarse envía el mensaje "Cliente,Conectado" al servidor.
function definirSocket() {
    socketCliente = new WebSocket("ws://192.168.1.47:60000");
    socketCliente.onopen = function() { 
        socketCliente.send("Cliente,Conectado");
    }
    //Cuando se recibe un mensaje se realiza la actualización de los resultados en la página. Al valor actual se le suma el valor recibido.
    socketCliente.onmessage = function (event) {
        var mensaje = event.data;
        mensaje = mensaje.split(",");
        var datoActual = document.getElementById(mensaje[0]).textContent
        document.getElementById(mensaje[0]).textContent = parseInt(datoActual) + parseInt(mensaje[1]);
        console.log("Resultado actualizado");
    }
}

//Al cargar el archivo se verifica si se está redirigiendo desde el servidor.
window.onload = verificarRedireccion();
