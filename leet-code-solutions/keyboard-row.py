class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            toLower_word = word.lower()
            in_row = False

            # Check if all characters in the word belong to the same row
            for row in rows:
                temp = len(toLower_word)
                for char in toLower_word:
                    if char in row :
                        temp -= 1
                    else: 
                        break
                        
                if temp == 0:
                    in_row = True

            if in_row:
                result.append(word)

        return result

                