import tkinter as tk
from tkinter import ttk, StringVar
from tkinter.font import BOLD

def runTimeVariables_Function(fileBasedNorm):
    master = tk.Tk()
    master.geometry("750x750")
    master.title("E.L.I. | Enhanced Lynx Interface")
    backgroundColor = "#e06666"
    master.config(background=backgroundColor)

    run_variables_Dict = {}
    paddingX = 5
    paddingY = 5

    intro_frame = tk.Frame(background=backgroundColor)
    intro_label = tk.Label(master=intro_frame, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 20, BOLD), background=backgroundColor, foreground="white")
    intro_label.grid(row=1, columnspan=3)
    intro_frame.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")

    horizontal =tk.Frame(master, bg="white", height=2,width=415)
    horizontal.place(x=10, y=45)



    q1_frame = tk.Frame(background=backgroundColor)
    question_1_label = tk.Label(master=q1_frame, text="Select source plate type:", font=("Monospace", 12), background=backgroundColor)
    question_1_label.grid(row=1,column=1, sticky="w")
    question_1_combo = ttk.Combobox(master=q1_frame, values=["96 MasterBlock", "96 DeepWell", "96 FlatBottom", "96 PCR"])
    question_1_combo.grid(row=2, column=1, sticky="w")
    q1_frame.grid(row=2,column=1, padx=paddingX, pady=paddingY,sticky="w")

    q2_frame = tk.Frame(background=backgroundColor)
    question_2_label = tk.Label(master=q2_frame, text="Select destinaton plate type:", font=("Monospace", 12), background=backgroundColor)
    question_2_label.grid(row=1,column=1, sticky="w")
    #change upon source selection
    question_2_combo = ttk.Combobox(master=q2_frame, values=["96 MasterBlock", "96 DeepWell", "96 FlatBottom", "96 PCR"])
    question_2_combo.grid(row=2, column=1, sticky="w")
    q2_frame.grid(row=3, column=1, padx=paddingX, pady=paddingY,sticky="w")

    q3_frame = tk.Frame(background=backgroundColor)
    question_3_label = tk.Label(master=q3_frame, text="Select tip type: (HINT! Your volume range: XuL - XuL)", font=("Monospace", 12), background=backgroundColor)
    question_3_label.grid(row=1,column=1, sticky="w")
    question_3_combo = ttk.Combobox(master=q3_frame, values=["60F", "340F", "1250F"])
    question_3_combo.grid(row=2, column=1, sticky="w")
    q3_frame.grid(row=4, column=1, padx=paddingX, pady=paddingY,sticky="w")

    q4_frame = tk.Frame(background=backgroundColor)
    question_4_label = tk.Label(master=q4_frame, text="Transfer to echo plate?", font=("Monospace", 12), background=backgroundColor)
    question_4_label.grid(row=1, column=1, sticky="w")
    question_4_answer = tk.IntVar()
    tk.Radiobutton(master=q4_frame, text="Yes", variable=question_4_answer, value=1, font=("Monospace", 12), background=backgroundColor).grid(row=1, column=2, sticky="w")
    tk.Radiobutton(master=q4_frame, text="No", variable=question_4_answer, value=0, font=("Monospace", 12), background=backgroundColor).grid(row=1, column=3, sticky="w")
    q4_frame.grid(row=5, column=1, padx=paddingX, pady=paddingY,sticky="w")

    q5_frame = tk.Frame(background=backgroundColor)
    question_5_label = tk.Label(master=q5_frame, text="Mix plates (8 cycles) after normalization?", font=("Monospace", 12), background=backgroundColor)
    question_5_label.grid(row=1, column=1, sticky="w")
    question_5_answer = tk.IntVar()
    tk.Radiobutton(master=q5_frame, text="Yes", variable=question_5_answer, value=1, font=("Monospace", 12), background=backgroundColor).grid(row=1, column=2, sticky="w")
    tk.Radiobutton(master=q5_frame, text="No", variable=question_5_answer, value=0, font=("Monospace", 12), background=backgroundColor).grid(row=1, column=3, sticky="w")
    q5_frame.grid(row=6, column=1, padx=paddingX, pady=paddingY,sticky="w")

    q6_frame = tk.Frame(background=backgroundColor)
    question_6_label = tk.Label(master=q6_frame, text="Mixing height offset (Recommended 1mm)?", font=("Monospace", 12), background=backgroundColor)
    question_6_label.grid(row=1,column=1, sticky="w")
    intMixHeightOffset = StringVar()
    question_6_combo = tk.Entry(master=q6_frame, textvariable=intMixHeightOffset, relief="sunken")
    question_6_combo.grid(row=1, column=2, sticky="w")
    q6_frame.grid(row=7, column=1, padx=paddingX, pady=paddingY,sticky="w")

    q7_frame = tk.Frame(background=backgroundColor)
    question_7_label = tk.Label(master=q7_frame, text="Mix Volume (Recommended 100ul)?", font=("Monospace", 12), background=backgroundColor)
    question_7_label.grid(row=10,column=1, padx=paddingX, pady=paddingY,sticky="w")
    mixVol = StringVar()
    question_7_combo = tk.Entry(master=q7_frame, textvariable=mixVol, relief="sunken")
    question_7_combo.grid(row=10, column=2, sticky="w")
    q7_frame.grid(row=8, column=1, padx=paddingX, pady=paddingY,sticky="w")

    def submitForum():
        run_variables_Dict["sourceTypeSelected"] = question_1_combo.get()
        run_variables_Dict["desTypeSelected"] = question_2_combo.get()
        run_variables_Dict["tipTypeSelected"] = question_3_combo.get()
        if question_4_answer.get() == 1:
            run_variables_Dict["bCreateEcho"] = "yes"
        else:
            run_variables_Dict["bCreateEcho"] = "no"
        if question_5_answer.get() == 1:
            run_variables_Dict["bMix"] = "yes"
        else:
            run_variables_Dict["bMix"] = "no"
        run_variables_Dict["intMixHeightOffset"] = intMixHeightOffset.get()
        run_variables_Dict["mixVol"] = mixVol.get()
        
        master.destroy()
    


    if fileBasedNorm:
        progressBarGreen =tk.Frame(master, bg="green", height=12, width=305)
        progressBarWhite =tk.Frame(master, bg="white", height=12, width=100)
        progressPercent = tk.Label(master, text="75%",  font=("Arial", 10), background=backgroundColor, foreground="white")
        progressPercent.place(x=415, y=450)
        progressBarGreen.place(x=10, y=450)
        progressBarWhite.place(x=315, y=450)
    else:
        progressBarGreen =tk.Frame(master, bg="green", height=12, width=276)
        progressBarWhite =tk.Frame(master, bg="white", height=12, width=124)
        progressPercent = tk.Label(master, text="66%",  font=("Arial", 10), background=backgroundColor, foreground="white")
        progressPercent.place(x=415, y=450)
        progressBarGreen.place(x=10, y=450)
        progressBarWhite.place(x=276, y=450)



    bSubmit = tk.Button(master ,text="OK",command=submitForum)
    bSubmit.grid(row=25, column=1, padx=10,pady=10,ipadx=15,ipady=5)

    master.mainloop()

    return run_variables_Dict


#run_variable_capture.py