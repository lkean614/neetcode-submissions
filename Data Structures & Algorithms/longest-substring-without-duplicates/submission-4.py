class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset =set()
        res = 0
        l = 0

        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[l])
                l+=1

            hashset.add(s[i])
            res = max(res,len(hashset))

        return res