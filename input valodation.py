special_character = ["!","£","@","$", "%","*", "#","~","¬","&"]
username = input ("Username : ")
username_has_specialC = False
for letter in username:
    if letter in special_character:
        username_has_specialC = True
        break
if username_has_specialC:
    print("Not allowed")
else:
    print("Username is valid")