print("WELCOME TO DISTRICT LIBRARY")
print("-"*28)
while True:
    username = input("Enter Username: ")
    if username == "kuldeep":
        password = input("Enter Password: ")
        if password == "1234":
            print("-"*30)
            print("Login Successfull")
            print()
            break
        else:
            print("Enter correct password")
    else:
        print("Please Enter Correct Username")
        
books = {"Math" : 10, "Science" : 10, "Hindi" : 10, "English" : 10}
borrowed_books = {}

while True:        
    print("""
             Press 1 to Show Books
             Press 2 to Add New Books
             Press 3 to Borrow Book
             Press 4 to View Borrowed Books
             Press 5 to Return Book 
             Press 6 to Exit
             """)
    choice = input("Enter Your Choice: ")
    print()
    if choice == "1":
        print("-"*40)
        for i,j in books.items():
            print(i, "=", j)
        print("-"*40)
        
    
    elif choice == "2":
        book_name = input("Enter book name: ").title()
        quantity = int(input("How much books you wants to add: "))
        if book_name in books:
            books[book_name] += quantity
            print("-"*40)
            print("Books Added Successfull")
            print("-"*40)
        if book_name not in books:
            books[book_name] = quantity
            print("-"*40)
            print("New Books Added Successfull")
            print("-"*40)
    
            
    elif choice == "3":
        name = input("Enter Your Name: ").upper()
        if name in borrowed_books:
            print("-"*40)
            print("You have already borrowed book")
            print("-"*40)
            continue
            
    
        book_name = input("Enter book name: ").title()
        if book_name not in books or books[book_name] == 0:
            print("-"*40)
            print("Sorry this book is not available")
            print("-"*40)
        else:
            books[book_name] = books[book_name] -1
            borrowed_books[name] = book_name
            print(borrowed_books)
            print("-"*40)
            print(name, "Book borrowed successfully")
            print("-"*40)
            
            
    elif choice == "4":     
        print("-"*40)
        print("          Borrowed Books")
        for i,j in borrowed_books.items():
            print(i, "-",j)
        print("-"*40)
        
        
    elif choice == "5":
        print("-"*40)
        print("          Borrowed Books")
        for i,j in borrowed_books.items():
            print(i, "-",j)
        print("-"*40)
        print()
        name = input("Enter your name: ").upper()
        print()
        if name not in borrowed_books:
            print("-"*40)
            print(name, "You have not borrowed any book")
            print("-"*40)
            continue
            
            
        book_name = input("Enter book name: ").title()
        if book_name not in borrowed_books[name]:
            print("-"*40)
            print(name, "You have not borrowed this book")
            print("-"*40)
        
        else:
            books[book_name] = books[book_name]+1
            del borrowed_books[name]
            print("-"*40)
            print(name,"Book Returned")
            print("-"*40)
            
            
    elif choice == "6":
        print("Thank You and Visit Again")
        break
        
    else:
        print("-"*40)
        print("Please choose a correct option")
        print("-"*40)
        
