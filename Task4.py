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

#Create a list of callers
for call in calls:
    numbers.append(call[0])


#Remove duplicate numbers
numbers = set(numbers)

#Create a numbers list duplicate
telemarketers = list(numbers)

#Remove numbers that are not telemarketers from telemarketers list
for number in numbers:
    #Iterate through calls
    for call in calls:
        if number == call[1]:
            telemarketers.remove(number)
            break

#Update numbers list w/ telemarketers list
numbers = telemarketers

for number in numbers:
    #Iterate through texts
    for text in texts:
        if number == text[0] or number == text[1]:
            telemarketers.remove(number)
            break

#Sort telemarketers
telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers:")

for telemarketer in telemarketers:
    print(telemarketer)

"""

Time Complexity

Quadratic:


2 inner for loops: O(2n^2)
sorting: O(n log(n))
1 for loop to print: O(n)

Result:
2n^2 + nlog(n) + n -> n^2 + nlog(n) + n

"""