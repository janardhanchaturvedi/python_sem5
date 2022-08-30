print("Range")

arr=[]
for i in range(1500,2700):
    if(i%7==0) and (i%5==0):
        arr.append(i)
        
print(arr)