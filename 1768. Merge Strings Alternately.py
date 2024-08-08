class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        left = 0
        minLength = min(len(word1), len(word2))
        maxLength = max(len(word1), len(word2))

        while left < minLength:
            word += word1[left] + word2[left]
            left += 1
        
        if len(word1) == len(word2):
            return word
        
        if len(word1) > len(word2):
            while left < maxLength:
                word += word1[left]
                left += 1
        else:
            while left < maxLength:
                word += word2[left]
                left += 1
        
        return word