class Solution:
    def reversePairs(self, record: List[int]) -> int:
        global number
        number = 0
        x = 0
        def merge(left, right):
            global number
            i = 0
            j = 0
            output = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    number += len(left) - i
                    j += 1
            output.extend(left[i:])
            output.extend(right[j:])
            return output
        def fun(arr):
            if len(arr) <=1:
                return arr
            mid = len(arr) // 2
            left = fun(arr[:mid])
            right = fun(arr[mid:])
            return merge(left,right)
        sorted_1 = fun(record)
        return number

