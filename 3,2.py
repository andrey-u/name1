def kpoTuk(x):
    if (x[0]<=0): open('result2.txt','w').write('-'+str(x[0]))
    if ((x[0]>0)&(x[0]<2)): 
        x[0]=x[0]*x[0]
        open('result2.txt','w').write(str(x[0]))
    if (x[0]>=2): open('result2.txt','w').write('4')
#if26
x = list(map(int, open('data2.txt','r').read().split()))
kpoTuk(x)
