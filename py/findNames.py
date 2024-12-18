f=open("namelist.txt")
user=input("Enter The Intials : ").upper()
for i in f:
    final=i.split()
    if len(final)==3 and len(user)==3:
        if(final[0][0]==user[0] and final[1][0]==user[1] and final[2][0]==user[2]):
            print(i)
    elif len(user)==2 or len(final)==2 :
        if(len(final)==3):
            if(final[0][0]==user[0] and final[2][0]==user[1]):
                print(i)
        elif(len(final)==2):
             if(final[0][0]==user[0] and final[1][0]==user[1]):
                print(i)