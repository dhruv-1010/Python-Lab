# sample Input----------->{"kanishk":"one","patel":"two","aman":"three"}
# sample output:--------->{'KANISHK': 'one', 'PATEL': 'two', 'AMAN': 'three'}
a={"kanishk":"one","patel":"two","aman":"three"}

b={}
for i in a.keys():
    c=i.upper()
    d=a[i]
    for j in range(len(a)):
        b.update({c:d})
print(b)