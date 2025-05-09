import json, os

data = {}
fileName = "db.json"
if os.path.exists(fileName) :
    with open(fileName,"r") as f:
        data = json.load(f)
else:
    with open(fileName,"w") as f:
        pass
    data["books"] = []
    data["users"] = []


def register():
    username = input("Enter your username: ")
    while username == "":
        print("it should not be empty")
        username = input("Enter your username: ")
    password = input("Enter your password: ")
    while len(password) < 8 :
        print("your password is too short")
        password = input("Enter your password: ")

    user = {
        "username" : username,
        "password" : password
    }
    data["users"].append(user)

def logIn():
    username = input("Enter your username: ")
    while username == "":
        print("it should not be empty")
        username = input("Enter your username: ")
    password = input("Enter your password: ")
    found = False
    for user in data["users"]:
        if username == user["username"]:
            if password == user["password"]:
                found = True
                print("Logged in successfully")
            else:
                print("Invalid Password")
                logIn()
    if found == False:
        print("Credintials are not correct")
        logIn()

def addBook():
    title = input("Enter the book title: ")
    while title == "":
        print("it should not be empty")
        title = input("Enter the book title: ")
    description = input("Enter the book description: ")
    while description == "":
        print("it should not be empty")
        description = input("Enter the book description: ")
    category = input("Enter the book category(science, sport): ")
    while category not in ["science", "sport"] :
        print("this isn't right category")
        category = input("Enter the book category(science, sport): ")
    author = input("Enter the book author: ")
    while author == "":
        print("it should not be empty")
        author = input("Enter the book author: ")
    price = float(input("Enter the book price: "))
    while price == "":
        print("it should not be empty")
        price = float(input("Enter the book price: "))
    isBorrowed = False
    book = {
        "title" : title,
        "description" : description,
        "category" : category,
        "author" : author,
        "price" : price,
        "isBorrowed" : isBorrowed
    }
    data["books"].append(book)
    print("Book added successfully")

def displayBooks():
    cnt = 1
    for book in data["books"] :
        print(f"{cnt}- book : {book["title"]}")
        cnt+=1

def deleteBook():
    displayBooks()
    choice = int(input("choose the book you want to delete: "))
    while choice < 1 or choice > len(data["books"]):
        print("Invalid choice")
        choice = (input("choose the book you want to delete: "))
    del data["books"][choice-1]


def updateBook():
    displayBooks()
    choice = int(input("choose the book you want to update: "))
    while choice < 1 or choice > len(data["books"]):
        print("Invalid choice")
        choice = (input("choose the book you want to update: "))
    title = input("Enter the book title: ")
    while title == "":
        print("it should not be empty")
        title = input("Enter the book title: ")
    description = input("Enter the book description: ")
    while description == "":
        print("it should not be empty")
        description = input("Enter the book description: ")
    category = input("Enter the book category(science, sport): ")
    while category not in ["science", "sport"] :
        print("this isn't right category")
        category = input("Enter the book category(science, sport): ")
    author = input("Enter the book author: ")
    while author == "":
        print("it should not be empty")
        author = input("Enter the book author: ")
    price = float(input("Enter the book price: "))
    while price == "":
        print("it should not be empty")
        price = float(input("Enter the book price: "))
    isBorrowed = False
    book = {
        "title" : title,
        "description" : description,
        "category" : category,
        "author" : author,
        "price" : price,
        "isBorrowed" : isBorrowed
    }
    data["books"][choice-1] = book

def borrowBook():
    displayBooks()
    choice = int(input("choose the book you want to borrow: "))
    while choice < 1 or choice > len(data["books"]):
        print("Invalid choice")
        choice = (input("choose the book you want to borrow: "))
    while data["books"][choice-1]["isBorrowed"] == True:
        print("The book is already borrowed")
        choice = int(input("choose the book you want to borrow: "))
        while choice < 1 or choice > len(data["books"]):
            print("Invalid choice")
            choice = (input("choose the book you want to borrow: "))
    data["books"][choice-1]["isBorrowed"] = True

def reutrnBook():
    displayBooks()
    choice = int(input("choose the book you want to return: "))
    while choice < 1 or choice > len(data["books"]):
        print("Invalid choice")
        choice = int(input("choose the book you want to borrow: "))
    
    while data["books"][choice-1]["isBorrowed"] == False:
        print("The book is already not borrowed")
        choice = int(input("choose the book you want to return: "))
        while choice < 1 or choice > len(data["books"]):
            print("Invalid choice")
            choice = (input("choose the book you want to return: "))
    data["books"][choice-1]["isBorrowed"] = False

def mainMenu():
    print("Ahlan ya user ya habibi")
    choice = input("Login or signup ?")
    while choice.lower() not in ["login","signup"]:
        print("Invalid choice")
        choice = input("Login or signup ?")
    if choice == "login":
        print("=====Log in======")
        logIn()
    else:
        register()
        print("=====Log in======")
        logIn()
    print()
    print("=====================")
    print()
    print("======== main menu ========")
    print("1 - Add book")
    print("2 - Display books")
    print("3 - Delete book")
    print("4 - Update book")
    print("5 - Borrow book")
    print("6 - Return book")
    print("7 - Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addBook()
        elif choice == 2:
            displayBooks()
        elif choice == 3:
            deleteBook()
        elif choice == 4:
            updateBook()
        elif choice == 5:
            borrowBook()
        elif choice == 6:
            reutrnBook()
        elif choice == 7:
            break

mainMenu()

with open(fileName,"w") as f:
    json.dump(data,f, indent=4)


