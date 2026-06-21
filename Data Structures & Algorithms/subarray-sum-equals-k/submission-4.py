class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## main idea
        # A prefix sum turns a ranged sum question in to a differncing question
        # prefix[j] - prefix[i-1] = sum(from i to j)
        # prefix[j] = k + prefix[i-1]

        # Phase 1: build the prefix array
        curr_sum = 0
        prefix = [0]
        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)

        # Phase 2: count pairs where prefix[j] - prefix[i] = k, with i < j
        # this is equivalent to prefix[i] = prefix[j] - k
        # prefix[i] should have come first before k - prefix[j]
        total_subarrays = 0
        counts = {}
        for p in prefix:
            look_in_old = p - k
            if look_in_old in counts:
                total_subarrays += counts[look_in_old]

            counts[p] = counts.get(p, 0) + 1
            
           
        return total_subarrays
