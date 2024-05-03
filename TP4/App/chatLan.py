import socket
import threading

def speak():
    global stop
    socketSpeak = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    direction = ('192.168.1.255', 60000)
    print("Ingrese el mensaje a enviar: ")
    message = input()
    if message == "salir":
        stop = True
    socketSpeak.sendto(message.encode(), direction)
    socketSpeak.close()

def listen():
    socketListen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketListen.bind(('0.0.0.0', 60000))
    received = socketListen.recvfrom(128)
    message = received[0].decode()
    if message == "salir":
        print("El otro usuario ha salido")
    else:
        print("Mensaje recibido: ", message)

def initialize():
    global stop
    stop = False
    while stop == False:
        thread1 = threading.Thread(name="listen",target=listen)
        thread2 = threading.Thread(name="speak",target=speak)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    
