iM=int(0)
iN=int(0)
k=int(0)
print("введите М")
M=int(input())
print("введите N")
N=int(input())
matrix = [[0 for _ in range(N)] for _ in range(M)] 
matrix2 = [[0 for _ in range(N+2)] for _ in range(M+2)]
while(iM<M):
    while(iN<N):
        print("введите а",iM+1,iN+1)
        matrix[iM][iN]=int(input())
        matrix2[iM+1][iN+1]=matrix[iM][iN]
        if ((iM==0) or (iN==0)):
            matrix2[iM][iN]=9999
        if ((iM==(M-1)) or (iN==(N-1))):
            matrix2[iM+2][iN+2]=9999
        iN+=1
    iM+=1
    iN=0
iM=1
iN=1

matrix2[0][N+1]=9999
matrix2[0][N]=9999
matrix2[1][N+1]=9999
matrix2[M][0]=9999
matrix2[M+1][0]=9999
matrix2[M+1][1]=9999


while (iM<(M+1)):
    while(iN<(N+1)):
        if ((matrix2[iM][iN]<matrix2[iM-1][iN-1])and(matrix2[iM][iN]<matrix2[iM-1][iN])and(matrix2[iM][iN]<matrix2[iM-1][iN+1])and(matrix2[iM][iN]<matrix2[iM][iN-1])and(matrix2[iM][iN]<matrix2[iM][iN+1])and(matrix2[iM][iN]<matrix2[iM+1][iN-1])and(matrix2[iM][iN]<matrix2[iM+1][iN])and(matrix2[iM][iN]<matrix2[iM+1][iN+1])):
            matrix[iM-1][iN-1]=0
        iN+=1
    iM+=1
    iN=0
iM=0

while (iM<M):
    print(matrix[iM])
    iM+=1

#это самая неправильная программа, по моему мнению
#но она ведь работает, а значит все хорошо)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    