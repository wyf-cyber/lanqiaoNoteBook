# BFS
BFS算法主要有洪水填充（flood fill）和最短路径两个应用。
## 一、洪水填充算法（Flood Fill）
### 例题 1：岛屿个数（第14届省赛真题）
**题目描述：**
> 小蓝得到了一副大小为 M × N 的格子地图，可以将其视作一个只包含字符‘0’（代表海水）和 ‘1’（代表陆地）的二维数组，地图之外可以视作全部是海水，每个岛屿由在上/下/左/右四个方向上相邻的 ‘1’ 相连接而形成。\
在岛屿 A 所占据的格子中，如果可以从中选出 k 个不同的格子，使得他们的坐标能够组成一个这样的排列：$(x_0, y_0),(x_1, y_1), . . . ,(x_{k−1}, y_{k−1})，其中(x_{(i+1)\%k} , y_{(i+1)\%k}) 是由 (x_i , y_i)$ 通过上/下/左/右移动一次得来的 (0 ≤ i ≤ k − 1)，
此时这 k 个格子就构成了一个 “环”。如果另一个岛屿 B 所占据的格子全部位于这个 “环” 内部，此时我们将岛屿 B 视作是岛屿 A 的子岛屿。若 B 是 A 的子岛屿，C 又是 B 的子岛屿，那 C 也是 A 的子岛屿。
请问这个地图上共有多少个岛屿？在进行统计时不需要统计子岛屿的数目。

**解题思路：**
> 由于不需要考虑子岛屿的个数，我们只需要从海水开始直接使用BFS遍历，如果遇到海水就将其标记为已遍历，然后遍历其上下左右的邻接节点；如果遇到未遍历过的岛屿，就将岛屿个数加一，然后单独使用一次BFS遍历整个岛屿，在这一层BFS遍历中，只遍历未被检索的岛屿节点并将其标记为已遍历，由于整个外圈岛屿都已经被标记，所以就不会出现一个岛屿被当成多个岛屿的情况。\
为了简化边缘的处理，可以直接在原地图外围增加一圈海水。这样就可以确保不会出现初始节点选在某一个岛屿内部的情况。

```py
next_p = [(0,1),(1,0),(0,-1),(-1,0)]
next_q = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def search_island(x,y):
    global sea_map
    global visited
    # BFS  
    q = []
    q.append((x,y))
    while q:
        x1,y1 = q[0][0], q[0][1]
        q.pop(0)
        if visited[x1][y1]:
            continue
        # only search the island
        visited[x1][y1] = 1
        for d in next_p:
            if sea_map[x1+d[0]][y1+d[1]] == '1' and visited[x1+d[0]][y1+d[1]] == False:
                q.append((x1+d[0], y1+d[1]))

t = int(input())
sea_map = []
visited = []
for i in range(t):
    # initialize
    sea_map = []
    visited = []
    m,n = map(int, input().split())
    sea_map.append('0'*(n+2))
    for j in range(m):
        sea_map.append('0' + input() + '0')
    sea_map.append('0'*(n+2))
    visited = [[0]*(n+2) for k in range(m+2)]
    # bfs
    ans = 0
    q = []
    q.append((0,0))
    while q:
        x, y = q[0][0], q[0][1]
        q.pop(0)
        if visited[x][y]:
            continue
        # begin to visit this node
        if sea_map[x][y] == '0':
            # sea
            visited[x][y] = 1
            # push the nodes that near it into the queue
            for d in next_q:
                if  0 <= x+d[0] <= m+1 and 0 <= y+d[1] <= n+1 and visited[x+d[0]][y+d[1]] == False:
                    q.append((x+d[0], y+d[1]))
        else:
            # island
            ans += 1
            search_island(x,y)
    print(ans)
    for line in visited:
        print(line)
```
### 例题 2：最少的1（蓝桥杯第13届国赛）
**题目描述：**
> 给定1个正整数$n$，找出所有$n$的倍数中，用二进制表示法表示下1的个数最少是多少？

**输入格式：**
> 输入一行包含一个整数$n$

**输出格式：**
> 输出一行包含一个整数表示答案

**解题思路：**
> 二进制数的特殊进位方式 + 同余最短路径

**代码示例：**
```py
# 易知直接研究n的倍数的二进制进位是很难的，在进位过程中1的个数并没有明确的规律，需要绕开进位思考
# 注意到2进制数的递推有两种形式：
# 1.二进制01串末位是0，可以选择将0变为1或在末尾加1个0
# 2.二进制01串末位是1，只能在末尾加1个0
# 这个进位规则可以覆盖到所有的数，所以是一种有效的规则，尽管它在数值上不是递增的，但由于避免了进位，所以在1的个数上是不减的
# 这两种递推关系可以生成一棵树，每条边权值为1，第一个通过这种方式被找到的n的倍数拥有最少的1，题目由此变成最短路径问题，可以使用BFS解决

from collections import deque

n = int(input())
# 创建一个数组存储n取模后不同余数所对应的最短路径
# 本题所要求的就是 mindist[0]
mindist = [float('inf') for i in range(10)]
# 引入双端队列，以便体现两种迭代方式在优先级上差别
q = deque()
# 同余最短路径
q.append((1%n, 1)) # start from 1
while q:
    k,t = q.popleft()
    if mindist[k] <= t:
        # 直接舍弃，一定不是最优路径
        continue
    mindist[k] = t
    if k&1:
        # k is odd
        q.appendleft(((k*2)%n, t))
    else:
        q.appendleft(((k*2)%n, t))
        q.append(((k+1)%n, t+1))
print(mindist[0])
```
