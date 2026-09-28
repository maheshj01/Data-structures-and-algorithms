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
