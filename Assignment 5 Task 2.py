'''
Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

numbers = [i for i in range(1,11)]
print("original list: ",numbers)
extracted_list = numbers[:5]
print("Extracted list: ",extracted_list)
rev = [extracted_list[4-i] for i in range(5)]
print("reversed list: ",rev)