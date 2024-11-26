filename = input("Upload a file: ")
file_format =  filename.split(".")[-1]
if file_format == "py":
    print("Accepted")
else:
    print("Denied")