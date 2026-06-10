class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        
        for i in range(len(numbers)-1):
            for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        
        return []