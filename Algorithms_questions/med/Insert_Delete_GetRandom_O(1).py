import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()
        self.keys_set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hash_map:
            self.hash_map[val] = 1
            self.keys_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hash_map:
            del self.hash_map[val]
            self.keys_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        key = random.sample(self.keys_set, 1)
        return key

if __name__ == "__main__":
    val = 5
    obj = RandomizedSet()
    param_1 = obj.insert(val)
    param_1 = obj.insert(13)
    param_1 = obj.insert(21)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()
    print("kek")