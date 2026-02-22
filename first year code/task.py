#task about driving
def ages():
    username = input("Please enter your name")
    age = int(input("Enter your age").strip())
    age_valid = True
    
    if  age <= 18 :
        return True
    return False

