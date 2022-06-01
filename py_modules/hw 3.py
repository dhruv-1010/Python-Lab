#sample input
#lst1= [(1,2),(3,4),(5,6)]
#lst2= [(7,8),(9,10),(11,12)]
#sample output 
# lst=[(1,12)]
n=int(input("Enter the number of rows:"))
a=int(input("Enter the number of columns: "))
lst1=[]
lst2=[]
lst3=[]
for i in range(n):
    tpl=()
    for j in range(a):
        x=int(input("Enter the value of element [{0}][{1}] list 1:".format(i,j)))
        tpl+=x,
    lst1.append(tpl)
for i in range(n):
    tpl1=()
    for j in range(a):
        y=int(input("Enter the value of element [{0}][{1}] list 2:".format(i,j)))
        tpl1+=y,
    lst2.append(tpl1)
for i in lst1:
    x=i[0]
    break
for j in lst2:
    if(j==(n-1)):
        y=j[-1]
c=tuple((x,y))
lst3.append(c)
print(lst3)        