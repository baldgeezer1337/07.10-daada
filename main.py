f=open('in.txt', 'r')
for s in f:
    print(s,end='')
    f.close()

f=open('in.txt', 'r')
ss=f.readlines()
print(ss)
f.close

f=open('out.txt','w')
print('this is', file=f)
f.close()