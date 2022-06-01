str=input("Enter the main string :")
sub=input("Enter the sub  string :")
n=len(str)
flag=True
position=-1
while(True):
    position=str.find(sub,position+1,n)
    if position==-1:
        break
    print("found at position ",position+1)
    flag=True
if flag==False:
    print("Sub string not found:")

