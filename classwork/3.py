
def inpud():
    x = list(map(int, open('data1.txt','r').read().split()))
    return (x)

#if5 через фóнкцию
pol=int(0)
nol=int(0)
otr=int(0)
i=int(0)
while (i<3):
    chislo=inpud()
    if (chislo[i]<0):otr+=1
    if (chislo[i]>0):pol+=1
    if (chislo[i]==0):nol+=1
    i+=1
open('result1.txt','w').write('положительных:'+ str(pol) + '\n' + 'отительнх:'+ str(otr) +'\n' + 'нyлей:'+ str(nol))
