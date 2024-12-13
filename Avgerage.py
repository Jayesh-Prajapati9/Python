# Write a program that prompts for a file name and look for the line in below format 
# X-DSPAM-Confidence: 0.8475
# Extract the floating point from each of the following line and compute the avg of those values and produce 
# the output
f=open("mbox-short.txt")
sum=0
count=0
for line in f:
    if line.startswith("X-DSPAM-Confidence:"):
        sum+=float(line[20:])
        count+=1
print("AVERAGE IS :",sum/count)
