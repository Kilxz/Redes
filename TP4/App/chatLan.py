import socket
import threading

def buildMessage(msg, usuario):
    return usuario + ": " + msg

def decodeMessage(msg):
    return msg.split(": ")

def speak(user):
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

def listen():
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

def initialize():
    global stop
    userName = input("Ingrese nombre de usuario: ")
    stop = False
    while stop == False:
        thread1 = threading.Thread(name="listen",target=listen)
        thread2 = threading.Thread(name="speak",target=speak, args=(userName,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    return
