class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            width = j - i
            min_height = min(height[i], height[j])

            area = width * min_height
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1

        return max_area