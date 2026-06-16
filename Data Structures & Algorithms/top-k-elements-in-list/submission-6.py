class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        buckets = [[] for i in range(len(nums)+1)]
        for num, count in count_dict.items():
            buckets[count].append(num)

        results = []
        num_results = 0
        for bucket in buckets[::-1]:
            for num in bucket:
                if num_results == k:
                    break
                results.append(num)
                num_results += 1

        return results

