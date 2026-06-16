class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        triplets = set()
        for k, k_val in enumerate(sorted_nums):
            i = 0
            j = len(sorted_nums) - 1
            k_val = -k_val

            while i < j:
                if i == k:
                    i+=1
                if j == k:
                    j-=1
                if i == j:
                    continue
                candidate = sorted_nums[i] + sorted_nums[j]
                if candidate < k_val:
                    i+=1
                elif candidate > k_val:
                    j-=1
                else:
                    triplet = tuple(sorted([-k_val, sorted_nums[i], sorted_nums[j]]))
                    triplets.add(triplet)
                    i+=1
                    j-=1

        return list(triplets)

        