class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        sorted_nums = self.merge_sort(nums)
        return sorted_nums[len(sorted_nums) // 2]

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged