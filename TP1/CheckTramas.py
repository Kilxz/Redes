""" Para realizar el trabajo se tomó un enfoque que utiliza etapas, es decir, la fase de "búsqueda" de la bandera se da en la etapa 0, luego,
en la etapa 1 se verifica la longitud y se pasa a la etapa 2, en ella se va "contando", sumando y se va verificando que no aparezca una nueva bandera 7E en medio, por último, en la
etapa 3 se verifica el checksum de la trama utilizando la información de la anterior etapa. 

Se realizó utilizando este enfoque para lograr una complejidad temporal de O(n) """

#Verifica la suma del checksum
def checkSum(suma, verificador):
    sumaDec = 255 - (suma & int("FF", 16))
    return sumaDec == int(verificador, 16)

try:
    #Se abre el archivo
    fileLine = open("Tramas_802-15-4.log", "r")
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

    #Loop de las etapas explicadas anteriormente
    while (i < len(line)):
        if (etapa == 0):
            suma = 0
            actualByte = line[i:i+2]
            #Se busca la bandera "7E"
            if ((i == 0) and (actualByte == "7E")):
                etapa = 1
                total = total + 1
            #Se verifica que la bandera no tenga una secuencia de escape
            elif ((actualByte == "7E") and (line[i-2 : i] != "7D")):
                etapa = 1
                total = total + 1
            i = i + 2
        elif (etapa == 1):
            actualByte = line[i: i+4]
            #Se obtiene la longitud de la trama
            decLength = int(actualByte, 16)
            etapa = 2
            i = i + 4
        elif (etapa == 2):
            actualByte = line[i:i+2]
            #Se realiza la suma de los bytes, convirtiéndolos a enteros previamente
            suma = suma + int(actualByte, 16)
            #Se verifica que no se encuentre una bandera nueva en medio y que, en el caso de encontrarla, no se encuentre una secuencia de escape
            if ((actualByte == "7E") and (line[i-2:i] != "7D")):
                incorrectas = incorrectas + 1
                suma = 0
                etapa = 1
            else:
                if ((actualByte == "7E") and (line[i-2:i] == "7D")):
                    decLength = decLength + 1
                    suma = suma - int("7D", 16)
                    cantSecuenciaEscape = cantSecuenciaEscape + 1
                #Se decrementa la longitud, encontrada en la etapa anterior, por cada byte
                decLength = decLength - 1
                #Si la longitud es 0, se pasa a la siguiente etapa, donde se verificará que la trama no sea más larga de lo que debería.
                if (decLength == 0):
                    etapa = 3
            i = i + 2
        elif (etapa == 3):
            actualByte = line[i:i+2]
            flag = False

            #Se verifica que la trama termine en el byte actual, es decir, que la longitud sea correcta
            if (i == (len(line) - 2)):
                correctas = correctas + 1
                flag = True
            elif (line[i + 2 : i + 4] == "7E"):
                correctas = correctas + 1
                flag = True
            else:
                incorrectas = incorrectas + 1

            #En el caso de que la longitud sea correcta se procede con la verificación de suma
            if (flag == True):
                if (checkSum(suma, actualByte) == True):
                    correctasVerif = correctasVerif + 1
                else:
                    incorrectasVerif = incorrectasVerif + 1

            #Se vuelve a la etapa 0 para comenzar nuevamente el bucle
            etapa = 0
            i = i + 2
    print("El número total de tramas recibidas es de: ", total)
    print("De ellas, el número de tramas de longitud correctas es de: ", correctas, " y el número de longitud incorrectas es de: ", incorrectas)
    print("Si tomamos en cuenta solo las tramas de longitud correctas, las que tuvieron la suma de verificación correcta fueron: ", correctasVerif, " y las que la tuvieron incorrecta fueron: ", incorrectasVerif)
    print("La cantidad de secuencias de escape encontradas fueron de: ", cantSecuenciaEscape)
    fileLine.close()
except Exception as e:
    print("Ocurrió un error al abrir el archivo. Reintente")
