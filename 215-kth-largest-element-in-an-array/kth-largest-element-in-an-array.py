class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(start, end, k_smallest):
            if start == end:
                return nums[start]
            pivot_index = (start + end) // 2 
            pivot_value = nums[pivot_index]
            left, right = start - 1, end + 1
            while left < right:
                while True:
                    left += 1
                    if nums[left] >= pivot_value:
                        break
                while True:
                    right -= 1
                    if nums[right] <= pivot_value:
                        break
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            if right < k_smallest:
                return quick_select(right + 1, end, k_smallest)
            return quick_select(start, right, k_smallest)
        n = len(nums)
        k_smallest = n - k
        return quick_select(0, n - 1, k_smallest)