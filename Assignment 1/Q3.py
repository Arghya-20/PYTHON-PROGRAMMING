#If the marks obtained by a student in five different subjects are input through the keybo ard,
#find out the aggregate marks and percentage marks obtained by the student. Assume that the
#maximum marks that can be obtained by a student in each subject is 100.

sub1=int(input('enter the marks of sub1 : '))
sub2=int(input('enter the marks of sub2 : '))
sub3=int(input('enter the marks of sub3 : '))
sub4=int(input('enter the marks of sub4 : '))
sub5=int(input('enter the marks of sub5 : '))
sum=sub1+sub2+sub3+sub4+sub5
print('sum is :',sum)
per=(sum/500)*100
print('percentage is:',per)