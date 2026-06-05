class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index,height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                pop_i,pop_h = stack.pop()
                max_area = max(max_area, pop_h * (index - pop_i))
                start = pop_i
            stack.append((start,height))
        for i,h in stack:
            max_area = max(max_area,h * (len(heights)- i))

        return max_area