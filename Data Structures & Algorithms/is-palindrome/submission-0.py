class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''.join(ch for ch in s if ch.isalnum()).lower()
        i = 0
        j = len(cleanStr) - 1

        for i in range(len(cleanStr)//2):
            if cleanStr[i] != cleanStr[j]:
                return False
            j-=1
        return True