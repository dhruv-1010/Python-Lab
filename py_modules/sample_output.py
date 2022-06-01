x={}
n=int(input("Enter the number of elements: "))
v=int(input("Enter the value (v) value:"))
for i in range(1,n+1):
    x.update({i:i*v})
print(x)