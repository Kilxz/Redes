from flask import Flask, render_template, request, redirect, url_for
import os

# Se crea el objeto Flask que se encargará de manejar la aplicación.
app = Flask(__name__)

# Se encarga de manejar la página de inicio. Redirige a la página de encuesta con el status inicio.
@app.route("/")
def index():
    return redirect(url_for("encuesta", status = "inicio"))

# Se encarga de mostrar la página de encuesta. En caso de que se haya ingresado un mail inválido, se muestra un mensaje de error. En caso de que se haya seleccionado una opción inválida, se muestra un mensaje de error.
@app.route("/encuesta/<status>")
def encuesta(status):
    if status == "error":
        return render_template("encuesta.html", estado = "inicio", error = "email") 
    elif status == "error2":
        return render_template("encuesta.html", estado = "inicio", error = "opcion")
    else:
        return render_template("encuesta.html", estado = "inicio")

# Se encarga de recibir los datos del formulario y redirigir a la página de resultados. En caso de que el mail ingresado no sea válido, se redirige a la página de encuesta con un mensaje de error.
# En el caso de que sí sea válido, se llama a la función contabilizarResultado, que se encarga de verificar si el mail ya está en el archivo y de contabilizar el voto. Finalmente se muestra la página de resultados.
@app.route("/resultados", methods = ["POST"])
def resultados():
    if request.method == "POST":
        email = request.form["email"]
        if request.form.get("opcion") == None:
            return redirect(url_for("encuesta", status = "error2"))
        if validarMail(email):
            votos, condition = contabilizarResultado(email, request.form["opcion"])
            if condition == True:
                return render_template("encuesta.html", votos = votos, estado = "resultados", error = "votoingresado")
            else:
                return render_template("encuesta.html", votos = votos, estado = "resultados")
        else:
            return redirect(url_for("encuesta", status = "error"))


# Verifica que el mail ingresado no esté en el archivo, y, en el caso de estar, lo incorpora. Si no está, devuelve False, si está, devuelve True
def verificarExistenciaMail(email):
    filePath = "email.txt"
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            for line in file:
                if line.strip() == email:
                    return True

    with open(filePath, "a") as file:
        file.write(email + "\n")
    return False


# Verifica que el mail ingresado no esté en el archivo, y, en el caso de estar, devuelve una lista con los votos actuales.
# Si el mail no está, incorpora el voto y devuelve una lista con los votos actualizados. Además, se devuelve una variable booleana que indica True si el mail ya estaba en el archivo, y False si no estaba.
def contabilizarResultado(email, res):

    condition = verificarExistenciaMail(email)
    
    if condition == True:
        return getResultadosActuales(), condition
    else:
        file = "votos.txt"

        if not os.path.exists(file):
            with open(file, "a") as file2:
                file2.write("Boca: 0\n")
                file2.write("River: 0\n")
                file2.write("Racing: 0\n")
                file2.write("San Lorenzo: 0\n")
                file2.write("Otro: 0\n")
        contentList = []
        with open(file, "r") as lines:
            for line in lines:
                content = line.split(": ")
                if content[0] == res:
                    content[1] = str(int(content[1]) + 1) + "\n"
                contentList.append(content)
        with open(file, "w") as file2:
            for i in range (0, len(contentList)):
                file2.write(contentList[i][0] + ": " + contentList[i][1])
                contentList[i] = contentList[i][1]
        return contentList, condition


# Devuelve una lista con los votos actuales
def getResultadosActuales():
    contentList = []
    file = "votos.txt"
    if os.path.exists(file):
        with open(file, "r") as lines:
                for line in lines:
                    content = line.split(": ")
                    contentList.append(content[1])
        return contentList
    else:
        return [[0] * 5]
    
# Verifica que el mail ingresado sea válido. Devuelve True si es válido, False si no lo es. Se verifican ciertos aspectos como la arroba, caracteres especiales, la longitud del mail y la presencia de un punto.
especiales = ["*", "+", "-", "/", "(", ")", "[", "]", "{", "}", ":", ";", ",", "<", ">", "=", "?", "#", "%", "¿", "!", "¡", "°", "¬", "¨", "ç", "^", "`", "$", "&", "!"]
def validarMail(mail):
    if len(mail) < 7:
        return False
    if mail.count("@") != 1:
        return False
    if (mail.find(".") == -1) or mail.find(".") == 0  or mail.find(".") == len(mail)-1:
        return False
    for i in range(len(especiales)):
        if mail.find(especiales[i]) != -1:
            return False
    return True

# Inicializa el programa
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)