class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = ""
        for s in strs:
            length = len(s)
            encoded_result += f"{length}" + "#" + s
        return encoded_result

    def decode(self, s: str) -> List[str]:
        result = []
        x=0
        while x < len(s) :
            temp=""
            while(s[x].isdigit()):
                temp += s[x]
                x+=1
            if(temp.isdigit()):
                count = int(temp)
            result.append(s[x+1:x+count+1])
            x = x+count+1
        return result

