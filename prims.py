"""
The first line of input contains an integer T denoting the no of test cases .
 Then T test cases follow. The first line of each test case contains two integers n,e denoting the no of 
nodes and no of edges. Then in the next line are E*3 space separated values a b w where a,b denotes
 an edge from a to b and w is the weight of the edge.
input type
2 # test case
3 3 #vertex and edges
1 2 5 2 3 3 1 3 1 
2 1
1 2 5   """
import math
def minkey(key,mstset):
    min=math.inf
    for v in range(n):
        if key[v] < min and mstset == False:
            min = key[v]
        min_index=v
    return min_index
def spanningTree(graph, n, e):
    key=[math.inf]*n
    key[0]=0
    vertex=[None]*n#to store mst nodes
    mstset=[False]*n
    vertex[0]=-1
    for i in range(n):
        u=minkey(key,mstset)
        mstset[u]=True
        for v in range(n):
            if graph[u][v] > 0 and mstset[v]==False and key[v]> graph[u][v]:
                key[v]=graph[u][v]
                vertex[v]=u
    sum=0
    # for i in range(len(vertex)):
    #     sum+=graph[i][vertex[i]]          
    # return (sum)
    print(key)
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        c=0
        for j in range(e):
            x = arr[c]-1
            y = arr[c+1]-1
            matrix[x][y] = arr[c+2]
            matrix[y][x] = arr[c+2]
            c+=3
        print(spanningTree(matrix, n, e))

