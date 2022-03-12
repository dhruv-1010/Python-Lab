n = int(input("Enter no of characters"))
n1,n2=0,1
for i in range(n+1):
	n1,n2=n2,n1+n2
	print(n2," ",end="")

