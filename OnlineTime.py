# You are given a file called logfile.txt that has logon and logoff time for thew user each line has 3
# entry separedt by , one i username 2 is logon 3 is logoff times are in 24hrs format you can assume that 
# all logon and logoff are on same day write a program that scan for who are online for atleast an hour 
# with thier online time 

f=open("logfile.txt")
l=list()
d={}
for i in f:
    l.extend(i.split(","))

print(l)

for j in range(0,len(l),3):
    login=l[j+1]
    time1=int(login[0:2])*60+int(login[3:5])
    logout=l[j+2]
    time2=int(logout[0:2])*60+int(logout[3:5])
    difference=time2-time1
    if j not in d:
        if difference>=60:
            d[l[j]]=difference
print(d)