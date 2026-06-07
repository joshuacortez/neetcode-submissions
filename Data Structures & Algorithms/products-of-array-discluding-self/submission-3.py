class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        suffixes = [1]

        current_prod = 1
        for num in nums:
            current_prod = current_prod*num
            prefixes.append(current_prod)
        
        current_prod = 1
        for num in nums[::-1]:
            current_prod = current_prod*num
            suffixes.append(current_prod)

        prefixes = prefixes[:-1]
        suffixes = suffixes[:-1][::-1]


        print(nums)
        print(nums[::-1])
        print(prefixes)
        print(suffixes)
        result = [pre*suf for pre,suf in zip(prefixes,suffixes)]
        return result