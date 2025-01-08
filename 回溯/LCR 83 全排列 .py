class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def fun(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                fun(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
        
        res = []
        n = len(nums)
        fun(0)
        return res