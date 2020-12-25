iM=int(0)
iN=int(0)
k=int(0)
print("введите М")
M=int(input())
print("введите N")
N=int(input())
matrix = [[0 for _ in range(N)] for _ in range(M)] 
while(iM<M):
    while(iN<N):
        print("введите а",iM+1,iN+1)
        matrix[iM][iN]=int(input())
        iN+=1
    iM+=1
    iN=0
iM=1

while(iM<M):
    if (matrix[iM]==matrix[0]): k+=1
    iM+=1
print("похожих строк:",k)
    

