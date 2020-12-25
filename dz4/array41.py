print("введите количество элементов массива")

N=int(input())
i=int(0)
m=[0]*N
summ=int(0)
summmax=int(0)
k1=int(0)
k2=int(1)

while (i<N):
    print("введите число")
    m[i]=int(input())
    i+=1
i=0
summmax=m[0]+m[1]
while(i<(N-1)):
    summ=m[i]+m[i+1]
    if (summ>summmax):
        summmax=summ
        k1=i
        k2=i+1
    i+=1
    
print("это:",m[k1]," и конечно же",m[k2])

    

