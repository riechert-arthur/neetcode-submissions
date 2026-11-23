class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        def area(l, r):
            return (r - l) * min(heights[l], heights[r])

        while l <= r:
            curr_area = area(l, r)
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area