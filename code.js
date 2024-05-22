function validar() {
    var email = document.forms["form1"]["email"].value;
    if (email.length < 7) {
        alert("Email inválido. La longitud mínima es de 7 caracteres.");
        return false;
    } else {
        if (verificararroba(email)) {
            if (verificarespecial(email)) {
                if (verificarpunto(email)) {
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