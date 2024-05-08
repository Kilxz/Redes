import socket
import threading

#Función utilizada para enviar mensajes a través de la red
def cliente(ip):
    """
    La función es utilizada para enviar mensajes a través de la red. Se crea un socket utilizado solo
    para enviar mensajes. Luego, se habilita para enviar mensajes a la ip de broadcast. Luego, se
    repite el bucle solicitando un input y enviando lo que se coloque en él. Cuando el mensaje es "exit", el
    bucle termina y el programa también.

    :param user: Nombre de usuario que se utilizará para enviar mensajes.
    :return: 0. Para indicar que la función ha terminado correctamente.

    """
    global stop
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
    while. Cuando se recibe un mensaje, se decodifica y se imprime en pantalla con el formato solicitado.
    Si el mensaje es "exit", se imprime en pantalla que el usuario ha abandonado la conversación, si es "nuevo" se
    indica que un nuevo usuario se ha unido a la conversación y si es cualquier otro mensaje, se imprime en pantalla.

    :return: 0. Para indicar que la función ha terminado correctamente.
    """
    global stop
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.bind(('0.0.0.0', 60001))
    socketServer.listen(5)
    while stop != True:
        (cliente, address) = socketServer.accept()
        message = cliente.recv(100).decode("utf-8")
        if message == "exit":
            stop = True
    print(message)

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
    ip = input("Ingrese ip: ")
    ip = "10.65.4.102"
    stop = False
    while stop == False:
        thread1 = threading.Thread(name="Server",target=server)
        thread2 = threading.Thread(name="Client",target=cliente, args=(ip,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    return 0

initialize()