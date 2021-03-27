"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

"""

#Task 1 - The script correctly prints number of distinct telephone numbers in the dataset.

#Append numbers in a new list. Then remove duplicates

numbers = []

for text in texts:
    numbers.append(text[0])
    numbers.append(text[1])

for call in calls:
    numbers.append(call[0])
    numbers.append(call[1])

#Remove any duplicates
numbers = list(dict.fromkeys(numbers))
print("There are {} different telephone numbers in the records.".format(len(numbers)))


