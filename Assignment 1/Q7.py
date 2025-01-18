 #If a five-digit number is input through the keyboard, write a program to calculate the sum of 
#its digits.(Hint: Use the modulus operator ‘%’) 
n=int(input('enter a number :'))
r1=n%10
n=n//10
print(r1,end="  ")
r2=n%10
n=n//10
print(r2,end="  ")
r3=n%10
n=n//10
print(r3,end="  ")
r4=n%10
n=n//10
print(r4,end="  ")
r5=n%10
n=n//10
print(r5,end="  ")
sum=r1+r2+r3+r4+r5
print("  ")
print( 'The sum of five digit is : ',sum)