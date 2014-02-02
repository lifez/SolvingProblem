n = int(raw_input())
x = 0
y = 0
z = 0
for i in range(0, n):
    ss = raw_input().split(" ")
    x += int(ss[0])
    y += int(ss[1])
    z += int(ss[2])
print "YES" if x == 0 and y == 0 and z == 0 else "NO"c