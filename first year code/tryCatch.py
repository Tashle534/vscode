
try:
    file = open("tryCatch.txt","xt")
    
    file.write("Hello world!")
    
    file.close()
    
except FileExistsError:
    print("File already exists")
    