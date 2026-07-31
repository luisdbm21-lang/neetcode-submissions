class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        for i in range(len(words)):
            if words[i] != self.calculate_ith_column_word(words, i):
                return False
        return True

    def calculate_ith_column_word(self, words: list[str], j: int) -> str:
        column_word = ''
        for i in range(len(words[j])):
            try:
                column_word += words[i][j]
            except:
                return False
        return column_word