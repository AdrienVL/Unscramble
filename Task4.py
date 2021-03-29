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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

numbers = []
telemarketers = []


for call in calls:
    numbers.append(call[0])


#Remove duplicate numbers
numbers = set(numbers)
telemarketers = list(numbers)

for number in numbers:
    for call in calls:
        if number == call[1]:
            telemarketers.remove(number)
            break

numbers = telemarketers

for number in numbers:
    for text in texts:
        if number == text[0] or number == text[1]:
            telemarketers.remove(number)
            break



print("These numbers could be telemarketers: \n")

telemarketers = sorted(telemarketers)

for telemarketer in telemarketers:
    print(telemarketer)

