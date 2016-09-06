# Read through and parse a file with text and numbers.
# Extract all the numbers in the file and compute the sum of the numbers.

import re
fhand = open("regex_sum_270119.txt")
lst = []
for line in fhand:
    numbers = re.findall("[0-9]+", line)
    if len(numbers) > 0:
        for num in numbers:
            num = int(num)
            lst.append(num)

sum = 0
for num in lst:
    sum += num
print sum
