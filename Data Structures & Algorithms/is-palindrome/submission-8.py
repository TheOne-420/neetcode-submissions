class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            leftChar=s[l].lower()
            rightChar=s[r].lower()

            while (not leftChar.isalpha() and not leftChar.isdigit()) and l<r:
                l+=1
                leftChar= s[l].lower()
            while (not rightChar.isalpha() and not rightChar.isdigit() ) and r>l:
                r-=1
                rightChar= s[r].lower()
            print(rightChar, leftChar)
            if leftChar==rightChar:
                l+=1
                r-=1
            else:
                return False
        return True
            





