n=input("Enter the string: ")
a=len(n)
for i in range(a):
    if(i%2==0):  #because index is starting from zero so first index is zero 
        print(n[i].upper(),end="")
    else:
        print(n[i],end="")