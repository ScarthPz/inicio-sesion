import os
os.stem("cls")

usuarios = []

while True:
    print("""
    1. Inicio sesión
    2. Registrar usuario
    3. Eliminar usuario
    4. Salir
    """)
    opc = int(input("Ingrese opción: "))

    if opc == 1:
        pass
    elif opc == 2:
        print("REGISTRAR USUARIO")
        while True:
           user = input("Ingrese nombre de usuario: ")
           if len(user) > 3 and user.isalpha:
               print("usuario registrado!")
               break
           else:
               print("ERROR! vuelva a ingresar nombre de usuario")

        while True:
            contra = input("Ingrese contraseña: ")
            if contra in usuarios:
                print("contraseña ya existente!")
                continue
            else:
                break
        
        usuarios ={
            "user": user,
            "contra": contra
        }


    elif opc == 3:
        pass
    else:
        break