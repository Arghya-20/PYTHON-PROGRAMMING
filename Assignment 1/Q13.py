number=input('enter a five digit number: ')
new_number=" "

for digit in number:
    new_digit=(int(digit)+1)%10
    new_number+=str(new_digit)

print('The new number is :',new_number)