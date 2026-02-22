def admin_validation():
    admin_name ="Ashleigh Chiriro"
    admin_pass = "1233456"
    admin_resp=""
    valid = False
    while valid:
        
        user_resp = input("Are you a user or an admin? \n Please type 'admin' or 'user' .")
        if user_resp == "admin":
            admin = input("please enter admin name")
            if admin == admin_name:
                print("welcome",admin_name)
                admin= input("please enter admin password ")
                if admin_pass== admin:
                    admin_resp = input("what would you like to do?\n add to the book list,remove items from book list,or updating book list \n pick 1,2 or 3 .")
                    if admin_resp == "1":
                        num_books= input("how many books do you want to add?")
                        for i in range(num_books):
                            Title = input("Title:   ")
                            Author = input ("Author : ")
                            Stats = input("Status : ")
                            book.update({"title":"Title","author":"Author","status":"Stats"})
                            books.append(book)
                            library = open("libraryFiles.txt","wt")
                            print(library.write(books))
                            library.close()
                        
                    elif admin_resp == "2":
                        indx = int(input("What is the  index of the book you wish to delete from the list ."))
                        if indx in book_index:
                            book.pop(indx)
                            books.append(book)
                            library = open("libraryFiles.txt","wt")
                            print(library.write(books))
                            library.close()
                        else:
                            print("Index out of range")
                    elif admin_resp == "3":
                        books.append(book)
                        library = open("libraryFiles.txt","rt")
                        print(library.read())
                        library.close()
                    else:
                        print("invalid response")
                else:
                    print("invalid password")
            else:
                ("invalid admin name")
        else:
            main()
    

#making functions so that its easier for me to handle
global num_books
global status
global book
global books
# Initialize an empty list to store books
#made a status list for easy access
def book_details():
    #Get the number of books to add1
    books = [] # type: ignore
    book_index = 0 
    num_books = 0
    num_books = int(input("How many books would you like to add? "))
    #Loop to get book details from the user
    library = open("libraryFiles.txt","wt")
    for i in range(num_books):
        print(f"\nEnter details for book {i+1}:")
        title = input("Title: ")
        author = input("Author: ")
        status = input ("Please enter book status : available or reserved ").lower()
        
        # Create a dictionary for the book and add it to the list
        book =dict({"title": title,"author": author,"status": status})
        
        
        books.append(book)
        print(*books, sep="\n")
        
    for key,value in book.items():
        library.write(f"{key}:{value},\n")
    library.close()
    
    library = open("libraryFiles.txt","rt")
    print(library.read())
    library.close()
    
    library = open("libraryFiles.txt","rt")
    print(library.read())
    library.close()
    
    
def book_return():
    book_index = int(input("which book do you want to return(book number/index)"))
    library = open("libraryFiles.txt","wt")
    if books[book_index].get("status") == "reserved":
        books[book_index].update({"status":"available"})
    print("Book returned, Book now available for borrowing. 📖 ")
    for BookR in books:
        library.write(f"{books}:{status}\n") # type: ignore 
    library.close()
    library = open("libraryFiles.txt","rt")
    print(library.read())
    library.close()
    
def book_viewing() :
    print("Welcome to the book list")
    print ("The list of books is \n", books)
    library =open("libraryFiles",'wt')
    for indx,book in enumerate(books):
        library.write(f"the library list is :{indx}:{books} ""\n")
    library.close()
    
    library = open("libraryFiles.txt","rt")
    print(library.read())
    library.close()
    
def book_reserve():
    global book_index
    book_index = int(input("which book do you want to reserve(book number/index)"))
    if 0 <= book_index < len(books):
        if books[book_index].get("status") == "available":
            books[book_index].update({"status" : "reserved"})
            print("book is now reserved")
        else:
            print("book is already reserved.")
    library = open("libraryFile.txt","wt")
    for book_index in books:
        library.write(f"{book_index}:{status}\n")
    library.close()
    
    library = open("libraryFiles.txt","rt")
    print(library.read())
    library.close()
#making a way for users to exit program when they want to exit
def main():
    #main logic
    book_details()
    user_exit = False
    while not user_exit:
        user_Response = input("What would you like to do: 'Reserve a book','Return a book','View Book List' or 'Exit' \n write 'return','reserve', 'view' or 'exit' ").lower()
        print("  ") 
        if user_Response == "exit":
            user_exit = True
            print("Good Bye!,Hope to see you again soon 👋") #stop the program from continuing if they want to exit
        if user_Response == "reserve":
            book_reserve()
        elif user_Response == "return":
            book_return()
        elif user_Response == "view":
            book_viewing()
            break
        else:
            print("Invalid input, please choose 'reserve','return','view',or 'exit'")
            
