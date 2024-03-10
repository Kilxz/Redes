using System;
using System.ComponentModel.DataAnnotations;
using System.IO;
namespace CheckTramasRedes;
/* Para realizar el trabajo se tomó un enfoque que utiliza etapas, es decir, la fase de "búsqueda" de la bandera se da en la etapa 0, luego,
en la etapa 1 se verifica la longitud y se pasa a la etapa 2, en ella se va "contando", sumando y se va verificando que no aparezca una nueva bandera 7E en medio, por último, en la
etapa 3 se verifica el checksum de la trama utilizando la información de la anterior etapa. 

Se realizó utilizando este enfoque para lograr una complejidad temporal de O(n) */
class CheckTramasRedes {
    static void Main() {
        string line;
        try {
            //Se abre el archivo
            StreamReader fileLine = new StreamReader("Tramas_802-15-4.log");
            line = fileLine.ReadLine();
            
            //Se declaran variables y se inicializan
            int i = 0;
            int etapa = 0;
            int incorrectas = 0;
            int correctas = 0;
            int correctasVerif = 0;
            int total = 0;
            int incorrectasVerif = 0;
            int suma = 0;
            int cantSecuenciaEscape = 0;
            string actualByte;
            bool flag = false;
            int decLength = 0;
            //Loop de las etapas explicadas anteriormente
            while (i < line.Length) {
                if (etapa == 0) {
                    suma = 0;
                    actualByte = line.Substring(i, 2);
                    //Se busca la bandera "7E"
                    if ((i == 0) && (actualByte == "7E")) {
                        etapa = 1;
                        total = total + 1;
                    //Se verifica que la bandera no tenga una secuencia de escape
                    } else if ((actualByte == "7E") && (line.Substring(i-2, 2) != "7D")) {
                        etapa = 1;
                        total = total + 1;
                    }  
                    i = i + 2;
                } else if (etapa == 1) {
                    actualByte = line.Substring(i, 4);
                    //Se obtiene la longitud de la trama
                    decLength = Convert.ToInt32(actualByte, 16);
                    etapa = 2;
                    i = i + 4;
                } else if (etapa == 2) {
                    actualByte = line.Substring(i, 2);
                    //Se realiza la suma de los bytes, convirtiéndolos a enteros previamente
                    suma = suma + Convert.ToInt32(actualByte, 16);
                    //Se verifica que no se encuentre una bandera nueva en medio y que, en el caso de encontrarla, no se encuentre una secuencia de escape
                    if ((actualByte == "7E") && (line.Substring(i-2,2) != "7D")) {
                        incorrectas = incorrectas + 1;
                        suma = 0;
                        etapa = 1;
                    } else {
                        if ((actualByte == "7E") && (line.Substring(i-2,2) == "7D")) {
                            cantSecuenciaEscape = cantSecuenciaEscape + 1;
                        }
                        //Se decrementa la longitud, encontrada en la etapa anterior, por cada byte
                        decLength = decLength - 1;
                        //Si la longitud es 0, se pasa a la siguiente etapa, donde se verificará que la trama no sea más larga de lo que debería.
                        if (decLength == 0) {
                            etapa = 3;
                        }
                    }
                    i = i + 2;
                } else if (etapa == 3) {
                    actualByte = line.Substring(i, 2);
                    flag = false;
                    //Se verifica que la trama termine en el byte actual, es decir, que la longitud sea correcta
                    if (i == (line.Length - 2)) {
                        correctas = correctas + 1;
                        flag = true;
                    } else if (line.Substring(i+2, 2) == "7E") {
                        correctas = correctas + 1;
                        flag = true;
                    } else {
                        incorrectas = incorrectas + 1;
                    }
                    //En el caso de que la longitud sea correcta se procede con la verificación de suma
                    if (flag == true) {
                        if (checkSum(suma, actualByte) == true) {
                            correctasVerif = correctasVerif + 1;
                        } else {
                            incorrectasVerif = incorrectasVerif + 1;
                        }
                    }
                    //Se vuelve a la etapa 0 para comenzar nuevamente el bucle
                    etapa = 0;
                    i = i + 2; 
                }
                }
                Console.WriteLine("El número total de tramas recibidas es de: " + total);
                Console.WriteLine("De ellas, el número de tramas de longitud correctas es de: " + correctas + " y el número de longitud incorrectas es de: " + incorrectas);
                Console.WriteLine("Si tomamos en cuenta solo las tramas de longitud correctas, las que tuvieron la suma de verificación correcta fueron: " + correctasVerif + " y las que la tuvieron incorrecta fueron: " + incorrectasVerif);
                Console.WriteLine("La cantidad de secuencias de escape encontradas fueron de: " + cantSecuenciaEscape);

            } catch {
                Console.WriteLine("Error en la lectura del archivo, por favor, reintente");
            }
    }
    //Verifica la suma del checksum
    static bool checkSum(int suma, string verificador) {
        int sumaDec = 255 - (suma & Convert.ToInt32("FF", 16));
        return sumaDec == Convert.ToInt32(verificador, 16);
    }

}