#making functions so that its easier for me to handle

# Initialize an empty list to store books
#made a status list for easy access
books = []
book_index = 0
def book_details():
    #Get the number of books to add1
    
    num_books = int(input("How many books would you like to add? "))
    #Loop to get book details from the user
    for i in range(num_books):
        print(f"\nEnter details for book {i+1}:")
        
        title = input("Title: ")
        author = input("Author: ")
        status = input ("Please enter book status : available or reserved ").lower()
        
        # Create a dictionary for the book and add it to the list
        book = {
            "title": title,
            "author": author,
            "status": status
        }
        books.append(book)
        print(*books, sep="\n")
    
def book_return():
    book_index = int(input("which book do you want to return(book number/index)"))
    if books[book_index].get("status") == "reserved":
        books[book_index].update({"status":"available"})
    print("Book returned, Book now available for borrowing. 📖 ")
    

def book_viewing() :
    print("Welcome to the book list")
    print ("The list of books is \n", books)
    
def book_reserve():
    book_index = int(input("which book do you want to reserve(book number/index)"))
    if book_index >= len(books) or book_index < 0:
        print("Invalid book index!!!")
    
    if books[book_index].get("status") == "reserved":
        print("Sorry book is already reserved. ")
    elif books[book_index].get("status") == "available":
        books[book_index].update({"status" : "reserved"})
        print("book is now reserved")
#making a way for users to exit program when they want to exit

#main logic
book_details()

user_exit = False

user_Response = input("What would you like to do: 'Reserve a book','Return a book','View Book List' or 'Exit' \n write 'return','reserve', 'view' or 'exit' ").lower()
print("  ") 
while not user_exit:

    if user_Response == "exit":
        user_exit = True
        print("Good Bye!,Hope to see you again soon 👋")
        breakpoint   #stop the program from continuing if they want to exit
    if user_Response == "reserve":
        print("Welcome to book reserve")
        book_reserve()
    elif user_Response == "return":
        book_return()
    elif user_Response == "view":
        book_viewing()
    else:
        print("Invalid input, please choose 'reserve','return','view',or 'exit'")