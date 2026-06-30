class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    i = j
                    j += 1
                else:
                    break
            if len(seen) > res:
                res = len(seen)

        return res
                
