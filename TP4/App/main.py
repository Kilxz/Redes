import chatLanUDP
import chatLanTCP

def menu():
    print("============= MENU =============")
    print("1. Chat LAN UDP")
    print("2. Chat LAN TCP")
    print("3. Salir")
    print("=================================")
    option = int(input("Elija una opción: "))
    return option

if __name__ == "__main__":
    option = menu()
    if option == 1:
        chatLanUDP.initialize()
    elif option == 2:
        chatLanTCP.initialize()
    else:
        print("Saliendo...")