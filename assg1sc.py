ANS1:
# Finding average of three numbers
a = int(input('Enter number 1 :'))
b = int(input('Enter number 2 :'))
c = int(input('Enter number 3 :'))
Average = (a + b + c) / 3
print("The Average of 3 numbers is: ", Average)



ANS2:
# calculating income tax for a person , all figures are in dollars
income = float(input('Enter your gross income: '))
depend = int(input('Enter number of dependents: '))
tax_i = income - 10000 - (dep * 3000)
print('Your annual tax is: ', tax_i * 0.2)




ANS3:
# student[SID,Name,Gender,Course Name,CGPA]
SID = int(input('Enter your sid: '))
Name = input('Enter your name: ')
Gender = input('Enter your gender: ')
if Gender== 'M' or 'F':
    Gender=Gender
else:Gender= 'U'
Course = input('Enter your course name: ')
CGPA = float(input('Enter your CGPA: '))
Student = [SID, Name, Gender, Course, CGPA]
print('Student Details' , Student )



ANS4:
# making list of marks of students 
Mark1 = int(input('Enter marks of 1st student '))
Mark2 = int(input('Enter marks of 2nd student '))
Mark3 = int(input('Enter marks of 3rd student '))
Mark4 = int(input('Enter marks of 4th student '))
Mark5 = int(input('Enter marks of 5th student '))
Marks = [Mark1, Mark2, Mark3, Mark4, Mark5]
Marks.sort()
print(Marks)


ANS5(a):
# removing element from list
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour.remove('Black')
print(colour)



5(b) 
# replacing elements from list
colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour[3] = colour[4] = 'Purple'
print(colour)


