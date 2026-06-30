class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        max_arr = [curr_max]
        for num in arr[::-1]:
            if num > curr_max:
                curr_max = num
            max_arr.append(curr_max)

        result = max_arr[::-1][1:]
        return result