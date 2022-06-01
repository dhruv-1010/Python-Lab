# sample input=['DHRUV', 'ritik', 'rahul', 'govind', 'dev']
# sample output+=['DHRUV', 'RITIK', 'RAHUL', 'GOVIND', 'DEV']
a=input("Enter string with space:").split()
print(a)
lst=list(map(lambda x:x.upper(), a))
print(lst)