


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
createUser()

print(users)

