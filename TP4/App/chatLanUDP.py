import socket
import threading

#Función utilizada para construir el mensaje en el formato solicitado Usuario:Mensaje
def buildMessage(msg, usuario):
    return usuario + ": " + msg

#Función utilizada para decodificar el mensaje en el formato solicitado Usuario:Mensaje
def decodeMessage(msg):
    return msg.split(": ")

#Función utilizada para enviar mensajes a través de la red
def speak(user):
    """
    La función es utilizada para enviar mensajes a través de la red. Se crea un socket utilizado solo
    para enviar mensajes. Luego, se habilita para enviar mensajes a la ip de broadcast. Luego, se
    repite el bucle solicitando un input y enviando lo que se coloque en él. Cuando el mensaje es "exit", el
    bucle termina y el programa también.

    :param user: Nombre de usuario que se utilizará para enviar mensajes.
    :return: 0. Para indicar que la función ha terminado correctamente.

    """
    global stop
    socketSpeak = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketSpeak.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    direction = ('192.168.1.255', 60000)
    welcome = buildMessage("nuevo", user)
    socketSpeak.sendto(welcome.encode(), direction)
    while stop != True:
        message = input()
        socketSpeak.sendto(buildMessage(message, user).encode(), direction)

        if message == "exit":
            stop = True
            socketSpeak.close()
    return 0

def listen():
    """
    La función es utilizada para escuchar mensajes a través de la red. Se crea
    un socket utilizado solamente para escuchar. Se escucha continuamente gracias al bucle
    while. Cuando se recibe un mensaje, se decodifica y se imprime en pantalla con el formato solicitado.
    Si el mensaje es "exit", se imprime en pantalla que el usuario ha abandonado la conversación, si es "nuevo" se
    indica que un nuevo usuario se ha unido a la conversación y si es cualquier otro mensaje, se imprime en pantalla.

    :return: 0. Para indicar que la función ha terminado correctamente.
    """
    global stop
    socketListen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketListen.bind(('0.0.0.0', 60000))
    while stop != True:
        received = socketListen.recvfrom(128)
        ip = received[1][0]
        message2 = decodeMessage(received[0].decode())
        user = message2[0]
        message2 = message2[1]

        if message2 == "exit":
            print("El usuario " + user + " (" + ip + ") ha abandonado la conversación.")
        elif message2 == "nuevo":
            print("El usuario " + user + " se ha unido a la conversación.")
        else:
            print(user + " (" + ip + ") dice: " + message2)

    return 0

#Función utilizada para inicializar el chat
def initialize():
    """
    Función utilizada para inicializar el chat. Se solicita el nombre de usuario del
    usuario y se inicializan los dos hilos, uno destinado a escuchar y el otro a enviar mensajes.
    Se inician ambos hilos y se espera a que terminen. Cuando terminan, se retorna 0 para indicar que se
    finalizó correctamente.

    :return: 0. Para indicar que la función ha terminado correctamente.
    """
    global stop
    userName = input("Ingrese nombre de usuario: ")
    stop = False
    thread1 = threading.Thread(name="listen",target=listen, daemon=True)
    thread2 = threading.Thread(name="speak",target=speak, args=(userName,))
    thread1.start()
    thread2.start()
    thread2.join()
    return 0
