# sample input---->
#  Enter the number of rows:2
# Enter the number of columns:2
# Enter the element [0][0]: 1
# Enter the element [0][1]: 2
# Enter the element [1][0]: 3
# Enter the element [1][1]: 4
#sample output----->

# ((1, 2), (3, 4))
# sum of all elements is  10

n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
temp=0
a=()
for i in range(n):
    b=()
    for j in range(m):
        x=int(input("Enter the element [{0}][{1}]".format(i,j)))
        temp+=x
        b+=x,
    a+=b,
print(a)
print("sum of all elements is ",temp)