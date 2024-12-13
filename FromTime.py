#  From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 You will parse the From line using
# split() and print out the second word in the line (i.e. the entire address of the person who sent the
# message). Then print out a count at the end. Hint: make sure not to include the lines that start
# with ‘From:’. Also look at the last line of the sample output to see how to print the count

f=open("mbox-short.txt")
count=0
for line in f:
    if line.startswith("From "):
            print((line.split(" ")[1]))
            count+=1
print(count)