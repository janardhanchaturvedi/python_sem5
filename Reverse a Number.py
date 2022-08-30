def Revnum(i):
    sum=0
    while(i):
        c=i%10
        print(c)
        i//=10
    return sum

i = int(input("Enter the Number "))
print("Reversed Number is ",Revnum(i))