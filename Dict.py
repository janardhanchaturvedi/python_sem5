pen = '+'
pin = ['j','A','N','A','R','D','H','A','N']
print("Joining")
print(pen.join(pin))
c =  pen.join(pin)
print("String")
print(c.split('+'))
people = {'Karan':{'birthday':'Aug 22'},'Niraj':{'birthday':'Oct 1'},'Adarsh':{'birthday':'Mar 17'},'Moksh':{'birthday':'July 14'}}
labels = {'birthday':'birth date'}
name = input("Name : ")
if name in people :
    request = input('birthday(b)?')
    if request == 'b':
        key = 'birthday'
        print("%s's %s is %s."%(name,labels[key],people[name][key]))
    else :
        print("Invalid Input")
else :
    print("User Doesnt Exits")