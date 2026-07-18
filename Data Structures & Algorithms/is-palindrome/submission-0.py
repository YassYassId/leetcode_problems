class Solution:
    def isPalindrome(self, s: str) -> bool:
        concat_s = "".join(e.lower() for e in s if e.isalnum())
        n = len(concat_s)
        i = 0
        j = n-1
        isPalindrome = True
        while j> i:
            if  concat_s[i] == concat_s[j]:
                i += 1
                j -= 1
            else: return not isPalindrome
        return isPalindrome