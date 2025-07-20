'''
 Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist
'''
try:
    f = open('sample.txt','r')
    reading_file = f.read()
    print(reading_file)
    f.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")