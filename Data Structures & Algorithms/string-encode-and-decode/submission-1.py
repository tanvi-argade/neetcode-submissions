#improved variable names
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded=encoded+str(len(s))+"#"+s
        return encoded        

    def decode(self, s: str) -> List[str]:
        decoded=[]
        start=0
        while start < len(s):
            hsh=s.index("#",start)
            length=int(s[start:hsh])
            start=hsh+1
            end=start+length
            decoded.append(s[start:end])
            start=end
        return decoded
