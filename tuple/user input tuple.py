n=int(input("Enter the number of items :"))
tpl=()
for i in range(n):
    a=int(input("Enter the element %d:"%(i+1)))
    tpl+=a,
print(tpl)
