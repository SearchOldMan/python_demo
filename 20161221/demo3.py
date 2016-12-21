class Countlist:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]


c1 = Countlist(2,3,4,5)
c2 = Countlist(1,24,5,67,7)

print c1[2]