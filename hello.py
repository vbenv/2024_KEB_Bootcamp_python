class Bill():
    def __init__(self,des):
        self.des= des

class Tail():
    def __init__(self,length):
        self.length = length
class Duck():
    def __init__(self,bill,tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("this duck ahs a",
              self.bill.description,
              "bill and a",
              self.tail.length,
              'tail')
a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

