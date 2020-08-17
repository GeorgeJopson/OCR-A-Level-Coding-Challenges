from tkinter import *
import re
def clearWindow():
    for widget in window.winfo_children():
        widget.destroy()
def assignWeight(xValue,yValue,weightValue):
    
    for x in range(xValue):
        Grid.columnconfigure(window, x, weight=weightValue)
        
    for y in range(yValue):
        Grid.rowconfigure(window, y, weight=weightValue)

def main():
    global txtInput
    global regexInput
    
    Label(window, text='Your text: ').grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
    txtInput=Entry(window,bd=2)
    txtInput.grid(row=0,column=2,columnspan=3,padx=2, pady=2,sticky=N+S+E+W)
    
    Label(window, text='Your Regex Expression: ').grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)
    
    regexInput=Entry(window,bd=2)
    regexInput.grid(row=1,column=2,columnspan=3,padx=2, pady=2,sticky=N+S+E+W)
    
    submitBtn=Button(window,text="Sumbit",command=check).grid(row=2,column=0,columnspan=4,padx=2, pady=2,sticky=N+S+E+W)
    
def check():
    global txtInput
    global regexInput
    text=txtInput.get()
    regex=regexInput.get()
    result=re.search(regex,text)
    outcome=''
    if(result):
        outcome="Matches: "+result.group()
    else:
        outcome="No matches found"
    clearWindow()
    Label(window,text=outcome).grid(row=0,column=0, columnspan=5,sticky=N+S+E+W)
    
    
window =Tk()
window.title("Regex Expression Checker")
assignWeight(3,5,5)
main()
window.mainloop()
