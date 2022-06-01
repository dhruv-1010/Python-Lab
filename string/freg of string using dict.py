a="kanishk"
b={}
for i in a:
    b[i]=b.get(i,0) + 1
for k,v in b.items():
    print("key={} its occurances={}".format(k,v))