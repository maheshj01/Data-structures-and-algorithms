### Problem 438. Find All Anagrams in a String (Medium): https://leetcode.com/problems/find-all-anagrams-in-a-string/

# hint: maintain two hashmaps one for window and one for p
# Use sliding window update the window hashmap and check if it is equal to p hashmap
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if(len(p) > len(s)):
            return result
        freq = {}
        for letter in p:
            if(letter in freq):
                freq[letter] += 1
            else:
                freq[letter] = 1

        window = {}
        for i in range(len(p)):
            if(s[i] in window):
                window[s[i]]+=1
            else:
                window[s[i]]=1

        start = 0
        end = len(p)-1
        result = []
        while(end < len(s)):
            if(window == freq):
                result.append(start)

            window[s[start]] -= 1

            if(window[s[start]] == 0):
                del window[s[start]]

            if(end < len(s) - 1):
                if(s[end + 1] in window):
                    window[s[end + 1]] += 1
                else:
                    window[s[end + 1]] = 1

            start+= 1
            end += 1
        return result

# Pattern
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



