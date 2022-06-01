n=int(input("Enter the number : "))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("factorial of the number {0} is {1}".format(n,fact))