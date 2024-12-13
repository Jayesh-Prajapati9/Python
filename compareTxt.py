# Write a program to compare 2 txt files if they are different give 
# the line and char no in the files where the 2st difference occurs
f1=open("pager.txt")
f2=open("writefile.txt")
l1=f1.readlines()
l2=f2.readlines()

for i,j in enumerate(l1):
    if j!=l2[i]:
        for k,char in enumerate(j):
            if char!=l2[i][k]:
                print("line Number: ",i+1,"char no: ",k+1)
                break
        break

