f=open("mbox-short.txt")
count=0
d={}
for line in f:
    if line.startswith("From "):
        l=line.split()
        time=l[5][0:2]
        d[time]=d.get(time,0)+1
final_d=dict(sorted(d.items()))
print(final_d)
