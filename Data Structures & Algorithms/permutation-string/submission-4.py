class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        counter = {}
        for r, c in enumerate(s2):
            counter[c] = counter.get(c, 0) + 1
            if r >= len(s1):
                counter[s2[r - len(s1)]] -= 1
                if counter[s2[r - len(s1)]] == 0:
                    del counter[s2[r - len(s1)]]
            if counter == freq:
                return True
        
        return False