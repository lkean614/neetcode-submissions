class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)
        have = 0
        target = defaultdict(int)
        current = defaultdict(int)
        l,res=0,""
        minlen = len(s)+1

        for i in t:
            target[i] +=1

        for r in range(len(s)):
            if s[r] in target :
                current[s[r]]+=1
                if current.get(s[r],0) <= target.get(s[r]):
                    have +=1
                
            while have == need:
                current_length = r - l + 1
                if current_length < minlen:
                    minlen = current_length
                    res = s[l : r+1]
                if s[l] in target:
                    current[s[l]] -= 1
                    if current[s[l]] < target[s[l]]:
                        have -= 1
                l+=1

        return res