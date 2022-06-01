n=input("Enter the string: ")
i=1
a=len(n)
while(i<=a):
    if(i%2==1):
        print(n[i-1],end="")
    i=i+1