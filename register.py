



##Diccionario para los usuarios
usersData = {
    "usuario1": {
        "password": "1234",
        "phone": "1234567890",
        "email": "usuario1@mail.com",
        "id": 1
    }
}


books = {
    "1984": {
        "author": "George Orwell",
        "year": 1949,
        "available": True
    },
    "El Principito": {
        "author": "Antoine de Saint-Exupéry",
        "year": 1943,
        "available": True
    },
    "Don Quijote": {
        "author": "Miguel de Cervantes",
        "year": 1605,
        "available": True
    }
}

currentUser = None



def main_menu():
    while True: 
        print("\n--- Main Menú ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Registrar nuevo libro")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            createUser()
        elif opcion == "2":
            login()
        elif opcion == "3":
            borrow_book()
        elif opcion == "4":
            return_book()
        elif opcion == "5":
            register_new_book()
        elif opcion == "6":
            print("¡Gracias por usar la biblioteca!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")



##US1/create register

##users = [[],[]]

def createUser():
    global currentUser
    id = int(input("Ingrese su documento de identidad: "))
    
    if id in usersData:
        print("Esta id ya existe.")
    else:
        user_name = input("Ingrese su nombre: ")
        user_last_name = input("Ingrese su apellido: ")
        phone = input("Ingrese su telefono: ")
        user_email = input("Ingrese su correo electronico: ")
        user_password = input("Ingrese su contraseña: ")

        usersData[user_name] = {
            "last_name":user_last_name, 
            "password": user_password,
            "phone": phone,
            "email": user_email,
            "id": id
        }

        currentUser = user_name
        print(f"Usuario {user_name} registrado exitosamente!")

#login

def login():
    global currentUser
    print("Registrese para ingresar")

    user_name = input("Ingrese su usuario: ")
    
    if user_name in usersData:

        password = input("Ingrese su contraseña: ")

        if usersData[user_name]["password"] == password:
            currentUser = user_name
            print(f"Bienvenido {user_name}, has iniciado sesión correctamente.")
        else:
            print("Contraseña incorrecta. Intenta nuevamente.")
    else:
        print("El nombre de usuario no existe. Intenta nuevamente.")

##login()


##libros disponibles

def availableBooks():
    print("\n--- AVAILABLE BOOKS ---")
    for title, info in books.items():
        status = "Available" if info["available"] else "Not Available"
        print(f"{title} | Author: {info['author']} | Year: {info['year']} | Status: {status}")



# funcion prestar un libros
def borrow_book():
    if currentUser is None:
        print("El usuario debe estar registrado para poder prestar un libro")
        return

    availableBooks()
    book = input("Ingresa el libro que quieres prestar:  ")

    if book in books:
        if books[book]["available"]:
            books[book]["available"] = False
            if "borrowed_books" not in usersData[currentUser]:
                usersData[currentUser]["borrowed_books"] = []
                usersData[currentUser]["borrowed_books"].append(book)
            print(f"Haz prestado el libro '{book}'. Por favor devolverlo en 8 días.")
        else:
            print(f"'{book}' el ibro no esta disponible")
    else:
        print("Este libro no existe en el catálogo")

# Función para devolver un libro
def return_book():
    if currentUser is None:
        print("Debes registarte para devolver el libro")
        return

    borrowed_books = usersData[currentUser].get("borrowed_books", [])
    if not borrowed_books:
        print("No haz prestado libros")
        return

    print("\nTus libros prestados: ")
    for book in borrowed_books:
        print(f"- {book}")

    book = input("Ingresa el nombre del libro que deseas regresar")

    if book in borrowed_books:
        books[book]["available"] = True
        usersData[currentUser]["borrowed_books"].remove(book)
        print(f"Haz devuelto el libro'{book}'. Gracias")
    else:
        print("No haz prestado libros")


# Función para registrar un nuevo libro
def register_new_book():
    if currentUser is None:
        print("Debes iniciar sesion para agregar un nuevo libro")
        return

    title = input("Ingresa el titulo del nuevo libro: ")
    if title in books:
        print("Ese libro ya existe en la biblioteca")
        return

    author = input("Ingresa el nombre del autor: ")
    year = input("Ingresa el año de publicación: ")

    books[title] = {
        "author": author,
        "year": year,
        "available": True
    }

    print(f"El libro '{title}' se registro correctamente ")


# Iniciar el programa
main_menu()

