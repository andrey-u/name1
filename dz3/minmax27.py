print("введите количество элементов")

N=int(input())
i=int(0)
m=[0]*N
k=int(1)
kmax=int(1)
chislo=int(0)
nachposled=int(0)

while (i<N):
    print("введите число")
    m[i]=int(input())
    if (i!=0):
        
        if(m[i]==m[i-1]):
            k+=1
            if (k>kmax):
                kmax=k
                nachposled=i-k+2

        if(m[i]!=m[i-1]):
            k=1
    
    i+=1

print("наибольшая последовательность начинается на элементе:",nachposled,"  количество:",kmax)