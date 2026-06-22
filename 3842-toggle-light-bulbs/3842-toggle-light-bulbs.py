class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        r=[]
        bulbs.sort()
        for i in bulbs:
            if bulbs.count(i)%2!=0 and i not in r:
                r.append(i)
        return r

        

        