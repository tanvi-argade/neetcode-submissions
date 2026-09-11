class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            length=len(s)
            slength=str(length)
            string=string+slength+"#"+s
        return string

    def decode(self, s: str) -> List[str]:
        strs=[]
        start=0
        while start<len(s):
            hsh=s.index("#",start)
            nlength=int(s[start:hsh])
            start=hsh+1
            end=start+nlength
            strs.append(s[start:end])
            start=end
        return strs
            
