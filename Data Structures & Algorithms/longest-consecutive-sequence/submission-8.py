class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen_nums = set(nums)

        # this stores key (start of sequence), val (all belonging to that sequence)
        sequence_dict = {}

        # first pass to get all seed values
        # seed values are those whose predecessor doesnt exist in list
        for num in nums:
            if num-1 not in seen_nums:
                # candidate for new sequence
                if num not in sequence_dict.keys():
                    sequence_dict[num] = 1
        
        # second pass to count all consecutive
        for seed in sequence_dict.keys():
            i = 1
            while (seed + i) in seen_nums:
                sequence_dict[seed] += 1
                i+=1
        
        print(sequence_dict)
        return max(list(sequence_dict.values()))
        



