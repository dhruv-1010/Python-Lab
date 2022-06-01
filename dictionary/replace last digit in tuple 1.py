#sample input---->
#[(1, 2), (1, 3)]
# enter the number to replace-->100
#sample output------>
#[(1, 100), (1, 100)]
a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of columns:"))
lst=[]
el=int(input("Enter the number that you want to replace:"))
for i in range(a):
    tpl=()
    for j in range(b):
        x=int(input("Enter the element [{0}][{1}]".format(i,j)))
        if(j==(b-1)):
           x=el
        tpl+=x,
    lst.append(tpl)
print(lst)


#second method
print("second method:")
lst=[(1, 2), (1, 3),(2,4)]
lst1=[]
for i in lst:
    x=i[:-1]+(100,)
    lst1.append(x)
print(lst1)


