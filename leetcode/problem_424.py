# Problem 424: Longest Repeating Character Replacement (Medium): https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        result =''
        skip = k
        freq = {}
        while(end != len(s)):
            if(len(s[start:len(s)]) < len(result)):
                break
            if(s[end] not in freq):
                freq[s[end]] = 1
            currentStr = s[start:end+1]
            length = end - start + 1
            maxfreq = self.maxFreq(freq)
            if(length - maxfreq <= k):
                end+=1
                if(end < len(s)): 
                    if s[end] not in freq:
                        freq[s[end]] = 1
                    else:
                        freq[s[end]] += 1
                if(len(currentStr) > len(result)):
                    result = currentStr
            else:
                freq[s[start]] -= 1
                start+=1
        return len(result)

    def maxFreq(self, freq):
        m = 0
        for i, (key, value) in enumerate(freq.items()):
            if(value > m):
                m = value
        return m


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        # A A B A B B A = k = 1
        # a: 1
        # b: 0
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


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s,k)) # 4