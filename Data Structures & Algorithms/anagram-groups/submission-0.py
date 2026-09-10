class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict={}
        for s in strs:
            key="".join(sorted(s))
            if key in sdict:
                sdict[key].append(s)
            else:
                sdict[key]=[s]
        return list(sdict.values())