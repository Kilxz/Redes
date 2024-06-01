import websockets;
import asyncio;

#Lista en la que se guardan los clientes conectados
listaClientes = []
#Función que maneja los mensajes recibidos por los clientes
async def handler(websocket):

    listaClientes.append(websocket)

    while True:
        try:
            #Se recibe el mensaje del websocket cliente con el formato "mail,mensaje"
            mensaje = await websocket.recv()
            mensaje = mensaje.split(",")
            messageReceived = None

            #Si el mensaje recibido es Conectado, se envian los datos que cargaran los votos que se tienen hasta el momento en el cliente
            if mensaje[1] == "Conectado":
                await cargarDatos(websocket)
                enviar = None
                pass

            #Si el mensaje recibido no es Conectado, se verifica si el mail recibido ya emitió un voto, si no lo hizo, se continua con el bucle
            if verificarMail(mensaje[0]) == True:
                pass
            else:
                messageReceived = mensaje[1]

            #Según el mensaje recibido, se almacena en la variable enviar la respuesta que será enviada a todos los clientes conectados
            if messageReceived == "Boca":
                enviar = "bocares,1"
            elif messageReceived == "River":
                enviar = "riverres,1"
            elif messageReceived == "Racing":
                enviar = "racingres,1"
            elif messageReceived == "San Lorenzo":
                enviar = "sanlorenzores,1"
            elif messageReceived == "Otro":
                enviar = "otrores,1"
            else:
                enviar = None
            
            #Si la variable enviar posee una respuesta, esta se envía a todos los clientes conectados, almacenados en la listaClientes
            if enviar != None:
                for i in range(0, len(listaClientes)):
                    await listaClientes[i].send(enviar)
                enviar = None
        #Cuando se cierra la conexión con el cliente, se elimina de la lista de clientes conectados
        except websockets.ConnectionClosedOK:
            listaClientes.remove(websocket)
            break

#Función utilizada para cargar todos los votos existentes hasta el momento en la página que visualiza el cliente
async def cargarDatos(websocket):
    f = open("votos.txt", "r")
    datos = f.readline()
    #Se lee cada linea del archivo que almacena los votos, votos.txt
    while datos:
        #Se obtiene por cada equipo una lista de la forma [equipo, votos]
        descomponer = datos.strip().split(": ")
        #Se prepara el mensaje a enviar, que será de la forma "equipores,votos". equipores, por ejemplo, bocares, es el id que identifica a cada elemento
        enviar = descomponer[0].replace(" ", "").lower() + "res," + descomponer[1]
        #Se envía el mensaje al cliente
        await websocket.send(enviar)
        datos = f.readline()
    f.close()
    return

#Función utilizada para verificar que el mail no exista en el archivo que almacena los mails, email.txt. Si se encuentra retorna True, caso contrario False
def verificarMail(mail):
    f = open("email.txt", "r")
    datos = f.readline()
    while datos:
        if datos.strip() == mail:
            f.close()
            return True
        datos = f.readline()
    f.close()
    return False

#Inicializa el socket en la dirección ip establecida y el puerto indicado
async def main():
    async with websockets.serve(handler, "192.168.1.47", 60000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())