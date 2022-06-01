a="kanishk=18,ritik=19,rahul=18,govind=20"
lst=[]
for x in a.split(","):
    y=x.split("=")
    lst.append(y)
c=dict(lst)
print(c)