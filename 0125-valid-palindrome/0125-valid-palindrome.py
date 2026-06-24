class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalpha() or i.isdigit():
                a=i.lower()
                r=r+a
        b=r[::-1]
        if r==b:
            return True
        else:
            return False

        

        