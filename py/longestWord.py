# Write a program to find longest words or word from file 
f=open("pager.txt","r")
max=0
l=list()
for j in f:
    l.extend(j.split())
    for i in l:
        if max<len(i):
            max=len(i)
        
for i in l:
    if max==len(i):
        print(i)

