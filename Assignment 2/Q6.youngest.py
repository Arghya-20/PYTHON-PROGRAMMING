# ' If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to
#  determine the youngest of the three'
ram_age=int(input('Enter age:'))
shyam_age=int(input('Enter age:'))
Ajay_age=int(input('Enter age:'))

if ram_age<shyam_age and ram_age<Ajay_age:
    print('ram is the youngest')

elif shyam_age<ram_age and shyam_age<Ajay_age:
    print('shaym is the youngest')

else:
    print('Ajay is the youngest')
    