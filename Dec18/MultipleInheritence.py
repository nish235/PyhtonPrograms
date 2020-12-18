class Customer:
    def __init__(self, cid, cname, cmob):
        self.id = cid
        self.name = cname
        self.mob = cmob

    def showId(self):
        print(self.id)

    def showName(self):
        print(self.name)

    def showMob(self):
        print(self.mob)


class Transaction(Customer):
    def __init__(self, twid, tdep, tbal):
        self.wid = twid
        self.dep = tdep
        self.bal = tbal

    def showWid(self):
        print(self.wid)

    def showDep(self):
        print(self.dep)

    def showBal(self):
        print(self.bal)


class Bank(Transaction):
    def __init__(self, name, mob, id, wid, dep, bal):
        Customer.__init__(self, name, mob, id)
        Transaction.__init__(self, wid, dep, bal)


class Shop(Transaction):
    def __init__(self, name, bal):
        Customer.__init__(self, name)
        Transaction.__init__(self, bal)


b = Bank('John', '123456', '102', '100', '500', '10000')
b.showName()
print(b.showId())

s = Shop('John', '10000')
s.showName()
print(s.showId())
