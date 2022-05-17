from copy import deepcopy
from operator import index
import pack1 as PK
##### st0  st1   st2  end
TM1=[[0.1, 0.8, 0.1,   0],#start
     [0.3, 0.3, 0.3, 0.1],#st0
     [0.2, 0.2, 0.5, 0.1],#st1
     [0.7, 0.1, 0.1, 0.1]]#st2
EM1=[[0.9, 0.1],#st0
     [0.7, 0.3],#st1
     [0.3, 0.7]]#st2
##### ob0  ob1
states=["rainy","cloudy","sunny"]
observables=["umbrella","null"]
obSeq1=["umbrella","umbrella","null","umbrella","umbrella","null"]
######## t0         t1         t2     t3         t4         t5        total=6
def alpha(i,t,obSeq1):
    PK.saveStates(states)
    PK.saveObservations(observables)
    PK.saveTMatrix(TM1)
    PK.saveEMatrix(EM1)
    viterbiM=PK.scoringSolo(obSeq1)[1]
    alph= viterbiM[i][t]
    #if t == len(obSeq1)-1:
        #alph*= TM1[i+1][-1]  #we bring in the termination at alpha not at A &&&&&&&&&&&&&&&&&&&&&&&
    return alph
def beta(i,t,obSeq1): 
    TM=deepcopy(TM1)
    row0=TM[0].copy()
    for x in range(len(TM1)-1):
        TM[0][x]=deepcopy(TM1)[x+1][len(TM1)-1]  #changed TM to deepcopy(TM1) no diff
        #TM[x+1][len(TM)-1]=row0[x] #new TM start is not used.this line will not make a diff
    TMM=deepcopy(TM)
    for x in range(1,len(TM1)):
        for y in range(len(TM1)-1):
            TM[x][y]=deepcopy(TMM)[y+1][x-1]
    obSeq=list(obSeq1)
    for x in range(len(obSeq1)):
        obSeq[len(obSeq1)-x-1]=obSeq1[x]
    PK.saveStates(states)
    PK.saveObservations(observables)
    PK.saveTMatrix(TM)
    PK.saveEMatrix(EM1)
    viterbiM=PK.scoringSolo(obSeq)[1]
    beta=viterbiM[i][len(obSeq)-1-t]/EM1[i][observables.index(obSeq1[t])]   
    #if t == 0:    #we bring in the start at beta not at A &&&&&&&&&&&&&&&&&&&&&&&
        #beta*= TM[0][i]    
    return beta
def gama(i,t,obSeq1):
    alph=alpha(i,t,obSeq1)
    bet=beta(i,t,obSeq1)
    totalGam=0
    #for x in range(len(states)):
        #totalGam+=alpha(x,t,obSeq1)*TM1[x+1][-1]
    #if t>0 :    #47-49 = correction for early ends at t   // and t<len(obSeq1)-1
        #for z in range(t):
            #nonSenseSeqLeft=obSeq1[:z+1]
            #print("nonSenseSeq= ",nonSenseSeqLeft)
            #for x in range(len(states)):
                #temp=alpha(x,z,nonSenseSeqLeft)
                #print(temp)
                #totalGam+=temp
        #print(totalGam)
        #for z in range(t,len(obSeq1)):
            #nonSenseSeqRight=obSeq1[z:]
            #for x in range(len(states)):
                #temp=beta(x,z,nonSenseSeqRight)
                #totalGam+=temp
    for x in range(len(states)):
        totalGam+=alpha(x,t,obSeq1)*beta(x,t,obSeq1)
    gama=alph*bet/totalGam
    return gama
def zeta(i,j,t,obSeq1):
    alphI=alpha(i,t,obSeq1)
    betJ=beta(j,t+1,obSeq1)
    zitIJ=alphI*TM1[i+1][j]*EM1[j][observables.index(obSeq1[t+1])]*betJ

    totalZit=0
    for x in range(len(states)):
        #totalZit+=alpha(x,t,obSeq1)*TM1[x+1][-1]
        for y in range(len(states)):
            totalZit+=alpha(x,t,obSeq1)*TM1[x+1][y]*EM1[y][observables.index(obSeq1[t+1])]*beta(y,t+1,obSeq1)     
    zetaIJ=zitIJ/totalZit
    return zetaIJ
def newTM(obSeq1):
    newMatrix=[[0 for y in range(len(TM1))] for x in range(len(TM1))]
    newMatrix[0][-1]=0
    for y in range(len(TM1)-1):
        newMatrix[0][y]=gama(y,0,obSeq1)
    for x in range(1,len(TM1)):
        endUnit=gama(x-1,(len(obSeq1)-1),obSeq1)*(TM1[x][-1])
        for y in range(len(TM1)-1):
            zetaAllTime=0
            gamaAllTime=0
            for t in range(len(obSeq1)-1):
                zetaAllTime+=zeta(x-1,y,t,obSeq1)
                gamaAllTime+=gama(x-1,t,obSeq1)
            newMatrix[x][y]=(zetaAllTime/gamaAllTime)*(1-TM1[x][-1])
        rowTotal=endUnit
        for y in range(len(TM1)-1):
            rowTotal+=newMatrix[x][y]
        newMatrix[x][-1]=endUnit/rowTotal
        for y in range(len(TM1)-1):
            newMatrix[x][y]=newMatrix[x][y]/rowTotal
    return newMatrix
def newEM(obSeq1):
    newMatrix=[[0 for y in range(len(EM1[0]))] for x in range(len(EM1))]
    for y in range(len(EM1[0])):
        for x in range(len(EM1)):
            nom=0
            denom=0
            for t in range(len(obSeq1)):
                denom+=gama(x,t,obSeq1)
                if obSeq1[t]==observables[y]:
                    nom+=gama(x,t,obSeq1)
            newMatrix[x][y]=nom/denom      
    return newMatrix

sum1=gama(0,0,obSeq1)
sum2=(zeta(0,0,0,obSeq1))+(zeta(0,1,0,obSeq1))+(zeta(0,2,0,obSeq1))
MT2=newTM(obSeq1)
EM2=newEM(obSeq1)
