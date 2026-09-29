### Sliding Window Patterm

Problem 424

```python

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        result = 0
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(freq[s[right]], max_freq)
            while((right - left + 1) - max_freq > k):
                freq[s[left]] -= 1
                left += 1
            result = max(right - left + 1, result)
        return result
```

Problem 904

```python
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
```

Problem 438.

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_freq = defaultdict(int)
        p_freq = Counter(p)
        left = 0
        result = []
        # c b a e b a b a c d
        # [ 0, ]
        for right in range(len(s)):
            s_freq[s[right]] += 1
            while(right - left + 1 > len(p)):
                s_freq[s[left]] -= 1
                if(s_freq[s[left]] == 0):
                    del s_freq[s[left]]
                left += 1
            if(len(s_freq) == len(p_freq) and s_freq == p_freq):
                result.append(left)
        return result
```
