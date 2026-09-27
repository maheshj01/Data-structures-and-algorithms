# Problem 380. Insert Delete GetRandom O(1) (Medium): https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet2:

    def __init__(self):
        # hashmap to keep track of val -> index of array
        self.mapping = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if(val in self.mapping):
            return False
        else:
            index = len(self.arr)
            self.arr.append(val)
            self.mapping[val] = index
            return True

    def remove(self, val: int) -> bool:
        if(val not in self.mapping):
            return False
        else:
            # arr = [2]
            # map = {2: 0}
            index = self.mapping[val] # 0
            lastElement = self.arr[-1] # 2
            self.arr[index] = lastElement #
            self.mapping[lastElement] = index
            del self.mapping[val]
            self.arr.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# stack = [2]
# hashMap = {
    # 2: 0
# }

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()