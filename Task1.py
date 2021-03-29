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

#Task 1 - 


numbers = []

#Append numbers in list

def count(calls,texts):
    for i in range(2):

        for text in texts:
            numbers.append(text[i])

        for call in calls:
            numbers.append(call[i])

    return numbers


#Remove any duplicates using set type
numbers = set(count(calls,texts))
print("There are {} different telephone numbers in the records.".format(len(numbers)))

"""
Time Complexity

Linear:

4n -> n

"""


