function validar(email) {
    var email = document.getElementById("email_en_email").value;
    if (email.length < 7) {
        alert("Email inválido");
        return false;
    } else {
        if (verificararroba(email)) {
            if (verificarespecial(email)) {
                return true;
            } else {
                alert("Email inválido");
                return false;
            }
        } else {
            alert("Email inválido");
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
    len = email.length;
    for (var i = 0; i < len; i++) {
        if (email[i] == ".") {
            if (i == 0 || i == (len - 1)) {
                return false;
            }
        } else {
            return true;
        }
    }
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