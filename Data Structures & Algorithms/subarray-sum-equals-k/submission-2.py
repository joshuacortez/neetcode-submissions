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
        indices = {}
        for i, p in enumerate(prefix):
            hashmap[i] = p+k
            if p not in indices:
                indices[p] = set([i])
            else:
                indices[p].add(i)

        total_subarrays = 0
        for i,total in hashmap.items():
            if total in indices:
                j_indices = indices[total]
                for j in j_indices:
                    if i < j:
                        total_subarrays += 1

        return total_subarrays
