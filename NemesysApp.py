# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:14:38 2018

@author: ADMIN
"""
import sklearn
from tkinter import *
import prediction as prd

def create_window():
    #a=mytext2.get()
    #mytext3=Text(root,width=20,height=5)
    #mytext3.grid(row=5,column=1,pady=25)
    a=mytext2.get("1.0",'end-1c')
	#a=input("")
    mylabel4=Label(root,text=prd.find1(a),font='Georgia 25 italic',fg='red')
    mylabel4.grid(row=6,column=1,pady=25,sticky='NW')
    mylabel6=Label(root,text=prd.find2(a),font='Georgia 25 italic',fg='green')
    mylabel6.grid(row=7,column=1,pady=25,sticky='NW')
    
    
    
def clear():
    mytext2.delete("1.0",'end')
    
    
    
root =Tk()
root.geometry('500x500+200+200')
root.title('NEMESYS')


mylabel1=Label(root,text="NEMESYS",font='Georgia 25 italic',fg='green')
mylabel1.grid(row=0,column=1,pady=25,sticky='NW')

mylabel2=Label(root,text="Enter Text Message",font='Georgia 15')
mylabel2.grid(row=2,column=0,pady=25,sticky='NW')

"""mytext2=Entry(root,text='')
mytext2.grid(row=2,column=1,padx=60,pady=25,sticky='NW')
"""
mytext2=Text(root,width=30,height=5)
mytext2.grid(row=2,column=1,padx=60,pady=25,sticky='NW')

b = Button(root, text="Submit",font='Georgia 15 italic',command=create_window)
b.grid(row=4,column=0,padx=40,pady=15)




mybutton2=Button(root,text="Clear",font='Georgia 15 italic',command=clear)
mybutton2.grid(row=4,column=1,pady=15)


mylabel3=Label(root,text="Statement:",font='Georgia 25 italic',fg='red')
mylabel3.grid(row=6,column=0,pady=25,sticky='NW')

mylabel5=Label(root,text="Possibility:",font='Georgia 25 italic',fg='green')
mylabel5.grid(row=7,column=0,pady=25,sticky='NW')
root.mainloop()