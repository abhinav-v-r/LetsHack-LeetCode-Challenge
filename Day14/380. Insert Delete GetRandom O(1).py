class RandomizedSet:

    def __init__(self):
        import random
        self.r = random.choice
        self.arr = []
        self.pos = {}  

    def insert(self, val: int) -> bool:
        return False if val in self.pos else (self.pos.__setitem__(val,len(self.arr)), self.arr.append(val))[1] or True

        

    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        i = self.pos[val]
        last = len(self.arr) - 1
        if i < last:
            self.arr[i], self.arr[last] = self.arr[last], self.arr[i]
            self.pos[self.arr[i]] = i
        self.arr.pop()
        del self.pos[val]
        return True
    
        

    def getRandom(self) -> int:
        return self.r(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
