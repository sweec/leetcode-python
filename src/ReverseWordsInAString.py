class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = []
        word = []
        for c in reversed(s):
            if c == ' ':
                if word:
                    words.append(''.join(reversed(word)))
                    word = []
            else:
                word.append(c)
        if word:
            words.append(''.join(reversed(word)))
        return ' '.join(words)