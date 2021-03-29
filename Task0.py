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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Define first Record of texts
firstTextRecord = texts[0]

#Define last record of calls
lastCallRecord = calls[len(calls)-1]



print("First record of texts, {} texts {} at time {}.".format(firstTextRecord[0], firstTextRecord[1], firstTextRecord[2]))
print("Last record of calls, {} texts {} at time {}.".format(lastCallRecord[0], lastCallRecord[1], lastCallRecord[2], lastCallRecord[3]))
