n=tuple(map(eval,input("Enter the values separated with a space: ").split()))
pos=int(input("Enter the position to insert the element: "))
e=tuple(input("Enter the element that you want to insert:"))
a=n[:pos-1]
b=n[pos-1:]
print(a+e+b)