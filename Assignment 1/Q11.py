#A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn
#is input through the keyboard in hundreds, find the total number of currency notes of each
#denomination the cashier will have to give to the withd rawer.

amount=int(input("Enter the number of amount :- "))
Hundreds=amount//100
Fifties=(amount%100)//50
Tens=(amount%100)%50//10

print("Number of Hundred's   : ",Hundreds)
print("Number of Fiftie's    : ",Fifties)
print("Number of Ten's       : ", Tens)