a=[]
b=input("Enter number of elements of list:")
c=int(b)
for i in range(c):
    i=int(input("enter list element:"))
    a.append(i)
print("list=",a)
b=[]
for i in a:
    if i >= 0:
        b.append(i)
print(b)
