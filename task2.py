'''
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name
'''
n1=input("Enter your first name:")
n1=str(n1)
n2=input("Enter your last name:")
n2=str(n2)
name= n1 + " " + n2
print("Hello,",name,"!","Welcome to the Python Program.")