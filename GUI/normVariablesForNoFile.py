import tkinter as tk
from tkinter.font import BOLD
from tkinter import StringVar, filedialog, ttk

def normVariablesNoFile_function():
    noFileVarInfoDict = {}

    master = tk.Tk()
    master.geometry("550x300")
    master.title("E.L.I. | Enhanced Lynx Interface")
    backgroundColor = "#e06666"
    master.config(background=backgroundColor)
    paddingX = 5
    paddingY = 5
    

    intro_frame = tk.Frame(background=backgroundColor)
    intro_label = tk.Label(master=intro_frame, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 20, BOLD), background=backgroundColor, foreground="white")
    intro_label.grid(row=1, columnspan=3)
    intro_frame.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")

    horizontal =tk.Frame(master, bg="white", height=2,width=415)
    horizontal.place(x=10, y=45)

    second_frame = tk.Frame(background=backgroundColor)
    question_2_label = tk.Label(master=second_frame, text="Target volume (uL):",  font=("Arial", 14), background=backgroundColor)
    question_2_label.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")
    targetVol = StringVar()
    question_2_answer = tk.Entry(master=second_frame, textvariable=targetVol)
    question_2_answer.grid(row=1, column=2, sticky="w")

    question_3_label = tk.Label(master=second_frame, text="Target concentration (ug/mL):",  font=("Arial", 14), background=backgroundColor)
    question_3_label.grid(row=2, column=1, padx=paddingX, pady=paddingY, sticky="w")
    targetConc = StringVar()
    question_3_answer = tk.Entry(master=second_frame, textvariable=targetConc)
    question_3_answer.grid(row=2, column=2, sticky="w")

    question_4_label = tk.Label(master=second_frame, text="Volume for neat transfers (uL):",  font=("Arial", 14), background=backgroundColor)
    question_4_label.grid(row=3, column=1, padx=paddingX, pady=paddingY, sticky="w")
    neatTransfer = StringVar()
    question_4_answer = tk.Entry(master=second_frame, textvariable=neatTransfer)
    question_4_answer.grid(row=3, column=2, sticky="w")
    second_frame.grid(row=2, column=1, sticky="w")

    def submitForum():
        noFileVarInfoDict["targetVol"] = targetVol.get()
        noFileVarInfoDict["targetConc"] = targetConc.get()
        noFileVarInfoDict["neatTransfer"] = neatTransfer.get()

        master.destroy()


    bOK = tk.Button(master ,text="OK",command=submitForum)
    bOK.grid(row=3, column=1, padx=10,pady=10,ipadx=15,ipady=5)

    progressBarGreen =tk.Frame(master, bg="green", height=12, width=138)
    progressBarWhite =tk.Frame(master, bg="white", height=12, width=262)
    progressPercent = tk.Label(master, text="33%",  font=("Arial", 10), background=backgroundColor, foreground="white")
    progressPercent.place(x=415, y=250)
    progressBarGreen.place(x=10, y=250)
    progressBarWhite.place(x=138, y=250)

    master.mainloop()

    return noFileVarInfoDict