x={}
n=int(input("How many players:"))
for i in range(n):
    a=input("Enter the name of the player:")
    b=int(input("Enter the runs scored by the player:"))
    x.update({a:b})
print(x)
for pname in x.keys():
    print(pname)
n=input("Enter the name of the player:") 
run=x.get(n,-1)
if(run==-1):
    print("Player not found:")
else:
    print("{0} made runs {1}".format(n,run))   

