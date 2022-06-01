a=["kanishk","ritik","rahul","govind"]
b=["patel","thakur","kori","sharma"]
c=zip(a,b)
d=dict(c)
print(d)
print("{:10s} -------  {:10s}".format('Name','Caste'))
for i,v in d.items():
    print("{:10s} ------- {:10s}".format(i,v))