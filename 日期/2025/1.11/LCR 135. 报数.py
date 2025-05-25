class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        output = []
        i = 1
        while len(str(i)) <= cnt:
            i +=1
        for i in range(1, i):
            output.append(i)
        return output