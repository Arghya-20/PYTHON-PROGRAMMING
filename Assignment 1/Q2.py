#The distance between two cities (in km.) is input through the keyboard. Write a program to
#convert and print this distance in meters, feet, inches and centimeters.
Dis_km=int(input('Enter the distance of two cities in km :'))
m= Dis_km*1000
cm=Dis_km*100
inch=cm/2.54
ft=inch/12
print('Meter is      :',m)
print('centimeter is :',cm)
print('inch is       :',inch)
print('Feet is       :',ft)


