n1=input("Enter first string:")
n2=input("Enter second string:")
n=int(input("Enter the no of character you want to swap: "))

a=n1[0:n]
b=n2[0:n]
c=n1[n:]
d=n2[n:]
print(b+c)
print(a+d)