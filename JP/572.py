class SQ ():
    def __init__(self,l):
        self.l=l
    def shift(self):
        if len(self.l)==0:
            raise Exception("List is Empty")
        else:
            first=self.l.pop(0)
        return first
    def unshift(self,a):
        self.l.insert(0,a)
        print(self.l)
    def push(self,a):
        self.l.append(a)
        print(self.l)
    def pop(self):
        if len(self.l)==0:
            raise Exception("List is Empty")
        else:
            return self.l.pop()
    def remove(self):
        self.l.remove(max(self.l))
        print(self.l)

l=eval(input("Enter Your List : "))
sq=SQ(l)
sq.remove()


