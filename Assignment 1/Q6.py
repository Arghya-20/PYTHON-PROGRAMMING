6.	#Two numbers are input through the keyboard into two locations C and D. 
    #Write a program to interchange the contents of C and D.
Loc_C=int(input('Enter loc value of c :'))
Loc_D=int(input('Enter loc value of D :'))
print("  ")
print('After Swappiing :-')
print('loc of C :',Loc_C)
print('loc of D :',Loc_D)
Loc_C , Loc_D =Loc_D , Loc_C
print("  ")
print('Before swapping :-')
print('loc of C :',Loc_C)
print('loc of D :',Loc_D)
