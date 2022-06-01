n=tuple(map(eval,input("Enter the values separated with a space: ").split()))
pos=int(input("Enter the position to modify the element: "))
e=tuple(input("Enter the element that you want to replace:"))
a=n[:pos-1]
b=n[pos:]
print(a+e+b)