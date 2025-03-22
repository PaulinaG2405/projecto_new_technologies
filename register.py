


##US1/create register

users = [[],[]]

def createUser():
    id = int(input("Ingrese su documento de identidad"))
    user = []
    user.append(id)
    user_name = input("Ingrese su nombre")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido")
    user.append(user_last_name)
    phone = input("Ingrese su telefono")
    user.append(phone)
    user_email = input("Ingrese su correo electronico")
    user.append(user_email)
    user_password = input("Ingrese su contraseña")
    user.append(user_password)
    users.append(user)

createUser()
createUser()

print(users)







##Diccionario para los usuarios
usersData = {
    "usuario1": "1234" 
}

def login():
    print("Registrese para ingresar")

    #Pedir el nombre de usuario
    User = input("Ingrese su usuario: ")
    
    #Verificar si existe ese usuario
    if User in usersData:
        #Pedir la contraseña
        password = input("Ingrese su contraseña: ")
        #Verificar si es correcta
        if usersData[User] == password:
            print(f"Bienvenido {User}, has iniciado sesión correctamente.")
        else:
            print("Contraseña incorrecta. Intenta nuevamente.")
    else:
        print("El nombre de usuario no existe. Intenta nuevamente.")

login()
    

