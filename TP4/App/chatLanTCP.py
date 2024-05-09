import socket
import threading

#Función utilizada para enviar mensajes a través de la red
def cliente():
    """
    La función es utilizada para enviar mensajes a través de la red. Se crea un socket utilizado solo
    para enviar mensajes y se conecta a la dirección IP ingresada en el puerto 60001. Luego, se
    repite el bucle solicitando un input y enviando lo que se coloque en él. Cuando el mensaje es "exit", el
    bucle termina y el programa también al cambiar el valor de la variable global "stop" a True

    :return: 0. Para indicar que la función ha terminado correctamente.

    """
    global stop
    ip = input("Ingrese ip: ")
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((ip, 60001))
    while stop != True:
        message = input()
        socketClient.send(message.encode())
        if message == "exit":
            stop = True
            socketClient.close()
    return 0

def server():
    """
    La función es utilizada para escuchar mensajes a través de la red. Se crea
    un socket utilizado solamente para escuchar. Se escucha continuamente gracias al bucle
    while. Cuando se recibe un mensaje, se decodifica y se imprime en pantalla.
    Si el mensaje es "exit", se cambia la variable global "stop" a True y se termina el bucle.

    :return: 0. Para indicar que la función ha terminado correctamente.
    """
    global stop
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.bind(('0.0.0.0', 60001))
    socketServer.listen(5)
    (cliente, address) = socketServer.accept()
    while stop != True:
        message = cliente.recv(100).decode("utf-8")
        if message == "exit":
            stop = True
        print(message)
    socketServer.close()
    return 0

#Función utilizada para inicializar el chat
def initialize():
    """
    Función utilizada para inicializar el chat. Se inicializan los dos hilos como daemon, uno destinado a escuchar y el otro a enviar mensajes.
    Se inician ambos hilos y se espera a que terminen. Cuando terminan, se retorna 0 para indicar que se
    finalizó correctamente. La variable global stop se controla dentro del while, si en algún momento se recibe o envía un mensaje con la palabra "exit", se cambia a True y se termina el bucle. Por lo que
    los hilos daemon terminaran y se cerrará el programa.

    :return: 0. Para indicar que la función ha terminado correctamente.
    """
    global stop
    stop = False
    thread1 = threading.Thread(name="Server",target=server, daemon=True)
    thread2 = threading.Thread(name="Client",target=cliente, daemon=True)
    thread1.start()
    thread2.start()
    while stop == False:
        pass
    print("Saliendo...")
    return 0