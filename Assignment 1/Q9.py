#If a four-digit number is input through the keyboard, 
#write a program to obtain the sum of the first and last digit of this number
n=int(input('enter a number :'))
r1=n%10
n=n//10
r2=n%10
n=n//10
r3=n%10
n=n//10
r4=n%10
n=n//10
sum=r1+r4
print('The sum is :',sum)