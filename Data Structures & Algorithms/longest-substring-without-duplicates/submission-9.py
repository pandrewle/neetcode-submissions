class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        start = 0
        char_set = set()
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            count = max(count, end - start + 1)
        return count
                