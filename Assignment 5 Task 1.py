'''
Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
Marklist = {'Ajay':67,'Balu':36,'Chethan':89}
name = input("Enter a name: ")
if name in Marklist:
    print("{}'s Marks: {}".format(name,Marklist[name]))
else:
    print("Student not found")