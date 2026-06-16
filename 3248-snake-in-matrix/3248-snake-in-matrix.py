class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        a=0
        for i in range(len(commands)):
            if commands[i]=="RIGHT":
                a=a+1
            elif commands[i]=="DOWN":
                a=a+n
            elif commands[i]=="UP":
                a=a-n
            else:
                a=a-1
        return a
        
        