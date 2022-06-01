a={}
n=list(input("Enter your name:"))
print(n)
for i in range(1,27):
    ch=96+i
    b=chr(ch)
    for j in range(1,27):
            a.update({b:ch})
sum=0
for i in range (len(n)):
    
     b=n.pop()
     sum=sum+a.get(b)

print(a)
print(sum)