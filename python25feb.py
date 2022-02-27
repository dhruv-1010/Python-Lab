#first

a = int(input("Enter number to multiply with :  "))
b = a<<5
print("value of number x 32 =  ",b)

#second
a = int(input("Enter the number to multiply with : "))
b = a<<5
b = b | a
print("Value of number x 33 = ",b)

#third
a = int(input("Enter any binary"))
b = a&1
print("Last digit = ",b)
 
 #fourth
a = int(input("Enter uni roll"))
n1 = a%1000
q1=n1//100
n2=a%100
q2=n2//10
n3=a%10
print("The sum is  = ",q1+q2+n3)

#fifth
a = int(input("Enter any 3 Digit number"))
n1 = a//100
n2=a%100
q1=n2//10
q2=a%10
print("The number rev is = ",100*q2+10*q1+n1)

#Bmi
a = int(input("Enter weight in kg"))
b = int(input("Enter height in m"))
bmi = a/(b**2)
print("Your BMI is %.3f"%bmi)

