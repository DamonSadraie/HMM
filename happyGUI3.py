######################################### Tkinter Root + Retrieving The Stored Vars
import tkinter as tk
import mainCode as mC
observations=mC.observations
states=mC.states
obSeq=[]
stSeq=[]
whichProblem=""
root = tk.Tk()
root.geometry("520x550")
def stDeleteBut(): 
    global stSeq
    if len(stSeq)==0:
        return
    del stSeq[-1]
    someLabel2.config(text=str(stSeq))
    if len(stSeq)==0:
        someLabel2.config(text="your states sequence")
    return
def obsDeleteBut():
    global obSeq
    if len(obSeq)==0:
        return
    del obSeq[-1]
    someLabel.config(text=str(obSeq))
    if len(obSeq)==0:
        someLabel.config(text="your observation sequence")
    return
def scryptGen(index,boul1):
    if boul1==True:
        nameList="observations"
        nameTag="obs"
        nameSeq="obSeq"
        labelName="someLabel"
        rowNumber="5"
        extraVar=""
    else:
        nameList="states"
        nameTag="st"
        nameSeq="stSeq"
        labelName="someLabel2"
        rowNumber="7"
        extraVar="n"
    for i in range(index):   #script Vars= i(i), nameTag(obs), nameList(observations)
        fullName=nameTag+"Button"+str(i)
        exec("global function"+extraVar+str(i)+"\nglobal "+fullName+"\ndef function"+extraVar+str(i)+"():\n\tglobal "+nameSeq+"\n\t"+nameSeq+".append("+nameList+"["+str(i)+"])\n\t"+labelName+".config(text=str("+nameSeq+"))\n\treturn\n"+fullName+"=tk.Button(root,text="+nameList+"[i],padx=5,pady=5,command=function"+extraVar+str(i)+")\n"+fullName+".grid(row="+rowNumber+",column=i)")
    return
def scryptWipe(index,boul1):
    if boul1==True:
        nameTag="obs"
        extraVar=""
    else:
        nameTag="st"
        extraVar="n"
    for i in range(index):
        butName=nameTag+"Button"+str(i)
        funcName="function"+extraVar+str(i)
        exec("global "+butName+"\nglobal "+funcName+"\n"+butName+".destroy()\ndel "+butName+"\ndel "+funcName)
    return
def scoreSoloBut():
    but1.config(relief="sunken")
    but2.config(relief="raised")
    but3.config(relief="raised")
    index=len(observations)
    global whichProblem
    whichProblem="p1"
    but5.config(state="normal")
    if not ("someLabel" in globals() ):  #and "someLabel2" in globals()
        global someLabel
        global someLabel2
        someLabel=tk.Label(root,text="your observation sequence")
        someLabel.grid(row=4,column=0,columnspan=span)

        boul1=True
        scryptGen(index,boul1)
        global newObsDelBut
        newObsDelBut=tk.Button(root,text="delete",padx=5,pady=5,command=obsDeleteBut)
        newObsDelBut.grid(row=5,column=span-1)
    else:
        but5.config(state="disabled")
        but1.config(relief="raised")
        global obSeq
        global stSeq
        obSeq=[]
        stSeq=[]
        boul1=True
        scryptWipe(index,boul1)
        newObsDelBut.destroy()
        del newObsDelBut
        if "stButton0" in globals():
            global newstDelBut
            newstDelBut.destroy()
            del newstDelBut
            boul1=False
            index=len(states)
            scryptWipe(index,boul1)
        someLabel.destroy()
        del someLabel
        if "someLabel2" in globals():
            someLabel2.destroy()
            del someLabel2
    return
def scorePairBut():
    but2.config(relief="sunken")
    but1.config(relief="raised")
    but3.config(relief="raised")
    index=len(observations)
    global whichProblem
    whichProblem="p2"
    but5.config(state="normal")
    if not ("someLabel" in globals() ):  #and "someLabel2" in globals()
        global someLabel
        someLabel=tk.Label(root,text="your observation sequence")
        someLabel.grid(row=4,column=0,columnspan=span)
        global someLabel2
        someLabel2=tk.Label(root,text="your states sequence")
        someLabel2.grid(row=6,column=0,columnspan=span)
        boul1=True
        scryptGen(index,boul1)
        boul1=False
        index=len(states)
        scryptGen(index,boul1)
        global newObsDelBut
        newObsDelBut=tk.Button(root,text="delete",padx=5,pady=5,command=obsDeleteBut)
        newObsDelBut.grid(row=5,column=span-1)
        global newstDelBut
        newstDelBut=tk.Button(root,text="delete",padx=5,pady=5,command=stDeleteBut)
        newstDelBut.grid(row=7,column=span-1)
    else:
        but5.config(state="disabled")        
        but2.config(relief="raised")
        global obSeq
        global stSeq
        obSeq=[]
        stSeq=[]
        boul1=True
        scryptWipe(index,boul1)
        newObsDelBut.destroy()
        del newObsDelBut
        if "newstDelBut" in globals():
            newstDelBut.destroy()
            del newstDelBut
        if "stButton0" in globals():
            boul1=False
            index=len(states)
            scryptWipe(index,boul1)
        someLabel.destroy()
        del someLabel
        if "someLabel2" in globals():
            someLabel2.destroy()
            del someLabel2    
    return
def decodingBut():
    but3.config(relief="sunken")
    but2.config(relief="raised")
    but1.config(relief="raised")
    index=len(observations)
    global whichProblem
    whichProblem="p3"
    but5.config(state="normal")
    if not ("someLabel" in globals() ):  #and "someLabel2" in globals()
        global someLabel
        global someLabel2
        someLabel=tk.Label(root,text="your observation sequence")
        someLabel.grid(row=4,column=0,columnspan=span)

        boul1=True
        scryptGen(index,boul1)
        global newObsDelBut
        newObsDelBut=tk.Button(root,text="delete",padx=5,pady=5,command=obsDeleteBut)
        newObsDelBut.grid(row=5,column=span-1)
    else:
        but5.config(state="disabled")        
        but3.config(relief="raised")
        global obSeq
        global stSeq
        obSeq=[]
        stSeq=[]
        boul1=True
        scryptWipe(index,boul1)
        newObsDelBut.destroy()
        del newObsDelBut
        if "stButton0" in globals():
            boul1=False
            index=len(states)
            scryptWipe(index,boul1)
            global newstDelBut
            newstDelBut.destroy()
            del newstDelBut
        someLabel.destroy()
        del someLabel
        if "someLabel2" in globals():
            someLabel2.destroy()
            del someLabel2
    return
def calculate():
    but5.config(fg="green")
    global whichProblem, resulttxt1 ,resulttxt2,scroll,reslabel1,reslabel2,obSeq,stSeq,someLabel,someLabel2,newObsDelBut,newstDelBut
    if whichProblem=="p-1":
        obSeq=[]
        stSeq=[]
        scryptWipe(len(states),boul1=False)
        scryptWipe(len(observations),boul1=True) 
        someLabel.destroy()
        someLabel2.destroy()
        resulttxt1.destroy()
        reslabel1.destroy()
        newObsDelBut.destroy()
        newstDelBut.destroy()
        del newObsDelBut
        del newstDelBut
        del someLabel
        del someLabel2
        del reslabel1
        del resulttxt1       
        but1.config(state="normal")
        but2.config(state="normal")
        but3.config(state="normal")
        but5.config(text="Solve")
        but5.config(state="disabled")
    if whichProblem=="p0":
        obSeq=[]
        stSeq=[]
        someLabel.destroy()
        resulttxt1.destroy()
        resulttxt2.destroy()      
        scroll.destroy()
        reslabel1.destroy()
        reslabel2.destroy()
        newObsDelBut.destroy()
        del newObsDelBut
        del someLabel
        del resulttxt1
        del resulttxt2
        del scroll
        del reslabel1
        del reslabel2
        scryptWipe(len(observations),boul1=True)
        but1.config(state="normal")
        but2.config(state="normal")
        but3.config(state="normal")
        but5.config(text="Solve")
        but5.config(state="disabled")
    if whichProblem=="p1":
        but1.config(state="disabled")
        but2.config(state="disabled")
        but3.config(state="disabled")
        result=mC.scoringSolo(obSeq)
        resulttxt1=tk.Text(root,width=30,height=1)
        resulttxt1.grid(row=11,column=1,columnspan=(span))
        resulttxt2=tk.Text(root, height=5, width=30)
        scroll = tk.Scrollbar(root)
        resulttxt2.configure(yscrollcommand=scroll.set)
        scroll.config(command=resulttxt2.yview)
        resulttxt2.grid(row=13,column=1,columnspan=span)
        scroll.grid(row=13,column=0)
        resulttxt1.insert(tk.END, str(result[0]))
        resulttxt2.insert(tk.END, str(result[1]))
        reslabel1=tk.Label(text="Probability")
        reslabel1.grid(row=11,column=0,columnspan=len(observations))
        reslabel2=tk.Label(text="viterbiMatrix")
        reslabel2.grid(row=13,column=0,columnspan=len(observations))
        whichProblem="p0"
        but5.config(text="reset")
    if whichProblem=="p2":
        if len(obSeq) != len(stSeq):
            but5.config(fg="red")
            return
        but1.config(state="disabled")
        but2.config(state="disabled")
        but3.config(state="disabled")
        result=mC.scoringPair(obSeq,stSeq)
        resulttxt1=tk.Text(root,width=30,height=1)
        resulttxt1.grid(row=11,column=1,columnspan=(span))
        reslabel1=tk.Label(text="Pair Probability")
        reslabel1.grid(row=11,column=0,columnspan=len(observations))
        resulttxt1.insert(tk.END, str(result[0]))
        whichProblem="p-1"
        but5.config(text="reset")        
    if whichProblem=="p3":
        but1.config(state="disabled")
        but2.config(state="disabled")
        but3.config(state="disabled")
        result=mC.decoding(obSeq)     
        resulttxt1=tk.Text(root,width=30,height=1)
        resulttxt1.grid(row=11,column=1,columnspan=(span))
        resulttxt2=tk.Text(root, height=5, width=30)
        scroll = tk.Scrollbar(root)
        resulttxt2.configure(yscrollcommand=scroll.set)
        scroll.config(command=resulttxt2.yview)
        resulttxt2.grid(row=13,column=1,columnspan=span)
        scroll.grid(row=13,column=0)
        resulttxt1.insert(tk.END, str(result[0]))
        prettyResultList=[]
        for i in result[1]:
            tempList=[]
            for j in i:                
                tempList.append(states[j])
            prettyResultList.append(tempList)
        resulttxt2.insert(tk.END, str(prettyResultList))
        reslabel1=tk.Label(text="Probability")
        reslabel1.grid(row=11,column=0,columnspan=len(observations))
        reslabel2=tk.Label(text="Most Probable State Sequence(s)")
        reslabel2.grid(row=13,column=0,columnspan=len(observations))
        whichProblem="p0" 
        but5.config(text="reset")           
    return
span=100
but1=tk.Button(root,text="     Scoring Problem, Solo Observation Sequence     ",padx=35,pady=15,command=scoreSoloBut,fg="green",bg="black",font=("Times New Roman", 15),relief="raised",borderwidth=10)
but1.grid(row=0,column=0,columnspan = span)
but2=tk.Button(root,text=" Scoring Problem, Observation-State Sequence Pair ",padx=35,pady=15,command=scorePairBut,fg="green",bg="black",font=("Times New Roman", 15),relief="raised",borderwidth=10)
but2.grid(row=1,column=0,columnspan = span)
but3=tk.Button(root,text="                          Decoding Problem                           ",padx=35,pady=15,command=decodingBut,fg="green",bg="black",font=("Times New Roman", 15),relief="raised",borderwidth=10)
but3.grid(row=2,column=0,columnspan = span)
but4=tk.Button(root,text="                             Learning Problem                             ",padx=35,pady=15,command=None,fg="red",bg="black",state="disabled",font=("Times New Roman", 15),relief="raised",borderwidth=1)
but4.grid(row=3,column=0,columnspan = span)
but5=tk.Button(root,text="Solve",padx=35,pady=15,command=calculate,fg="green",bg="black",state="disabled",font=("Times New Roman", 15),relief="raised",borderwidth=1)
but5.grid(row=10,column=span-1)
root.mainloop()
