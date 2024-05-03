import chatLan

def menu():
    print("============= MENU =============")
    print("1. ChatLAN")
    print("2. Otro")
    print("3. Salir")
    print("=================================")
    option = int(input("Elija una opcion: "))
    return option

if __name__ == "__main__":
    
    if menu() == 1:
        chatLan.initialize()
    else:
        print("Saliendo...")