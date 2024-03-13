""" Para realizar el trabajo se tomó un enfoque que utiliza etapas, es decir, la fase de "búsqueda" de la bandera se da en la etapa 0, luego,
en la etapa 1 se verifica la longitud y se pasa a la etapa 2, en ella se va "contando", sumando y se va verificando que no aparezca una nueva bandera 7E en medio, por último, en la
etapa 3 se verifica el checksum de la trama utilizando la información de la anterior etapa. 

Se realizó utilizando este enfoque para lograr una complejidad temporal de O(n) """

#Verifica la suma del checksum
def checkSum(suma, verificador):
    sumaDec = 255 - (suma & int("FF", 16))
    return sumaDec == int(verificador, 16)


#Se abre el archivo
fileLine = open("/home/estudiante/Redes/TP1/Tramas_802-15-4.log", "r")
line = fileLine.readline()

#Se declaran variables y se inicializan
i = 0
etapa = 0
incorrectas = 0
correctas = 0
correctasVerif = 0
total = 0
incorrectasVerif = 0
suma = 0
cantSecuenciaEscape = 0
flag = False
decLength = 0
longIncorrecta = False

#Loop de las etapas explicadas anteriormente
while (i < len(line)):
    #En la etapa 0 se busca la flag 7E
    if (etapa == 0):
        suma = 0
        
        actualByte = line[i:i+2]
        #Se busca la bandera "7E"
        if ((i == 0) and (actualByte == "7E")):
            #Agregado en caso de que la longitud fuese mayor a la mencionada en el campo longitud. Permite imprimir al final la trama errónea completa
            if longIncorrecta == True:
                print("La trama", total - 1, "tiene longitud incorrecta. Trama: ", acumuladorTrama)
                longIncorrecta = False
            etapa = 1
            total = total + 1
            secuenciaEscape = False
            #Se añade una variable que funcione como acumuladora de la trama
            acumuladorTrama = ""
            acumuladorTrama = acumuladorTrama + actualByte
        #Se verifica que no exista secuencia de escape
        elif ((actualByte == "7D") and (line[i + 2 : i + 4] == "7E")):
            cantSecuenciaEscape = cantSecuenciaEscape + 1
            secuenciaEscape = True
            actualByte = "7E"
            i = i + 2
            acumuladorTrama = acumuladorTrama + actualByte
        elif (actualByte == "7E"):
            #Agregado en caso de que la longitud fuese mayor a la mencionada en el campo longitud. Permite imprimir al final la trama errónea completa
            if longIncorrecta == True:
                print("La trama", total - 1, "tiene longitud incorrecta. Trama: ", acumuladorTrama)
                longIncorrecta = False
            etapa = 1
            secuenciaEscape = False
            total = total + 1
            #Se añade una variable que funcione como acumuladora de la trama
            acumuladorTrama = ""
            acumuladorTrama = acumuladorTrama + actualByte
        else:
            acumuladorTrama = acumuladorTrama + actualByte
        i = i + 2
    #En la etapa 1 se busca la longitud de la trama
    elif (etapa == 1):
        bandera = False
        actualByte1 = line[i : i + 2]
        actualByte2 = line[i + 2 : i + 4]
        j = i
        #Se comienzan a analizar los dos siguientes bytes por separado, buscando secuencias de escape en ellos
        #Si encuentra una secuencia de escape, se cambia al primer byte por el segundo y el segundo pasa a valer lo que su siguiente byte.
        if actualByte1 == "7E":
            j = i + 2
            bandera = True
        elif (actualByte1 == "7D" and actualByte2 == "7E"):
            actualByte1 = "7E"
            actualByte2 = line[i + 4 : i + 6]
            acumuladorTrama = acumuladorTrama + actualByte1
            secuenciaEscape = True
            cantSecuenciaEscape = cantSecuenciaEscape + 1
            j = i + 6
        else:
            acumuladorTrama = acumuladorTrama + actualByte1
            j = i + 2
        if (actualByte2 == "7D" and line[j : j + 2] == "7E"):
            actualByte2 = "7E"
            j = j + 2
            secuenciaEscape = True
            cantSecuenciaEscape = cantSecuenciaEscape + 1
            acumuladorTrama = acumuladorTrama + actualByte2
        elif (actualByte2 == "7E"):
            bandera = True
        else:
            acumuladorTrama = acumuladorTrama + actualByte2
            j = j + 2

        #Si en algún momento la bandera se vuelve True es porque se encontró un bit de bandera y por lo tanto la trama es incorrecta
        if (bandera == True):
            if secuenciaEscape == True:
                print("La trama", total - 1, "tiene secuencia de escape. Trama sin secuencia: ", acumuladorTrama)
                secuenciaEscape = False
            i = j - 2
            etapa = 0
        else:
            i = j
            etapa = 2
            actualByte = actualByte1 + actualByte2
            #Se obtiene la longitud de la trama
            decLength = int(actualByte, 16)
    #En la etapa 2 se va "contando" y sumando cada byte, para posteriormente verificar su longitud y el checksum correcto
    elif (etapa == 2):
        actualByte = line[i:i+2]
        i = i + 2
        #Si encuentra un 7E, un byte de bandera, significa que la longitud es incorrecta pues es menor de la mencionada
        if (actualByte == "7E"):
            if secuenciaEscape == True:
                print("La trama", total - 1, "tiene secuencia de escape. Trama sin secuencia: ", acumuladorTrama)
                secuenciaEscape = False
            incorrectas = incorrectas + 1
            print("La trama", total - 1, "tiene longitud incorrecta. Trama: ", acumuladorTrama)
            suma = 0
            etapa = 0
            i = i - 4
        #Se verifica que no se encuentre una bandera nueva en medio, esto se hace verificando que no haya secuencia de escape
        elif ((actualByte == "7D") and (line[i: i + 2] == "7E")):
                decLength = decLength - 1
                actualByte = "7E"
                i = i + 2
                suma = suma + int("7E", 16)
                secuenciaEscape = True
                cantSecuenciaEscape = cantSecuenciaEscape + 1
        else:
        #Se decrementa la longitud, encontrada en la etapa anterior, por cada byte
            decLength = decLength - 1
            #Se realiza la suma de los bytes, convirtiéndolos a enteros previamente
            suma = suma + int(actualByte, 16)
        #Si la longitud es 0, se pasa a la siguiente etapa, donde se verificará que la trama no sea más larga de lo que debería.
        acumuladorTrama = acumuladorTrama + actualByte
        if (decLength == 0):
            etapa = 3
            
    #En la etapa 3 se termina de verificar la longitud y se realiza la verificación de suma
    elif (etapa == 3):
        actualByte = line[i:i+2]
        flag = False
        #Se verifica que la trama termine en el byte actual, es decir, que la longitud sea correcta
        if (i == (len(line) - 3)):
            correctas = correctas + 1
            flag = True
        elif (actualByte == "7E"):
            etapa = 0
            i = i - 2
            flag = False
            incorrectas = incorrectas + 1
            actualByte = ""
        else:
            #Se verifica que no exista una secuencia de escape y en el caso de que exista se pasa al siguiente byte
            if (actualByte == "7D") and (line[i + 2: i + 4] == "7E"):
                actualByte = "7E"
                i = i + 2
                cantSecuenciaEscape = cantSecuenciaEscape + 1
                secuenciaEscape = True
            if (line[i + 2 : i + 4] == "7E"):
                correctas = correctas + 1
                flag = True
            else:
                incorrectas = incorrectas + 1
                longIncorrecta = True
        acumuladorTrama = acumuladorTrama + actualByte
        #En el caso de que la longitud sea correcta se procede con la verificación de suma
        if (flag == True):        
            if (checkSum(suma, actualByte) == True):
                correctasVerif = correctasVerif + 1
            else:
                incorrectasVerif = incorrectasVerif + 1
                print("La trama", total - 1, "tiene checksum incorrecto. Trama: ", acumuladorTrama)
            if secuenciaEscape == True:
                print("La trama", total - 1, "tiene secuencia de escape. Trama sin secuencia: ", acumuladorTrama)
                secuenciaEscape = False
        #Se vuelve a la etapa 0 para comenzar nuevamente el bucle
        etapa = 0
        i = i + 2
print("El número total de tramas recibidas es de: ", total)
print("De ellas, el número de tramas de longitud correctas es de: ", correctas, " y el número de longitud incorrectas es de: ", incorrectas)
print("Si tomamos en cuenta solo las tramas de longitud correctas, las que tuvieron la suma de verificación correcta fueron: ", correctasVerif, " y las que la tuvieron incorrecta fueron: ", incorrectasVerif)
print("La cantidad de secuencias de escape encontradas fueron de: ", cantSecuenciaEscape)
fileLine.close()