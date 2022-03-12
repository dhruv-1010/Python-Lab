'''q1 and q2'''
s=input("Enter string : ")
print(s[::-1])
n=len(s)
i=0
while(n>0):
	print(s[n-1],end="")
	n-=1
print()
'''q3'''
s=input("Enter string : ")
n=len(s)
i=0
a=''
while(i<n):
	if(i%2==0):
		a+=s[i]
	i+=1
print(a,end="")
print()
