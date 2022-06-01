x={}
n=int(input("Enter the number of elements: "))
for i in range(n):
    k=input("Enter the keys:")
    v=int(input("Enter its value:"))
    x.update({k:v})
print(x)
s=sum(x.values())   #to find sum
print(s)
print(len(x))