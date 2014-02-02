n = input()
s = ''
for i in xrange(n):
    s += raw_input()
ans = 1
for i in xrange(len(s) - 1):
    if s[i] == s[i+1]: ans+=1
print ans