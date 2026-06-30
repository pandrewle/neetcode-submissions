class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            letters = [0]*26
            for c in str:
                letters[ord(c)-ord('a')] += 1
            ans[tuple(letters)].append(str)
        
        return list(ans.values())