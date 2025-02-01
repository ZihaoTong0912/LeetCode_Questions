class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        def search(target):
            i = 0
            j = len(scores) - 1
            while i <= j:
                m = (i+j) // 2
                if target >= scores[m]:
                    i = m +1
                else:
                    j = m - 1
            return i
        return search(target)- search(target-1) 