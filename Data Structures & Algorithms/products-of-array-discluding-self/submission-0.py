class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = len(nums)
        result=[0] * num

        for i in range(num):
            product = 1
            for j in range(num):
                if i == j:
                    continue
                product  *=nums[j]

            result[i] = product
        return result