class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store1 = {}
        store2 = {}
        
        for i in range(len(s)):
            store1[s[i]] = 1 + store1.get(s[i], 0)
            store2[t[i]] = 1 + store2.get(t[i], 0)

        for c in store1:
            if store1[c] != store2.get(c, 0):
                return False
        return True
            
        