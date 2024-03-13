def getTime(s):
    month = int(s[5:7])
    day = int(s[8:10])
    h = int(s[11:13])
    m = int(s[14:16])
    s = int(s[17:19])
    return (month,day,h,m,s)

t = []
f = open('D:\Algorithm\PythonExercise\source.txt')
for line in f:
    t.append(getTime(line))
t.sort()
isB = 1
pre = 0
ans = 0
for i in t:
    if isB:
        pre = (i[2]*60 + i[3])*60 + i[4]
        isB = 0
    else:
        ans += ((i[2]*60 + i[3])*60 + i[4] - pre)
        isB = 1
print(ans)