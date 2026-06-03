class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        
        buckets = [[] for i in range(len(nums)+1)]
        
        for num, freq in freq_dict.items():
            print(buckets, freq)
            buckets[freq].append(num)

        results = []
        i = len(nums) 
        while len(results) < k:
            latest = buckets[i]
            for num in latest:
                results.append(num)
                if len(results) == k:
                    break
            i -= 1
        return results
        