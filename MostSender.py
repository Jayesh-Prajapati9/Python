f=open("mbox-short.txt")
count=0
d={}
final_d={}
for line in f:
    if line.startswith("From "):
            d[(line.split(" ")[1])]=d.get((line.split(" ")[1]),0)+1
final_d=dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
print(final_d)
