n=int(input())
i=1
while(i<=n):
	print("* "*i)
	i=i+1






























'''
n=input()
leng=len(n)
n=int(n)
num=n
q=0

while(n!=0):
	r=n%10
	q=q+r**leng
	n=n//10
print(q)

n=int(input())
num=n
q=0
while(n!=0):
	r=n%10
	q=q*10+r
	n=n//10
print(q)
if(q==num):
	print("Palindromeee")
else:
	print("Not palindromeee")


n=int(input())
num=n
i=1
j=1
while(i<n):
	if(n%i==0):
		print("Factor ",j,"is",i)
		j=j+1
	i=i+1
'''
