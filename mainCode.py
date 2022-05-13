states=[]
observations=[]
transmissionMatrix=[]
emissionMatrix=[]
def saveStates(list):
    global states
    states=list
    return
def saveObservations(list):
    global observations
    observations=list
    return
def saveTMatrix(list):
    global transmissionMatrix
    transmissionMatrix=list
    return
def saveEMatrix(list):
    global emissionMatrix
    emissionMatrix=list
    return
def scoringSolo(obSeq):
    viterbiMatrix= [[0 for y in range(len(obSeq))] for x in range(len(states))]
    firstOb=obSeq[0]
    for i in range(len(states)):
        viterbiMatrix[i][0]=transmissionMatrix[0][i] * emissionMatrix[i][observations.index(firstOb)]
    for j in range(1,len(obSeq)):
        for i in range(len(states)):
            totalTP=0
            for edge in range(len(states)):
                totalTP+=viterbiMatrix[edge][j-1] * transmissionMatrix[edge+1][i]
            totalP=totalTP * emissionMatrix[i][observations.index(obSeq[j])]
            viterbiMatrix[i][j]=totalP
    obSeqP=0
    for i in range(len(states)):
        obSeqP+=viterbiMatrix[i][-1]*transmissionMatrix[i+1][-1]
    return [obSeqP,viterbiMatrix]
def scoringPair(obSeq,stSeq):
    pairP=transmissionMatrix[0][states.index(stSeq[0])] * emissionMatrix[states.index(stSeq[0])][observations.index(obSeq[0])]
    pairP=pairP * transmissionMatrix[states.index(stSeq[-1])+1][-1] # we are adding End early. who cares
    theRange=range(1,len(obSeq))
    for i in theRange:
        pairP=pairP * transmissionMatrix[states.index(stSeq[i-1])+1][states.index(stSeq[i])] * emissionMatrix[states.index(stSeq[i])][observations.index(obSeq[i])]
    return [pairP]
def decoding(obSeq):
    viterDecoMatrix= [[0 for y in range(len(obSeq))] for x in range(len(states))]
    pathsMatrix= [[[] for y in range(len(obSeq)-1)] for x in range(len(states))]
    listOfPaths=[]
    firstOb=obSeq[0]
    for i in range(len(states)):
        viterDecoMatrix[i][0]=transmissionMatrix[0][i] * emissionMatrix[i][observations.index(firstOb)]
    for j in range(1,len(obSeq)):
        for i in range(len(states)):
            maxP=0
            path=[]
            for edge in range(len(states)):
                edgeP=viterDecoMatrix[edge][j-1] * transmissionMatrix[edge+1][i]
                if edgeP>maxP:
                    maxP=edgeP
                    path=[edge]
                elif edgeP==maxP:
                    path.append(edge)
            viterDecoMatrix[i][j]= maxP * emissionMatrix[i][observations.index(obSeq[j])]
            pathsMatrix[i][j-1]=path
    #for i in range(len(states)):
        #viterDecoMatrix[i][-1]=viterDecoMatrix[i][-1]*emissionMatrix[i][observations.index(obSeq[-1])]
    k=len(obSeq)-1
    while k>0:
        if listOfPaths==[]:
            maxViterP=0
            pathElement={}
            for i in range(len(states)):
                if viterDecoMatrix[i][k]> maxViterP:
                    maxViterP=viterDecoMatrix[i][k]
                    pathElement={}
                    pathElement[i]=(pathsMatrix[i][k-1])
                elif viterDecoMatrix[i][k]== maxViterP:
                    pathElement[i]=(pathsMatrix[i][k-1])
            for key in pathElement.keys():
                for edge in pathElement[key]:
                    listOfPaths.append([edge,key])
            k-=1
        else:
            for path in listOfPaths.copy():
                i=path[0]
                for element in pathsMatrix[i][k-1]:
                    pathUpdate=path
                    pathUpdate.insert(0,element)
                    listOfPaths.append(pathUpdate)
            listOfPaths.remove(path)
            k-=1
    return [maxViterP,listOfPaths]
