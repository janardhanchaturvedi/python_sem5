print("Factorial Program")

factorial=1
num= int(input("Enter any number : "))

if num<0:
    print("Factorial of number doesnt Exists")
elif num==0:
    print("Factorial of number is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of ",num, "is ",factorial)
    