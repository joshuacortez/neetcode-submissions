class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        
        i = 0
        j = 1
        while not ((i == len(numbers) - 1) and (j == len(numbers) - 1)):
            if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                if j <= len(numbers) - 2:
                    j += 1
                else:
                    i += 1
            else:
                if j >= i + 1:
                    j -= 1
                    i += 1
                else:
                    i -= 1
        
        return []
        