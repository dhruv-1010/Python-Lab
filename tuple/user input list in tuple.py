n=int(input("Enter the number of rows  :"))
o=int(input("Enter the number of columns  :"))
lst=[]
for j in range(n):
    tpl=()
    for i in range(o):
        a=int(input("Enter the element %d:"%(i+1)))
        tpl+=a,
    lst.append(tpl)
print(lst)