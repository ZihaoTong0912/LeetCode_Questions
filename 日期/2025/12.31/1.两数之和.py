class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这道题的要求是 找到nums中的两个相加等于target的数
        # 思路是通过哈希表 然后在每次遍历中将数加入哈希表 
        # 在之后的每次遍历中计算target 减去当前函数是否在哈希表内
        # 如果在就返回这两个数，不在就返回[] 这里用了哈希表来降低
        # 查找所需的时间，因此是时间复杂度为n的算法。
        hashtable = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target - nums[i]], i]
            hashtable[nums[i]] = i
        return []