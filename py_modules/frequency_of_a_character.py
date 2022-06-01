n=input("Enter the string:")
c=input("Enter the  character to find its frequency :")
a=len(n)
count=0
for i in range(a):
    if(c==n[i]):
        count=count+1
print("Frequency of ",c,"is ",count)