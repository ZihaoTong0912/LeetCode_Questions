class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        places.sort()
        number = places.count(0)

        for i in range(4):
            if places[i] != 0 and places[i] == places[i+1]:
                return False
        return places[4] - places[number] < 5