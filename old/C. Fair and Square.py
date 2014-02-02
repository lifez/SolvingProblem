from math import sqrt
import string, sys,operator
input_file = open('C-large-22.in')
output_file = open('output.out','r+')
def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step
def is_square_palindome(x):
    y = sqrt(x)
    if y%1==0:
        yrev = str(int(y))
    else:
        yrev = str(y)
    if x<10:
        return y%1==0
    else:
        xrev = str(int(x))
        return yrev==yrev[::-1] and  xrev==xrev[::-1]

for case in myxrange(int(input_file.readline())):
    count =0
    A,B= map(int,input_file.readline().split(" "))
    for i in myxrange(A,B):
        if is_square_palindome(i):
            count+=1
    output_file.write("Case #{0}: {1}\n".format(case+1,count))
input_file.closed()
output_file.closed()


