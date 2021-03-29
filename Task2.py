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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#Dictionary of distinct phone numbers (keys) and call duration (values). 

numbers = []
numberDict = {}

for i in range(2):

    for call in calls:
        numbers.append(call[i])

    #Distinct Phone numbers in dictionary
    numberDict = (dict.fromkeys(numbers, 0))

    #Aggregating call time for each caller
    for call in calls:
        numberDict[call[i]] = numberDict.get(call[i]) + int(call[3])


phonesLongest = max(numberDict, key=numberDict.get)
longestCall = max(numberDict.values())

print("{} spent the longest time, {}  seconds, on the phone during September 2016.".format(phonesLongest, longestCall))

"""
Time Complexity

Linear:


2 for loops running twice: O(4n)
.get(key): O(n)
max function: O(n)


Result:
O(6n) -> O(n)


"""