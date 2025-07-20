'''
Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
f = open('output.txt','w')
f.write(input("Enter text to write to the file: "))
print("Data successfully written to output.txt")
f.close()

f = open('output.txt','a')
f.write("\n")
f.write(input("Enter additional text to append: "))
print("Data successfully appended")
f.close()

f = open('output.txt','r')
print("Final content of output.txt:")
reading_file = f.read()
print(reading_file)
f.close()