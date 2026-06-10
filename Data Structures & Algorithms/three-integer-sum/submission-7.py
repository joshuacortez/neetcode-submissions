class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()

        nums_w_idx = [(num,i) for i,num in enumerate(nums)]
        sorted_nums = sorted(nums_w_idx, key=lambda x: x[0], reverse = False)
        
        for _k in range(len(nums)):
            target = -sorted_nums[_k][0]
            k = sorted_nums[_k][1]
            _i = 0
            _j = len(nums) - 1

            while _i < _j:
                if _i == _k:
                    _i += 1
                    continue
                if _j == _k:
                    _j -= 1
                    continue

                total = sorted_nums[_i][0] + sorted_nums[_j][0]
                if total == target:
                    i = sorted_nums[_i][1]
                    j = sorted_nums[_j][1]
                    indices = [i,j,k]
                    if len(set(indices)) == 3:
                        hash_results = [nums[i], nums[j], nums[k]]
                        hash_results = tuple(sorted(hash_results))
                        results.add(hash_results)
                    _j -= 1
                elif total < target:
                    _i += 1
                else:
                    _j -= 1
        
        results = list(results)
        return results
            