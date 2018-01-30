# for loop is used when we know iterations we need
# sample programme to print a factorial of number

num = int(input("enter a  number: "))
factorial = 1

if num < 0:
    print ("num value must be a positive")
elif num == 0:
    print("factorial=1")
else:
    for i in range(1,num+1):
        factorial = factorial *i

print(factorial)