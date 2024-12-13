user=input("Enter The String: ")
f=open("wordlist.txt")
d={}
for i in user:
    d[i]=d.get(i,0)+1
l=f.read().split()
for i in l:
    flag=True
    fd={}
    for j in i:
        fd[j]=fd.get(j,0)+1
    for k in d:
        if k not in fd or d[k]>fd[k]:
            flag=False
    if flag:
        print(i)