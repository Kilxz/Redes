from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/encuesta")

@app.route("/encuesta")
def encuesta():
    return render_template("encuesta.html", estado = "inicio")
    
@app.route("/resultados", methods = ["POST"])
def resultados():
    if request.method == "POST":
        email = request.form["email"]
        if validarMail(email):
            votos = contabilizarResultado(email, request.form["opcion"])
            return render_template("encuesta.html", votos = votos)
        else:
            return redirect("/encuesta")
        
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

def contabilizarResultado(email, res):

    condition = verificarExistenciaMail(email)
    
    if condition == True:
        return getResultadosActuales()
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
        return contentList


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
    
especiales = ["*", "+", "-", "/", "(", ")", "[", "]", "{", "}", ":", ";", ",", "<", ">", "=", "?", "¿", "!", "¡", "°", "¬"]
def validarMail(mail):
    if len(mail) < 7:
        return False
    if mail.find("@") == -1:
        return False
    if (mail.find(".") == -1) or mail.find(".") == 0  or mail.find(".") == len(mail)-1:
        return False
    for i in range(len(especiales)):
        if mail.find(especiales[i]) != -1:
            return False
    return True
        