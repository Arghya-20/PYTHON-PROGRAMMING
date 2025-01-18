'''Any year is input through the keyboard. Write a program to determine whether the year is a
leap year or not'''

year=int(input("enter year:"))
if (year%4==0 and year % 100!=0) or (year%400==0):
    print('leap year')
else:
    print('not  a leap year')
