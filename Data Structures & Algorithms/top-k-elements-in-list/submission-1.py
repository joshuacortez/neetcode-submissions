class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        
        freq_list = [(num,freq) for num,freq in freq_dict.items()]
        print(freq_list)
        freq_list = sorted(freq_list, key = lambda x: x[1], reverse=True)
        top_k = [x[0] for x in freq_list][:k]
        return top_k
        