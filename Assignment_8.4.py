# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# Desired Output:
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    strippedline = line.rstrip()
    words = strippedline.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print lst
