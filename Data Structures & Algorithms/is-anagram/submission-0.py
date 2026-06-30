class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            ans = defaultdict(int)
            for i in range(len(s)):
                ans[s[i]] += 1
                ans[t[i]] -= 1
            for val in ans.values():
                if val != 0:
                    return False
            return True
        return False