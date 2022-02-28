# minimum notes problem
abc = int(input("Enter money you want"))
abc1 = abc-100
notestwok = abc1//2000
rem = abc1%2000
notesfiv = rem//500
rem3 = rem%500
notesone = rem3//100
print("no of minimum notes required = ",notestwok + notesfiv + notesone + 1)
# rabbit- chicken farmhouse problem
h_c = int(input("Enter Head count"))
l_c = int(input("Enter leg count"))
rab = (l_c - 2*h_c)/2
chi = h_c - rab
print("Rabbits and chickens are %d %d"%(rab,chi))
# Maximum runs in an over
over  = int(input("Enter overs"))
runs = 30*(over - 1) + 3*(over - 1) + 36
print("Max Runs possible %d"%runs)
