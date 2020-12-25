print("введите количество элементов массива")

N=int(input())
i=int(0)
m=[0]*N

while (i<N):
    print("введите число")
    m[i]=int(input())
    i+=1
i-=1
print ("в обратном порядке")
while (i>-1):
    print (m[i])
    i+=-1
    

