n=int(input("Enter the number to find factors: "))
i=n
while(i!=0):
    if(n%i==0):
        print(i)
    i=i-1