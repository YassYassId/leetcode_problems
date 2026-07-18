class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictGrp = {}
        for i, word in enumerate(strs):
            sort = "".join(sorted(word))
            if sort not in dictGrp:
                dictGrp[sort] = []
            dictGrp[sort].append(word)
        return list(dictGrp.values())
            
