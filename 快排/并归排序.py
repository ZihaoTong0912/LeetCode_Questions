import random

# 这里采用的是并归排序，主要原理是分治，也就是先将数组全部分成
# n等分，然后再通过merge来合并。 merge的原理就是依次拿两个数组
# 中的数来比较，然后将排序后的数组合并 
        # Merge排序并合并左右两个数组。
def merge(left,right):
    i = 0
    j = 0
    output = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output
        # merge_sort先将数组不断分成左右两部分，然后再进行合并。
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


# 生成一个包含 10000 个 1~100000 之间的随机整数的数组
large_array = [random.randint(1, 100000) for _ in range(10000)]
sorted_array = sorted(large_array)
# 测试
output = merge_sort(large_array)
print(output == sorted_array)