
HoMeP_ZaDaHuA=int(1)
while ((HoMeP_ZaDaHuA>0)&(HoMeP_ZaDaHuA!=10)):
    print ("1-if5; 2-if26; 3-for11; 4-for2; 5-while25; 6-while13; 7-series35; 8-series33, 9-ничего; 10-выход")
    HoMeP_ZaDaHuA=int(input("введите номер задания:"))
    if (HoMeP_ZaDaHuA==1):
        print("выбрана программа if5, выводит сколько полож. и отр. чисел (из трех), +от меня количесто нулей")
        pol=int(0)
        nol=int(0)
        otr=int(0)
        i=int(0)
        while (i<3):
            i+=1
            chislo=int(input("введите число:"))
            if (chislo<0): otr+=1
            if (chislo>0): pol+=1
            if (chislo==0): nol+=1
        print ("положительных:", pol)
        print ("отрицетальных:", otr)
        print ("нулей:", nol)
    if (HoMeP_ZaDaHuA==2):
        print("выбрана программа if26, сложное описание пропущено...")
        x=float(input("введите х:"))
        if (x<=0): print(-x)
        if ((x>0)&(x<2)): print(x*x)
        if (x>=2):  print("4")
    if (HoMeP_ZaDaHuA==3):
        print("выбрана программа for11, опять сложное(лень писать) описание...")
        i=int(0)
        N=int(input("введите N:"))
        summ=(N**2)
        for i in range(N):
            i+=1
            summ+=((N+i)**2)
        print("получилось:", summ)
    if (HoMeP_ZaDaHuA==4):
        print("выбрана программа for2, вывести числа от меньш. к больш. +их кол-во")
        A=int(input("введите меньшее число:"))
        B=int(input("введите большее число:"))
        N=int(B-A+1)
        i=int(0)
        for i in range(B-A+1):
            print (A+i)
            i+=1
        print("всего получилось чисел:",N)
    if (HoMeP_ZaDaHuA==5):
        print('выбрана программа while25, найти первое число Фибоначчи, большее N')
        F3=int(2)
        F2=int(1)
        F1=int(1)
        N=int(input("введите N:"))
        while(F3<=N):
            F1=F2
            F2=F3
            F3=(F1+F2)
        print(F3)
    if (HoMeP_ZaDaHuA==6):
        print("выбрана программа while13, выводит какое-то число и сумму")
        A=float(input("введите А>1:"))
        K=int(1)
        summ=float(1)
        while (summ<=A):
            K+=1
            summ+=(1/K)
        print("K =", K)
        print("сумма =", summ)
    if (HoMeP_ZaDaHuA==7):
        print("выбрана программа series35, какое-то К, наборы с К, очень интересно, спасибо") 
        K=int(input("введите К:"))
        i=int(1)
        elem_B=int(0)
        m=[0]*K
        while (i<=K):
            i+=1
            print("след.массив")
            x=int(input("введите число (0-заканчивает):"))
            while (x!=0):
                elem_B+=1
                m[i-2]+=1
                x=int(input("введите число (0-заканчивает):"))
        i=0
        while(i<K):
            print("в наборе", i+1, "количество элементов:" , m[i])
            i+=1
        print("всего элементов:", elem_B)
    if (HoMeP_ZaDaHuA==8):
        print("выбрана программа series33, я устал писать")
        K=int(input("введите К:"))
        N=int(input("введите N:"))
        i=int(1)
        j=int(1)
        aaaaaaaa=int(0)
        while (i<=K):
            aaaaaaaa=0
            i+=1
            j=1
            print("след.массив")
            x=int(input("введите число:"))
            if (x==2): 
                aaaaaaaa=1 
            while (j<N):
                j+=1
                x=int(input("введите число:"))
                if (x==2): 
                    aaaaaaaa=j
            if (aaaaaaaa>0):        
                print("последняя двойка находится на месте:",aaaaaaaa)
            else:
                print("тут двоек нет! держите '0', как просится в условии")
    if (HoMeP_ZaDaHuA==10):
        print("спасибо, что проверили мою работу, досвиданья!")
    if (HoMeP_ZaDaHuA>10):
        print("тут всего 8 заданий, выбранное отсутствует") #как и мой креатив после 8ми заданий
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    