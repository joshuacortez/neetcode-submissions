class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i_max_jump = 0
        max_jump = 0

        for i, num in enumerate(nums):
            n_steps = i - i_max_jump 
            if num > 0:
                print(f"Current num {num}")
                print(f"Current max jump {max_jump}")
                print(f"N Steps since max jump {n_steps}")
                print(f"Candidate {num} compared to max_jump {max_jump} that is effectively {max_jump - n_steps}")
            
                if num > max_jump - n_steps:
                    max_jump = num
                    i_max_jump = i
                    print(f"New max_jump {max_jump} with idx {i_max_jump}\n")
                else:
                    print(f"Keeping max_jump {max_jump} from idx {i_max_jump}\n")
         
            if num == 0:
                print(f"Current num {0}")
                print(f"It will consume {n_steps} from {max_jump}\n")
                current_jump = max_jump - n_steps
              
                if i + current_jump == len(nums) - 1:
                    return True
                if current_jump <= 0:
                    return False


        return True