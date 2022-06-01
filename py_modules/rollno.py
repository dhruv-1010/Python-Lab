
n=int(input("Enter the number of students:"))
result={}
fresult={}
result1={}

for i in range(n):
    st=int(input("Enter roll no of student:"))
    nme=input("Enter the name of the studentL ")
    
    flag=0  
    result1={}
    for j in range(1,6):
        
        sub=input("Enter subject name :")
        num=int(input("Enter number in this subject :"))
        flag+=num
        result1.update({sub:num})
    print("sum of five subject marks of student  {0} is {1}".format(i+1,flag))
    print(result1)
    result.update({nme:result1})
    fresult.update({st:result})

print(fresult)
print(flag)
