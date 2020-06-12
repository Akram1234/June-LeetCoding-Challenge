import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val]=val
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        try:
            del self.d[val]
            return True
        except KeyError:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.d:
            return None
        else:
            k = list(self.d.keys())
            return k[random.randint(0,len(k)-1)]
            
    


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
