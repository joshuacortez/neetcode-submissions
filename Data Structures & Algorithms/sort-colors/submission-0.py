class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [0]*3
        for num in nums:
            buckets[num] += 1

        i = 0
        for j, bucket_count in enumerate(buckets):
            for _ in range(bucket_count):
                nums[i] = j
                i += 1
        