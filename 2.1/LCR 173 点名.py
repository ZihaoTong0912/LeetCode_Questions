class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        i = 0
        j = len(records)-1
        while i <= j:
            m = (i+j) // 2
            if m == records[m]:
                i = m+1
            else:
                j = m-1
        return i