#sample input
#lst1= [(1,2),(3,4),(5,6)]
#lst2= [(7,8),(9,10),(11,12)]
#sample output 
# lst=[(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)]

n=int(input("Enter the number of columns:"))
a=int(input("enter the number of rows"))
lst=[]
for j in range(a):
    tpl=()
    for i in range(n):
        a=int(input("Enter the element [{0}] [{1}] for lst 1:".format(j+1,i+1)))
        b=int(input("Enter the element [{0}] [{1}] for lst 2:".format(j+1,i+1)))
        tpl=a,b,
        lst.append(tpl)
print(lst)