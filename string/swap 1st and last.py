n=input("Enter the number :")
a=len(n)
n=int(n)
first=(n%10)*10**(a-1)
two=n%(10**(a-1))
middle=two//10
middle=middle*10
last=n//(10**(a-1))
rev=first+middle+last
print("NUmber before reverse first and last number  : ",n)
print("NUmber after reverse first and last number: ",rev)