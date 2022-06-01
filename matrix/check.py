lst2=[]
for k in range(1,100000):
        temp=k
        suma=0
        while(k!=0):
            r=k%10
            fact=1
            
            for i in range(1,r+1):
                fact=fact*i
            suma+=fact
            k=k//10
        if(temp==suma):
            lst2.append(suma)
print(lst2)