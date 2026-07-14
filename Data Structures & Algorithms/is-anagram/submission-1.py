class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWordLen = len(s)
        secondWordLen = len(t)
        if firstWordLen != secondWordLen:
            return False
        firstWord = list(s)
        secondWord = list(t)
        for i in range(firstWordLen):
            if firstWord[i] in secondWord:
                secondWord.remove(firstWord[i])
        if len(secondWord) == 0:
            return True
        else:
            return False
