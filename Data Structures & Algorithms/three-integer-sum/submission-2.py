class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # Skip duplicates for the first element
            if i > 0 and a == nums[i-1]:
                continue
                
            # FIX 1 & 2: Corrected the string subtraction and the loop condition
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    # FIX 3: Placed the boundary check first to prevent IndexErrors
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return result