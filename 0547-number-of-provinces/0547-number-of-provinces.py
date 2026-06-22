class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*len(isConnected)
        count=0
        def dfs(node,visited):
            visited[node]=True
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    dfs(i,visited)
        for i in range(len(isConnected)):
            if  not visited[i]:
                count+=1
                dfs(i,visited)
        return count