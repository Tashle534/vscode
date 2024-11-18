
#decide trade approvals , eligibility
traderOrigin = input(("Please enter planet of origin  :  ").lower())

def tradeEligibility(traderOrigin):
    if traderOrigin == "earth":
        print("Eligible")
    elif traderOrigin == "mars":
        TradeNum = int(input("Please enter number of successful trades  "))
        if TradeNum >= 10:
            tradeVal = str(input("Is your market value greater than 15 000 credits  \n True or False "))
            if tradeVal == "True" :
                print("Eligible, welcome to trading with us. ")
            else :
                print("Market value credits are not sufficient.")
        else:
            print("Number of successful trades is not sufficient.")
    elif traderOrigin == "jupiter":
        TradeEx =str(input(("What type of trading experience do you have: ","Expert","Medium","Novice : " )))
        if  TradeEx == "expert":
            resources =bool(input("Do you involve rare resources?  "))
            if resources == True:
                tradQuota = int(input("enter quota usage : "))
                try : 
                    tradQuota > 80 
                    print("Eligible")
                except ValueError:
                    print("Not eligible because Quota usage is too high")
            else: 
                print("Not eligible because resources do not involve rare resources.")
        else:
            print("Not allowed to trade because experience level is low") 
    else:
        print("Planet unknown")
tradeEligibility(traderOrigin)

##Calculation of taxes 

def taxCalculation(traderOrigin):
    traderOrigin = input("Enter planet of origin")
    if traderOrigin == "earth":
        taxRate = 0.05
        TradeEx =("Please enter experience level: 'novice','medium', 'expert'  ")
        if TradeEx == "novice":
            print("Tax Rate : ", taxRate += 0.02)
        elif TradeEx == "medium":
            print("Tax Rate : " taxRate )
        else:
            print("Tax rate : ", taxRate - 0.01)
    elif traderOrigin == "mars":
        taxRate = 0.08
        TradeEx =("Please enter experience level: 'novice','medium', 'expert'  ")
        if TradeEx == "novice":
            print("Tax Rate : ", taxRate += 0.02)
        elif TradeEx == "medium":
            print("Tax Rate : " taxRate )
        else:
            print("Tax rate : ", taxRate - 0.01)
            

