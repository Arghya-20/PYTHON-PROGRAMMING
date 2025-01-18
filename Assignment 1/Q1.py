#Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
#salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
#salary.
bs=int(input('Enter the basic salary :'))
da = 0.40 * bs  
hra = 0.20 * bs
gross_salary = bs + da + hra
print('Gross salary is :',gross_salary)
