# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        results = []

        for i in range(n):
            j = i - 1
            while j >= 0:
                if pairs[j+1].key < pairs[j].key:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1

            print([(pair.key, pair.value) for pair in pairs])
            current_state = [(Pair(pair.key, pair.value)) for pair in pairs]
            results.append(current_state)
        return results
            

        


        
        