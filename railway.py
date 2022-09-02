class Railway:
    def __init__(self,tn,tname,from_add,destination):
        self.book_ticket(tn, tname, from_add, destination)
    def book_ticket(self,tn,tname,from_add,destination):
        train=Train(tn,tname)
        train.book(from_add,destination)
        train.conformation()
class Train:
    def __init__(self,tn,tname):
        self.tno=tn
        self.tname=tname
    def book(self,fr,dest):
        self.start=fr
        self.dest=dest
    def conformation(self):
        print('ticket booked',self.tname,self.tno,self.start,self.dest,sep="\n")
tn=int(input('enter train no'))
tname=input('train name')
start=input('enter start')
dest=input('enter dest')
r=Railway(tn,tname,start,dest)