wordsfreqdict={"kanishk":32,"patel":23,"royal":45}
l=sorted(wordsfreqdict.items(), key=lambda x:x[1])
print(l)
for i in l:
    print(i[0] , ":" , i[1] )
    