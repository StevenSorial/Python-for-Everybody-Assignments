#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#When you are testing below enter mbox-short.txt as the file name.
#Desired Output:
#Average spam confidence: 0.750718518519

total = 0
count = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(" ")
    num = line[pos+1:]
    num = float(num)
    total = total + num
    count = count + 1
print "Average spam confidence:", total/count
