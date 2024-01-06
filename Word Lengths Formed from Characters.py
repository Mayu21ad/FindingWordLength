from collections import Counter
from typing import List
class Solution:
    def count_characters(self, word):
        return Counter(word)
    def countCharacters(self, word:List[str], chars:str)->int:
        chars_count = self.count_characters(chars)
        total_length = 0

        for word in words:
            word_count = self.count_characters(word)
            if all(word_count[char] <= chars_count[char] for char in word):
                total_length += len(word)

        return total_length
solution = Solution()
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
result = solution.countCharacters(words, chars)
print(result)
