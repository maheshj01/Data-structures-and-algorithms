# 904. Fruit Into Baskets
# sliding window

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # [1,2,3,2,2]
        # right = 0
        # left = 0
        # {1: 1, 2: 1}

        types = defaultdict(int)
        max_fruits = 0
        left = 0
        for right in range(len(fruits)):
            types[fruits[right]] += 1
            while(len(types) > 2):
                types[fruits[left]] -=1
                if(types[fruits[left]] == 0):
                    del types[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits