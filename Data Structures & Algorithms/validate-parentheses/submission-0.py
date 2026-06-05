from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        h_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        deq = deque()
        for i in s:
            if i in h_map:
                if len(deq)==0:
                    return False
                if h_map[i] != deq[-1]:
                    return False
                else:
                    deq.pop()
                continue
            deq.append(i)

        return len(deq)==0