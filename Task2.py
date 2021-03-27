"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# with open('testingCalls.csv', 'r') as f:
#     reader = csv.reader(f)
#     testingCalls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#Dictionary of phone numbers + add seconds

#Create a dictionary of distinct phone numbers

numbers = []


for call in calls:
    numbers.append(call[0])
    numbers.append(call[1])

numbers = (dict.fromkeys(numbers,0))

for call in calls:
    numbers[call[0]] = numbers.get(call[0]) + int(call[3])
    numbers[call[1]] = numbers.get(call[1]) + int(call[3])


phonesLongest = max(numbers, key=numbers.get)
longestCall = max(numbers.values())

print("{} spent the longest time, {}  seconds, on the phone during September 2016.".format(phonesLongest, longestCall))

