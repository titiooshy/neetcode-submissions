class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            my_sorted = ''.join(sorted(i))
            res[my_sorted].append(i)
        return list(res.values())