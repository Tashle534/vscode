#things i need to imprt so i can use later
import re
from datetime import datetime
#program of of an authenticator

#pre-defined variables 
stored_email = "tashy@something.com"
stored_userName = "Ashleigh123"
login_password ="123456789ash?"
special_char = [":",";","?","/",">","<","&","*","-",'_',"+","%","/","~","!","£","$","^"]
#declaring variables so i dont forget which ones too add

#prompting for creation or login
user_Response = input(" Would you like to Create an account or Login to your acoount? ")
#conditons for what to do when input is given
if user_Response == " Create " :
    #info for creating the account
    username =input ("Please enter your full name")
    user_surname = input ("Please enter your surname ")
    #email validation check 
    
    #validating the email address input
    while True:
        User_email = input("Please enter a valid email address e.g something@email.com")
        if "@" in User_email :
            print("Welcome")
        User_email =input("Pleas enter a  valid email address")
    #validating date of birth input
    while True:
        User_DOB= input("Please enter Date Of Birth")
        
        User_password = ("Please create a valid password with at least 1 special character \n ,and a minimum of 8 characters long ")
    
    if len(User_password) < 8 :
        print ("Password is too short")
        User_password =input("Please enter a valid password ")
    else:
        if special_char in User_password :
            print("Password is strong")
        else:
            print("password is weak")
            User_password = input("please enter valid input")
elif user_Response == "Login" :
    user_Response =input ("Please enter your email address")
    if user_Response == stored_email:
        print("Welcome", stored_email)
        user_Response = input("Please enter login Password ")
        '''
        if user_Response == login_password:
        else:
            print("incorect password, please go back to start")
        '''
    else:
        print("Email does not exist, please return to start.")
else:
    print ("Please pick a valid option ")
    