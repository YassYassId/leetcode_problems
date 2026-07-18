class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for x in s:
            dict_s[x] = dict_s.get(x,0) +1
        for x in t:
            dict_t[x] = dict_t.get(x,0) + 1
        return dict_s == dict_t
        