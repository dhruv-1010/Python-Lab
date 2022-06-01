n=tuple(map(eval,input("Enter the values separated with a space: ").split()))
pos=int(input("Enter the position to delete  the element: "))

a=n[:pos-1]
b=n[pos:]
print(a+b)