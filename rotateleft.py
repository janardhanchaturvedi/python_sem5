def rotateleft(lis,n):
    outputar=[]
    for i in range(n,len(lis)):
        outputar.append(arr[i])
        
    for i in range(0,n):
        outputar.append(arr[i])
        
    return outputar

rotateby=1
arr=[2,8,0,9,8]
print(rotateleft(arr,rotateby))