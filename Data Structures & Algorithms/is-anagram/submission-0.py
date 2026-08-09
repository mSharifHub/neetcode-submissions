class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        wrd_1 = {}
        wrd_2 = {}

        for char in s:
            wrd_1[char] = wrd_1.get(char,0) + 1

        for char in t:
            wrd_2[char] = wrd_2.get(char,0) + 1


        for key,value in wrd_1.items():
            if value != wrd_2.get(key,0):
                return False
          

        return True

        