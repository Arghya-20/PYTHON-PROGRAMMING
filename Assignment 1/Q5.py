#The length & breadth of a rectangle and radius of a circle are input through the keyboard. 
#Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle. 

Len=int(input('enter the Length of a Rectangle     : '))
Bredth=int(input('enter the bredth of a Rectangel     : '))
rad=float(input('enter the radius of a cirlcle       : '))
Area=Len*Bredth
print("  ")
perimeter=2*(Len + Bredth)
print('Area of retangle is           : ',Area)
print('Perimeter of rectangle is     : ',perimeter) 
print("  ")
Area= 3.14*rad*rad
circumference=2*3.14*rad
print('Area of Circle is              : ',Area)
print('circumference of circle is     : ',circumference)