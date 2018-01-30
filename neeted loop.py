# a loop in  a loop is called nested loop
# whether it is a while in for in loop or for in while loop
# here we are writing a simple logic for atm withdrawal
print("welcome To Ravi's Bank ATM")
balance = 67.51
chances = 3
response = ('y')
print("please Enter to pin to avail services")
while chances >0:
 pin = int(input("enter PIN:"))
 if pin == (1234) :
    print("welcome")
    while response not in ('n','N','no','NO'):
        print("press 1 for balance \n")
        print("press 2 for withdrawal \n")
        print("press 3 for deposit \n")
        option = int(input("enetr option number"))
        if option == 1:
            print("Balance in your account is: ",balance,'\n')
            response = input("would like to go back")
            if response in ('n','N','NO','no'):
                print("thank you")
                break
        elif option == 2:
            amount = float(input("enter amoun to withdraw"))
            balance = balance - amount
            print('you have successfully withdrawan', amount,'/n')
            print('your current balance', balance,'/n')
            break


 elif pin != (1234):
    print("you have enter in correct pin")
    chances = chances -1
    if chances == 0:
        print("\n sorry you card blocked for the day")









