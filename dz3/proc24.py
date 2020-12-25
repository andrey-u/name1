chet=0
def Even(K):
    global chet
    if (K%2==0):
        chet+=1
        print("True")
    if (K%2==1):
        print("False")
i=int(0)
while (i<10):
    print ("введите число:",i+1,"/10")
    k=int(input())
    Even(k)
    i+=1
    if (i==10):
        print("четных:",chet,"нечетных:",i-chet)
