#If a five-digit number is input through the keyboard, write a program to reverse the number.
n=int(input('enter a number :'))
r1=n%10
n=n//10
r2=n%10
n=n//10
r3=n%10
n=n//10
r4=n%10
n=n//10
r5=n%10
n=n//10
print('The reverse number are :',r1,r2,r3,r4,r5)
