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

outgoing_calls = []
numbers_sending_text = []
numbers_receiving_text = []
numbers_receiving_calls = []
final_list_set = []

for row in range (0, len(calls)):
        outgoing_calls.append(calls[row][0])
for row in range (0, len(texts)):
    numbers_sending_text.append(texts[row][0])
for row in range (0, len(texts)):
    numbers_receiving_text.append(texts[row][1])
for row in range (0, len(calls)):
    numbers_receiving_calls.append(calls[row][1])

outgoing_calls = set(outgoing_calls)
numbers_sending_text = set(numbers_sending_text)
numbers_receiving_text = set(numbers_receiving_text)
numbers_receiving_calls = set(numbers_receiving_calls)
final_set = outgoing_calls.difference(numbers_sending_text)
final_set = final_set.difference(numbers_receiving_text)
final_set = final_set.difference(numbers_receiving_calls)
final_list = list(final_set)
final_list.sort()
print ('These numbers could be telemarketers: ')
for item in final_list:
    print (item)






