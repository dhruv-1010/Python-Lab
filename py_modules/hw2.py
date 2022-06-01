#sample input
#lst1= [(1,2),(3,4),(5,6)]
#lst2= [(7,8),(9,10),(11,12)]
#sample output 
# lst=[(1,2),(11,12)]
n=int(input("Enter the number of rows:"))
a=int(input("Enter the number of columns: "))
lst1=[]
lst2=[]
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
a=lst1.pop(0)
b=lst2.pop()
c=(a,b,)
print(list(c))