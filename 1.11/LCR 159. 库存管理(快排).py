class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:

        def fun(stock, l, r):
            if l >= r:
                return 
            i,j = l, r 
            while i < j:
                while i < j and stock[j] >= stock[l]:
                    j -= 1
                while i < j and stock[i] <= stock[l]:
                    i += 1
                stock[i], stock[j] = stock[j], stock[i]
            stock[l], stock[i] = stock[i], stock[l]
            fun(stock, l, i-1)
            fun(stock, i+1, r)
        fun(stock, 0, len(stock)-1)
        output = []
        for i in range(cnt):
            output.append(stock[i])
        return output