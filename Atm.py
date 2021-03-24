balance=5000000


class Atm:
    def __init__(self):
        print("Processing")
    def BankEnquiry(self):
        cardnumber=int(input("Enter card number\t"))
        print("Your Balance is: ",balance)

    def CashWithdrawl(self):
        withdraw=int(input("Enter the amount you would like to withdraw\t"))
        pin=int(input("Enter your pin"))
        print("Processing the amount please be patient")
        print("You can now remove your card")
        print("Your current accout balance is: ",balance-withdraw)

customer=Atm()
def Activity():
    print("Hello hope you are having a good day")
    print("Please choose you activity \n Press 1 for Balance Enquiry amd 2 for Cash Withdrawl")
    act=int(input("Please enter the number"))

    if(act==1):
        customer.BankEnquiry()
    elif(act==2):
        customer.CashWithdrawl()
    else:
        print("Please choose a number from 1 and 2 only")

Activity()
    