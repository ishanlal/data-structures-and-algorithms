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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bang_called = []
index = 0
for row in range (0, len(calls)):
    num = calls[row][0]
    if num[0:5] == '(080)':
        if calls[row][1][0:3] == '140':
            bang_called.append('140')
        if ((calls[row][1][0:1] == '7') or (calls[row][1][0:1] == '8') or (calls[row][1][0:1] == '9')):
            bang_called.append(calls[row][1][0:4])
        if calls[row][1][0:1] == '(':
            for chars in range(0, len(calls[row][1])):
                if calls[row][1][chars] == ')':
                    index = chars
            bang_called.append(calls[row][1][0:index+1])
bang_called = list(set(bang_called))
bang_called.sort()
print ('The numbers called by people in Bangalore have codes:')
for item in bang_called:
    print (item)

#PART B
bang_num = []
bang_fixed_line = []
for row in range (0, len(calls)):
    num = calls[row][0]
    if num[0:5] == '(080)':
        bang_num.append(num)
        if calls[row][1][0:5] == '(080)':
            bang_fixed_line.append(calls[row][1])

total_bang_calls = len(bang_num)
same_calls = len(bang_fixed_line)
percentage = (same_calls / total_bang_calls) * 100
perc = str(round(percentage, 2))
print (perc + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')






