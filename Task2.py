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
all_nums = []
for row in range(0, len(calls)):
    for col in range(0, 2):
        all_nums.append(calls[row][col])
all_nums = list(set(all_nums))
num_dict = {}
num_dict = dict.fromkeys(all_nums)
for key in num_dict:
    for row in range(0, len(calls)):
        for col in range(0, 2):
            if (key == calls[row][col]):
                if num_dict[key] == None:
                    num_dict[key] = 0 + int(calls[row][3])
                else:
                    num_dict[key] = num_dict[key] + int(calls[row][3])
max_key = max(num_dict, key = num_dict.get)
print (str(max_key) + ' spent the longest time, ' + str(num_dict[max_key]) + ' seconds, on the phone during September 2016.')

