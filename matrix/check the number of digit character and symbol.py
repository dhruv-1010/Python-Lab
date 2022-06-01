n=input("Enter the string:")
a=len(n)
c,d,s=0,0,0
for i in range(a):
    if((n[i]>='a' and n[i]<='z') or (n[i]>='A' and n[i]<='Z')):
        c=c+1
    elif( n[i]>='0'and n[i]<='9'):
        d=d+1
    else:
        s=s+1
print("Total number of character is ",c)
print("Total number of  digits is ",d)
print("Total numer of special symbol is ",s)