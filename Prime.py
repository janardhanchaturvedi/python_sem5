num1= int(input("Enter the First range"))
num2= int(input("Enter the Second Range"))

prime=[]
for i in range(num1,num2+1):
    flag = True
    for x in range(2,i):
        if i%x==0:
            flag=False
            break
    
    if flag:
        prime.append(i)
print(prime)