class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        l = 0
        counter = {}
        have, need = 0, len(freq)
        res, resLen = "", float("infinity")
        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1
            if c in freq and counter[c] == freq[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                counter[s[l]] -= 1
                if s[l] in freq and counter[s[l]] < freq[s[l]]:
                    have -= 1
                l += 1
        
        return res
        