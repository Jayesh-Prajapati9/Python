f=open(input("Enter The File Name:"))
for i,line in enumerate(f):
    if i%5==0and i!=0:
        x=input("Enter Any key to continue OR Q to Stop:")
        if x.upper()=="Q":
            break
        else:
            print(line)
    else:
        print(line)
