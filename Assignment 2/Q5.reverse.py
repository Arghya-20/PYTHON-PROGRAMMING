num=int(input('enter a number:'))
sum=0
a=num
while(num>0):
    b=num%10
    sum=sum*10+b
    num=num//10
if(a==sum):
    print('palindrome')
else:
    print('not a palindrome')

