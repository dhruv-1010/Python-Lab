gth = int(input("Enter length of list	:	"))
lst1 = []
i = 0
while(i<length):
	print("Enter element at index %d"%i)
	ele = int(input())
	lst1.append(ele)
	i +=1
a1 = lst1[0]
a2 = lst1[length - 1]
print("the answer of q2 is: ",a1+a2)
if(length%2 != 0):
	resindex = length//2
	a3 = lst1[resindex]
else:
	resindex = length//2+1
	a3 = lst1[resindex-1]
print("the answer of q3 is: ",a1+a2+a3)
oddsum,evensum = 0,0
for index in range(1,length,2):
	oddsum+=lst1[index]
print("even sum is : %d"%oddsum)
for index in range(0,length,2):
	evensum+=lst1[index]
print("even sum is : %d"%evensum)


lst1.sort()
print(lst1)
