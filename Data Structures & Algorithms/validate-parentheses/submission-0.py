class Solution:
    def isValid(self, s: str) -> bool:
        charDict = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
        i = 0
        stack = []
        check = 0
        while i<len(s):
            if charDict[s[i]] > 0:
                stack.append(s[i])
            else:
                if len(stack)>0:
                    elem = stack.pop()
                    if charDict[elem] + charDict[s[i]] != 0:
                        return False
            check += charDict[s[i]]
            i+=1
        if check == 0 and len(stack) == 0:
            return True
        return False