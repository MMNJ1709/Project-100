class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print("Your balance is 50,000")
    def withdrawl(self,amount):
        newAmount=50000-amount
        print("You have withdrawn amount "+str(amount)+". Your remaining balance is "+str(newAmount))

def main():
    card_Number=input("Insert your card number: ")
    pin_Number=input("Insert a pin number: ")
    user=Atm(card_Number,pin_Number)
    print("Choose your activity")
    print("1.balance enquiry 2.withdrawl")
    activity=int(input("Enter activity number: "))
    if(activity==1):
        user.check_balance()
    elif(activity==2):
        amount=int(input("Enter the amount: "))
        user.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__=="__main__":
    main()

