# Mini Library Management System

library = {}      # Stores books and quantity
borrowed = {}     # Stores borrowed books


# 1. Add Book
def add_book():
    name = input("Enter book name: ")
    qty = int(input("Enter quantity: "))
    
    if name in library:
        library[name] += qty
    else:
        library[name] = qty
        
    print("Book added successfully!\n")


# 2. View Books
def view_books():
    if not library:
        print("Library is empty!\n")
    else:
        print("Available Books:")
        for book, qty in library.items():
            print(f"{book} - {qty} copies")
    print()


# 3. Borrow Book
def borrow_book():
    name = input("Enter book name to borrow: ")
    
    if name in library and library[name] > 0:
        library[name] -= 1
        
        if name in borrowed:
            borrowed[name] += 1
        else:
            borrowed[name] = 1
            
        print("Book borrowed successfully!\n")
    else:
        print("Book not available!\n")


# 4. Return Book
def return_book():
    name = input("Enter book name to return: ")
    
    if name in borrowed and borrowed[name] > 0:
        borrowed[name] -= 1
        library[name] += 1
        print("Book returned successfully!\n")
    else:
        print("This book was not borrowed!\n")


# 5. Search Book
def search_book():
    name = input("Enter book name to search: ")
    
    if name in library:
        print(f"{name} is available with {library[name]} copies\n")
    else:
        print("Book not found!\n")


# 6. Main Menu
def menu():
    while True:
        print("===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice!\n")


# Run the program
menu()
