class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## main idea
        # A prefix sum turns a ranged sum question in to a differncing question
        # prefix[j] - prefix[i-1] = sum(from i to j)
        # prefix[j] = k + prefix[i-1]
        curr_sum = 0
        prefix = [0]
        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)

        hashmap = {}
        for i, p in enumerate(prefix):
            hashmap[i] = p+k

        total_subarrays = 0
        for i,total in hashmap.items():
            for p in prefix[(i+1):]:
                if total == p:
                    total_subarrays += 1

        return total_subarrays
