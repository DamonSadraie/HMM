######################################### Tkinter Root + Retrieving The Stored Vars
import tkinter as tk
import mainCode as mC
root = tk.Tk()
root.geometry("520x400")
observations=mC.observations
states=mC.states
######################################### defusing exec/eval danger by making input wierd!
wierdStates=[]
wierdObservations=[]
def wierd(states,observations):
    global wierdStates
    global wierdObservations
    for i in states:
        stLen=len(i)
        tempState=i
        for j in range(stLen):
            tempState+=("letter"+str(ord(tempState[0])))
            tempState=tempState[1:]
        wierdStates.append(tempState)
    for i in observations:
        obLen=len(i)
        tempObs=i
        for j in range(obLen):
            tempObs+=("letter"+str(ord(tempObs[0])))
            tempObs=tempObs[1:]
        wierdObservations.append(tempObs)
    return
wierd(states,observations)
######################################### Local Vars needed for exec/eval Var Generation
wierdSX=["Start"] + wierdStates
wierdSY=wierdStates + ["End"]
normalSX=["Start"] + states
normalSY=states + ["End"]
wierdRange=range(len(wierdStates)+1)
creapyRange=range(len(wierdStates))
cringeRange=range(len(wierdObservations))
Xadditive=3+len(wierdStates)            # for adjusting the 2nd matrix row coordinates
######################################### The Visual Transmission Matrix Created
title=tk.Label(root,text="Transmission")
title.grid(row=0,column=0)
for i in wierdRange:
    exec(wierdSX[i] + "x =tk.Label(root,text=normalSX[i])")
    exec(wierdSX[i] + "x.grid(row=i+1,column=0)")
    exec(wierdSY[i] + "y =tk.Label(root,text=normalSY[i])")
    exec(wierdSY[i] + "y.grid(row=0,column=i+1)")
    for j in wierdRange:
        unit=wierdSX[i]+wierdSY[j]
        exec(unit + "=tk.Entry(root,width=10)")
        exec(unit + ".grid(row=i+1,column=j+1)")
######################################### The Visual Emission Matrix Created
title=tk.Label(root,text="Emission")
title.grid(row=Xadditive,column=0)
for i in cringeRange:
    exec(wierdObservations[i] + "y2 =tk.Label(root,text=observations[i])")
    exec(wierdObservations[i] + "y2.grid(row=Xadditive,column=i+1)")
for i in creapyRange:
    exec(wierdStates[i] + "x2 =tk.Label(root,text=states[i])")
    exec(wierdStates[i] + "x2.grid(row=i+1+Xadditive,column=0)")
    for j in cringeRange:
        unit=wierdStates[i]+wierdObservations[j]
        exec(unit + "=tk.Entry(root,width=10)")
        exec(unit + ".grid(row=i+1+Xadditive,column=j+1)")
######################################### All The Button Functions
but1color="black"
but2color="black"
def but1ok():
    global but1color
    try:
        transmissionMatrix = [[0 for y in wierdRange] for x in wierdRange]
        for i in wierdRange:
            for j in wierdRange:
                unit=wierdSX[i]+wierdSY[j]
                if eval("not (float("+unit+".get()) >= 0 and float("+unit+".get()) <= 1)"):
                    but1.config(fg="red")
                    del transmissionMatrix
                    return
                exec("transmissionMatrix[i][j]= float(" + unit +'.get())')
        Xrange=range(len(transmissionMatrix))
        Yrange=range(len(transmissionMatrix[0]))
        for x in Xrange:
            totalY=0
            for y in Yrange:
                totalY+=float(transmissionMatrix[x][y])
            if not (totalY==1 or totalY==2):
                but1.config(fg="red")
                del transmissionMatrix
                return
        mC.saveTMatrix(transmissionMatrix)
        but1color="green"
        but1.config(fg="green")
    except:
        but1color="red"
        but1.config(fg="red")
        del transmissionMatrix
        return
def but2ok():
    global but2color
    try:
        emissionMatrix = [[0 for y in cringeRange] for x in creapyRange]
        for i in creapyRange:
            for j in cringeRange:
                unit=wierdStates[i]+wierdObservations[j]
                if eval("not (float("+unit+".get()) >= 0 and float("+unit+".get()) <= 1)"):
                    but2.config(fg="red")
                    del emissionMatrix
                    return
                exec("emissionMatrix[i][j]= float(" + unit +'.get())')
        Xrange=range(len(emissionMatrix))
        Yrange=range(len(emissionMatrix[0]))
        for x in Xrange:
            totalY=0
            for y in Yrange:
                totalY+=float(emissionMatrix[x][y])
            if not (totalY==1):
                but1.config(fg="red")
                del emissionMatrix
                return        
        mC.saveEMatrix(emissionMatrix)
        but2color="green"
        but2.config(fg="green")
        if but1color=="green":
            but3.config(state="normal")
            but3.config(fg="green")
    except:
        but2color="red"
        but2.config(fg="red")
        del emissionMatrix
        return
def but3ok():
    root.destroy()
    import happyGUI3
    return
but1=tk.Button(root,text="click!",padx=15,pady=5,command=but1ok,fg="black",bg="grey")
but1.grid(row=len(wierdStates)+2,column=len(wierdStates)+2)
but2=tk.Button(root,text="click!",padx=15,pady=5,command=but2ok,fg="black",bg="grey")
but2.grid(row=len(wierdStates*2)+4,column=len(wierdObservations)+1)
but3=tk.Button(root,text="Go to Menu",padx=15,pady=5,command=but3ok,fg="red",bg="grey",state="disabled")
but3.grid(row=len(wierdStates*2)+4,column=len(wierdObservations)+2,columnspan=10)
root.mainloop()
