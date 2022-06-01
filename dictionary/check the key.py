x={}
n=int(input("Enter the number of elements: "))

for i in range(n):
    k=input("Enter the keys:")
    v=int(input("Enter its value:"))
    x.update({k:v})
    # all above code is taking a dictionary by user input
print(x)
k=input("Enter the key to check :")
a=x.get(k,[v])
if(a==[v]):
    print("key is not found ")
else:
    print("Key is found:")
    x.pop(k)    #for deleting found key 
    print(x)
