class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""

        i = 0
        j = 0

        for x in range(min(len(word1), len(word2))):
            newWord += word1[i]
            newWord += word2[j]

            i += 1
            j += 1
        
        while i < len(word1):
            newWord += word1[i]
            i += 1

        while j < len(word2):
            newWord += word2[j]
            j += 1

        return newWord

sol = Solution()
print(sol.mergeAlternately("abc", "abcdd"))