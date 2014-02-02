name = raw_input()
count = len(''.join(set(name)))
if count%2==0:print "CHAT WITH HER!"
else:print "IGNORE HIM!"