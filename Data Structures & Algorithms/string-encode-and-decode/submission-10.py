class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += s + '∂'
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        l,r = 0,0
        while r < len(s):
            if s[r] == '∂':
                ans.append(s[l:r])
                l = r + 1
            r += 1
        return ans
                

