import tkinter as tk
import mainCode as mC
root = tk.Tk()
root.geometry("520x200")

states=[]
observations=[]
sp="******                                                                     ******"

def action1():
    global states
    temp=e1.get()
    if temp=="":
        return
    e1.delete(0,"end")
    if temp in states:
        return
    states.append(temp)
    tempStates=""
    for i in states:
        tempStates+=i+" "
    padD=140-(len(tempStates)*3)
    L2.config(text=tempStates)
    L2.config(padx=padD)
    return 
def action2():
    if states==[]:
        return
    del states[-1]
    tempStates=""
    for i in states:
        tempStates+=i+" "
    padD=140-(len(tempStates)*3)
    L2.config(text=tempStates)
    L2.config(padx=padD)
    return
def done1():
    but1.config(state="disabled")
    but2.config(state="disabled")
    but3.config(state="disabled")
    e1.config(state="disabled")
    but4.config(state="normal")
    but5.config(state="normal")
    but6.config(state="normal")
    e2.config(state="normal")
    return
def action3():
    global observations
    temp=e2.get()
    if temp=="":
        return    
    e2.delete(0,"end")
    if temp in observations:
        return
    observations.append(temp)
    tempObs=""
    for i in observations:
        tempObs+=i+" "
    padE=140-(len(tempObs)*3)
    L4.config(text=tempObs)
    L4.config(padx=padE)
    return 
def action4():
    if observations==[]:
        return
    del observations[-1]
    tempObs=""
    for i in observations:
        tempObs+=i+" "
    padE=140-(len(tempObs)*3)
    L4.config(text=tempObs)
    L4.config(padx=padE)
    return
def done2():
    mC.saveStates(states)
    mC.saveObservations(observations)
    root.destroy()
    import happyGUI2
    return

L1=tk.Label(root,text="Enter the states and hit add one by one")
L2=tk.Label(root,text="", borderwidth=2, relief="groove",padx=170)  # needs changing
border1=tk.Label(root,text=sp)
##################
L3=tk.Label(root,text="Enter the observations and hit add one by one   ")
L4=tk.Label(root,text="", borderwidth=2, relief="groove",padx=170)
border2=tk.Label(root,text=sp)

but1=tk.Button(root,text="add",padx=15,pady=5,command=action1,fg="green",bg="grey")
but2=tk.Button(root,text="delete",padx=15,pady=5,command=action2,fg="green",bg="grey")
but3=tk.Button(root,text="done",padx=45,pady=5,command=done1,fg="green",bg="grey")
######################
but4=tk.Button(root,text="add",padx=15,pady=5,command=action3,fg="green",bg="grey",state="disabled")
but5=tk.Button(root,text="delete",padx=15,pady=5,command=action4,fg="green",bg="grey",state="disabled")
but6=tk.Button(root,text="done",padx=45,pady=5,command=done2,fg="green",bg="grey",state="disabled")

e1=tk.Entry(root,width=20)
###########
e2=tk.Entry(root,width=20,state="disabled")

L1.grid(row=0,column=0)
L2.grid(row=1,column=0,columnspan = 3)
border1.grid(row=2,column=0,columnspan = 4)
but1.grid(row=0,column=1)
but2.grid(row=0,column=2)
but3.grid(row=1,column=3)
e1.grid(row=0,column=3)
#########
L3.grid(row=4,column=0)
L4.grid(row=5,column=0,columnspan = 3)
border2.grid(row=3,column=0,columnspan = 4)
but4.grid(row=4,column=1)
but5.grid(row=4,column=2)
but6.grid(row=5,column=3)
e2.grid(row=4,column=3)

root.mainloop()