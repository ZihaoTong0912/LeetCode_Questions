import random

# 生成一个包含 10000 个 1~100000 之间的随机整数的数组
large_array = [random.randint(1, 100000) for _ in range(10000)]
sorted_array = sorted(large_array)
# 这段是通过一个哨兵节点来讲数从一个节点分成两组
# 我们选取最左边的数作为哨兵节点，然后依次从两端
# 寻找。 指针j用来寻找小于该节点的数，i用来寻找
# 大于该节点的数 当找到时交换两数 然后继续寻找
# 直到i=j。 这里先从使用j来寻找的原因是为了确保
# 当i=j时 两个指针指到的数一定小于哨兵节点 因此
# 就可以保证最后 i l 的交换是成立的。
def partition(nums,l,r):
    i,j = l,r
    while i < j:
        while i < j and nums[j] >= nums[l]:
            j -= 1
        while i < j and nums[i] <= nums[l]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i],nums[l] = nums[l],nums[i]

    return i
# 这个就是通过递归来对左右两边的列表进行交换。
def quick_sort(nums,l,r):
    if l >= r:
        return 
    i = partition(nums,l,r)
    quick_sort(nums,l,i-1)
    quick_sort(nums,i+1,r)
# 测试
quick_sort(large_array, 0, len(large_array) - 1)
print(large_array == sorted_array)