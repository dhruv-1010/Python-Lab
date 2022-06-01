a={"hiii":20,"kanishk":12,"patel":15,"aa":25}
a1=sorted(a.items(),key=lambda t:t[0])  #this wil sort keys
a2=sorted(a.items(),key=lambda t:t[1])
print(a1)
print(a2)