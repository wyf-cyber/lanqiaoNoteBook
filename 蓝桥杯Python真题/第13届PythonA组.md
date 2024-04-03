# 第13届Python A组
## 试题A：裁纸刀（5分）
**题目描述：**
> 本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。\
小蓝有一个裁纸刀，每次可以将一张纸沿一条直线裁成两半。小蓝用一张纸打印出两行三列共 6 个二维码，至少使用九次裁出来。如果小蓝要用一张纸打印出 20 行 22 列共 440 个二维码，他至少需要裁多少次？

**代码示例：**
```py
# 观察到如果要让总裁剪次数最小，应当尽可能让裁剪的线条最长
# 由此，我们先沿与较长边平行的方向剪裁，然后沿列逐个剪下即可
# 总次数 = 4 + 19 + 20*21 = 443
ans = 4+19+21*20
print(ans)
```

## 试题B：寻找整数（5分）
**题目描述：**
> 有一个不超过 $10^{17}$ 的正整数 $n$，n，已知这个数除以 2 至 49 后的余数如下表所示，求这个正整数最小是多少。
![alt text](image.png)

**代码示例：**
```py
'''
# 首先注意到这个数是11和17的公倍数，由于11和17都是素数，所以这个数一定是11*17的倍数，搜索步长为187
# 但数据量过大，当前步长仍然过小，会造成超时，需要进一步找出更大的搜索步长
getM = [0,0,1,2,1,4,5,4,1,2,9,0,5,10,11,14,9,0,11,18,9,11,11,15,17,9,23,20,25,16,29,27,25,11,17,4,29,22,37,23,9,1,11,11,33,29,15,5,41,46]
# 先取最后几个较大的除数进行筛选，筛选出两个符合条件的数以后这两个数的差值就是更大的步长，只有满足这个步长的数才能满足后几个除数的条件
num = [] # 存储符合条件的数
LIMIT = 10**17
for i in range(187, LIMIT, 187):
    # check i 
    isvalid = True
    for j in range(44,50):
        if i%j != getM[j]:
            isvalid = False
            break
    if isvalid:
        num.append(i)
        if len(num) > 1:
            break
d = num[1] - num[0]
# use new step to search the result
for i in range(num[0],LIMIT,d):
    isValid = True
    for j in range(2,44):
        if i%j != getM[j]:
            isValid = False
            break
    if isValid:
        print(i)
        break
'''
print(2022040920220409) # 程序运算时间过长，直接在本地编译器上运行后打印结果
```

## 试题C：质因数的个数（10分）
**题目描述：**
> 给定正整数 n，请问有多少个质数是 n 的约数

**输入格式：**
> 输入一行，包含一个整数 n

**输出格式：**
> 输出一个整数，表示答案

**代码示例：**
```py
'''
# 可以直接从2开始逐个试除，但考虑到数据量很大，估计只能过60%
# 线性筛的模板题
# 先用线性筛打表，然后逐个试除
def sieve(n):
    is_prime = [True]*(n+1)
    prime = []
    for i in range(2,n+1):
        if is_prime[i]:
            prime.append(i)
        for j in prime:
            if i*j > n:
                break
            is_prime[i*j] = False
            if i%j == 0:
                break
    return prime

print(sieve(10**8))
'''
def sieve(n):
    prime = []
    is_prime = [True]*(n+1)
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            m = 2
            temp = m*i
            while temp <= n:
                is_prime[temp] = False
                temp += i 
    return prime

prime = sieve(100000000)
n = int(input())
ans = 0
for i in prime:
    if i > n:
        break
    isValid = False
    while n%i == 0:
        isValid = True
        n //= i
    if isValid:
        ans += 1
if n > 2:
    ans += 1
print(ans)
```
```py
# 只能过80%的测试样例
n = int(input())
ans=0
i=2
while i*i<=n:
    if n%i==0:
        ans+=1
        while n%i==0:
            n=n//i
    i+=1
if n>1:
    ans+=1
print(ans)
```

## 试题 D:矩形拼接
**题目描述：**
> 已知 3 个矩形的大小依次是 $a_1×b_1,a_2×b_2,a_3×b_3$ 。用这 3 个矩形能拼出的所有多边形中, 边数最少可以是多少?

**输入格式：**
> 输入包含多组数据。第一行包含一个整数 T, 代表数据组数。以下 T 行, 每行包含 6 个整数 $a_1,b_1,a_2,b_2,a_3,b_3$ 其中 $a_1,b_1$ 是第一个矩形的长和宽，$a_2,b_2$ 是第二个矩形的长和宽,$a_3,b_3$ 是第三个矩形的长和宽。

**输出格式：**
> 对于每组数据, 输出一个整数代表答案。

**代码示例：**
```py
# 经过分析，拼接后矩形一共有4，6，8三种边数，其中8条边的情况最多，所以使用排除法，判断是否是4条边或6条边，如果均不是就输出8
# 4条边的情况
# 三个矩形均有一边相等
# 两个矩形一遍相等且另一边的和是第三个矩形的某一边的边长
t = int(input())
def check6(a,b,c):
    if a+b==c or a+c==b or b+c==a:
        return True
    elif a==b or a==c or b ==c:
        return True
    else:
        return False
def check4(a1,b1,a2,b2,a3,b3):
    for i in [a1,b1]:
        if i == a2+a3 and b2 == b3:
            return True
        elif i == a2 + b3 and b2 == a3:
            return True
        elif i == b2 + a3 and a2 ==b3:
            return True
        elif i == b2 + b3 and a2 == a3:
            return True
        elif i ==a2 and a2 ==a3:#三条边相等,4种
            return True
        elif i ==a2 and a2 ==b3:
            return True
        elif i ==b2 and b2 == a3:
            return True
        elif i == b2 and b2 == b3:
            return True

for i in range(t):
    s = list(map(int,input().split()))
    ans = 8
    #因为边数有3种情况:
    # 4（完美，有两边加起来等于另一边，另一边刚好相等)
    # 6（有两边加起来等于另一边)
    # 8（每个边都不等，任意两边加起来也不等第三边)
    a1,b1,a2,b2,a3,b3 = s[0],s[1],s[2],s[3],s[4],s[5]
    for i in range(0,2):
        for j in range(2,4):
            for k in range(4,6):
                x1,x2,x3 = s[i],s[j],s[k]
                if check6(x1,x2,x3):
                    ans = min(6,ans)
                if check4(a1,b1,a2,b2,a3,b3):
                    ans = min(4,ans)
                if check4(a2,b2,a1,b1,a3,b3):
                    ans = min(4,ans)
                if check4(a3,b3,a1,b1,a2,b2):
                    ans = min(4,ans)
    print(ans)
```
## 试题 E：消除游戏
**题目描述：**
> 在一个字符串 $S$ 中，如果 $S_i = S_{i−1}$ 且 $S_i \neq S_{n+1}$ ，则称 $S_i$ 和 $S_{i+1}$ 为边缘字符。如果且 $S_i = S_{i+1}$，则 $S_{i−1}$ 和 $S_i$ 也称为边缘字符。其它的字符都不是边缘字符。\
对于一个给定的串 $S$，一次操作可以一次性删除该串中的所有边缘字符（操作后可能产生新的边缘字符）。\
请问经过 $2^{64}$ 次操作后，字符串 S 变成了怎样的字符串，如果结果为空则输出 EMPTY。 

**输入格式：**
> 输入一行包含一个字符串 S 。

**输出格式：**
> 输出一行包含一个字符串表示答案，如果结果为空则输出 EMPTY。

**解题思路：**\
在删除一对边缘字符后，会产生新的相邻组合，这个新的相邻组合也有可能是边缘字符，所以需要重复操作，但是

**代码示例：**
```py
from copy import copy
# 暴力算法
# 可以通过58%的测试样例
LIMIT = 1 << 64
def f(s):
    # 进行一轮删除操作
    deleted = set() # 创建一个集合储存本轮所有应当被删除的节点的下标
    for i in range(1,len(s)-1):
        # 注意两边特殊处理
        if s[i-1] != s[i] and s[i] == s[i+1]:
            deleted.add(i-1)
            deleted.add(i)
        elif s[i-1] == s[i] and s[i] != s[i+1]:
            deleted.add(i)
            deleted.add(i+1)
    # 按照deleted数组重新生成一个字符串，比执行多次删除操作更快
    next_s = ''
    for i in range(len(s)):
        if i in deleted:
            continue
        next_s += s[i]
    return next_s

s = input()
flag = True
for i in range(LIMIT):
    pre = copy(s)
    s = f(s)
    if s == '':
        print('EMPTY')
        flag = False
        break
    elif s == pre:
        # 所有边缘字符均被删除，直接结束程序
        print(s)
        flag = False
        break
if flag:
    print(s)
```

```py
def remove(index):
    # delete the specialized node
    global left,right,deleted
    if deleted[index]:
        return 
    right[left[index]] = right[index]
    left[right[index]] = left[index]
    deleted[index] = True
    return 

# 为原字符串前后添加两个不可能出现在原字符串中的字符，这两个字符不会被判定为边缘字符，也不会被删除
# 存在的意义是为了避免开头结尾的特殊讨论，直接生成链表的头尾节点
s = '@' + input() + '@'
n = len(s)
# 创建一个列表存储所有元素的右指针
right = [i+1 for i in range(n)]
left = [i-1 for i in range(n)]
right[n-1] = -1
# 因为循环的次数很多，所以最终一定不会存在边缘字符，只需不断循环直到不存在边缘字符就可以
deleted = [False]*n # record whether the element has been deleted or not
modify = True
while modify:
    modify = False
    # 应用链表查询整个字符串，检查是否存在边缘字符，如果不存在边缘字符
    cur = right[0]
    need_delete = [] # store all of the index that belong to the node,which should be delete
    # search  
    while cur != -1:
        cur = right[cur]
        if cur == -1:
            # 只剩下1个元素了
            break
        if s[left[cur]] != s[cur] and s[cur] == s[right[cur]]:
            if s[left[cur]] != '@':
                # can't delete the head node
                # delete the cur and left[cur]
                need_delete.append(left[cur])
                need_delete.append(cur) 
        elif s[left[cur]] == s[cur] and s[cur] != s[right[cur]]:
            if s[right[cur]] != '@':
                # can't delete the rear node
                # delete cur and right[cur]
                need_delete.append(cur)
                need_delete.append(right[cur])
    # delete
    if need_delete:
        # the list is not empty
        modify = True
        for i in need_delete:
            remove(i)
# print answer
p = right[0]
if p == -1:
    print('EMPTY')
else:
    while p != -1:
        print(s[p], end = '')
        p = right[p]
```


## 试题 F：重新排序
**题目描述：**
> 给定一个数组 $A$ 和一些查询 $L_i , R_i$，求数组中第 $L_i$ 至第 $R_i$ 个元素之和。小蓝觉得这个问题很无聊，于是他想重新排列一下数组，使得最终每个查询结果的和尽可能地大。小蓝想知道相比原数组，所有查询结果的总和最多可以增加多少?

**输入格式：**
> 输入第一行包含一个整数 n。\
第二行包含 n 个整数 $A_1, A_2, · · · , A_n$，相邻两个整数之间用一个空格分隔。\
第三行包含一个整数 $m$ 表示查询的数目。\
接下来 $m$ 行，每行包含两个整数 $L_i、R_i$ ，相邻两个整数之间用一个空格分隔。

**输出格式：**
> 输出一行包含一个整数表示答案。

**解题思路：**\
看到求区间的和，想到前缀和与差分算法。然后想如何才能使区间和最大，注意到将会读取多个区间的和，这些区间可能会出现重叠，为了让读取的结果尽可能地大，我们应当确保一个元素被读取的次数越多，它的值越大。根据这个思路，我们可以先利用差分数组统计每一个元素被读取的次数，然后将原数组和读取次数的数组分别从大到小排序，然后将两个数组中下标相同的元素的乘积累加，所得结果就是最大所能达到的元素和。

**代码示例：**
```py
n = int(input())
num = [int(i) for i in input().split()]
# 建立差分数组记录每一个元素被统计的次数
d = [0 for i in range(n+2)]
m = int(input())
for i in range(m):
    l,r = map(int,input().split())
    d[l] += 1
    d[r+1] -= 1
# 根据差分数组计算出被统计的次数
times = [0]*(n+1)
times[0] = d[0]
for i in range(1,n+1):
    times[i] = times[i-1] + d[i]
del times[0]
# 先计算出原结果
ans_one = 0
for i in range(n):
    ans_one += times[i]*num[i]
# 排序然后计算出最大结果
ans_two = 0
times.sort(reverse = True)
num.sort(reverse = True)
for i in range(n):
    if times[i] == 0:
        break
    ans_two += times[i]*num[i]
print(ans_two - ans_one)
```

