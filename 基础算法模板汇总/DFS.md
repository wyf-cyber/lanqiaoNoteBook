# DFS
> 蓝桥杯中的DFS主要有针对分配过程的DFS和图/树的DFS两种类型，基本是模板题，难度中等
## 类型一：针对分配过程的DFS
### 例题 1：飞机降落
**题目描述：**
> N 架飞机准备降落到某个只有一条跑道的机场。其中第 i 架飞机在 $T_i$ 时刻到达机场上空，到达时它的剩余油料还可以继续盘旋 $D_i$ 个单位时间，即它最早可以于 $T_i$ 时刻开始降落，最晚可以于 $T_i + D_i$ 时刻降落。降落过程需要 $L_i$ 个单位时间。\
一架飞机降落完毕时，另一架飞机可以立即在同一时刻开始降落，但是不能在前一架飞机完成降落前开始降落。请判断n架飞机是否能够全部安全降落。

**输入格式：**
> 输入包含多组数据，第一行包含一个整数 $T$，表示测试数据的组数。
对于每组数据，第一行包含一个整数N
以下 N 行，每行包含三个整数：$T_i,D_i,L_i$

**输出格式：**
> 对于每组数据，输出 $YES$ 或者 $NO$，代表是否可以全部安全降落。

**代码示例：**
```py
from sys import setrecursionlimit
setrecursionlimit(10000)

def dfs(flight, landed, amount, cur_time, pre_lander):
    if pre_lander == amount:
        # all of the flights have already landed
        return True
    # choose the current flight
    for i in range(amount):
        if landed[i]:
            continue
        # hasn't landed yet
        if flight[i][1] < cur_time:
            # the fuel have run out, this schedule is wrong
            return False
        # it can land 
        landed[i] = True
        if dfs(flight, landed, amount, max(cur_time, flight[i][0])+flight[i][2],pre_lander+1):
            return True
        else:
            # try again
            landed[i] = False
    # no suitable answer
    return False

times = int(input())
for _ in range(times):
    n = int(input())
    flight = []
    for i in range(n):
        # create a list to record the earliest and latest time that every flight can land
        a,b,c = map(int, input().split())
        flight.append(a,a+b,c)
    landed = [False]*n
    if dfs(flight, landed, n, 0, 0):
        print('YES')
    else:
        print('NO')
```

### 例题 2：分糖果
**问题描述:**
> 两种糖果分别有9个和16个，要全部分给7个小朋友，每个小朋友得到的糖果总数最少为2个最多为5个，问有多少种不同的分法，糖果必须全部分完。如果有其中一个小朋友在两种方案中分到的糖果不完全相同，这两种方案就算作不同的方案。

**答案提交:**
> 这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只输出这个整数，输出多余的内容将无法得分。

**题目答案：**
> 35813063

**要点：**
> 注意递归处理的子问题是单个小朋友的分配问题，不是某一颗糖的分配问题，因为糖会出现重复，无法去重

**代码示例：**
```py
# 核心是去重
def dfs(cur,a,b):
    global cnt
    # start from 1
    if cur >= 8:
        # every child has gotten his candy
        # check whether all of the candy have been given away
        if a == 0 and b == 0:
            cnt += 1
        return
    # use for loops to avoid repeatly count
    for i in range(a+1):
        for j in range(b+1):
            if 2 <= i+j <= 5:
                dfs(cur+1, a-i, b-j)
cnt = 0
# dfs(1,9,16)
print(5067671)
```

## 类型二：树的DFS
### 例题 1：景区导游
> 题目链接：[景区导游（蓝桥杯）](https://www.lanqiao.cn/problems/3516/learning/?page=36&first_category_id=1&second_category_id=3)

**题目要求：**\
某景区一共有 N 个景点，编号 1 到 N。景点之间共有 N − 1 条双向的摆渡车线路相连，形成一棵树状结构。在景点之间往返只能通过这些摆渡车进行，需要花费一定的时间。\
小明是这个景区的资深导游，他每天都要按固定顺序带客人游览其中 K 个景点：$A_1, A_2, . . . , A_K$。今天由于时间原因，小明决定跳过其中一个景点，只带游客按顺序游览其中 K − 1 个景点。具体来说，如果小明选择跳过 Ai，那么他会按顺序带游客游览 $A_1, A_2, . . . , A_{i−1}, A_{i+1}, . . . , A_k, (1 ≤ i ≤ K)$。\
请你对任意一个 $A_i$，计算如果跳过这个景点，小明需要花费多少时间在景点之间的摆渡车上？

**输入格式:**
> 第一行包含 2 个整数 N 和 K。以下 N − 1 行，每行包含 3 个整数 u, v 和 t，代表景点 u 和 v 之间有摆渡车线路，花费 t 个单位时间。最后一行包含 K 个整数 $A_1, A_2, . . . , A_k$ 代表原定游览线路。

**输出格式:**
> 输出 K 个整数，其中第 i 个代表跳过 $A_i$ 之后，花费在摆渡车上的时间。

**提示:**
> 对于 20% 的数据，$2 ≤ K ≤ N ≤ 10^2$。\
对于 40% 的数据，$2 ≤ K ≤ N ≤ 10^4$。\
对于 100% 的数据，$2 ≤ K ≤ N ≤ 10^5，1 ≤ u, v, A_i ≤ N，1 ≤ t ≤ 10^5$。保证 $A_i$ 两两不同。

**代码示例：**
```py
from sys import setrecursionlimit
setrecursionlimit(100010)
def dfs(start,end,cur,pre,totalCost):
    global length
    global u
    global v
    global t
    if cur == end:
        return totalCost
    # 用for循环遍历邻接节点
    for i in range(length):
        if v[i] == pre:
            continue
        if u[i] == cur:
            temp = dfs(start,end,v[i],cur,totalCost+t[i])
            if temp > 0:
                return temp
    return 0

n,k = map(int,input().split())
u = []
v = []
t = []
for i in range(n-1):
    u1,v1,t1 = map(int,input().split())
    u.append(u1)
    v.append(v1)
    t.append(t1)
    u.append(v1)
    v.append(u1)
    t.append(t1)
length = (n-1)*2 # 邻接三元组的长度
path = [int(i) for i in input().split()]
# 算出总代价
s = 0
temp = [0]*(k-1)
for i in range(1,k):
    temp[i-1] = dfs(path[i-1],path[i],path[i-1],-1,0)
    s += temp[i-1]
print(s-temp[0],end = ' ')
# 中间部分
for i in range(1,k-1):
    print(s-temp[i-1]-temp[i]+dfs(path[i-1],path[i+1],path[i-1],-1,0),end = ' ')
print(s-temp[k-2],end = ' ')
```
