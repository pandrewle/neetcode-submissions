class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        left = 0
        max_freq = 0
        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(max_freq, freq[ch])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res
