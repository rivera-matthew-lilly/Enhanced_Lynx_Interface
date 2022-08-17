
import tkinter as tk
from tkinter.font import ITALIC, BOLD

def pageOne_function():
    master = tk.Tk()
    master.geometry("725x250")
    master.title("E.L.I. | Enhanced Lynx Interface")
    backgroundColor = "#e06666"
    master.config(background=backgroundColor)

    pageOneDict = {}
    paddingX = 5
    paddingY = 5



    intro_frame = tk.Frame(background=backgroundColor)
    intro_label = tk.Label(master=intro_frame, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 20, BOLD), background=backgroundColor, foreground="white")
    intro_label.grid(row=1, columnspan=3)
    intro_frame.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")

    horizontal =tk.Frame(master, bg="white", height=2,width=415)
    horizontal.place(x=10, y=45)




    direction_frame =tk.Frame(background=backgroundColor)
    intro_directions = tk.Label(master=direction_frame, text="Hello, I am ELI! Please answer the questions below and I will take care of the rest.", font=("Monospace", 14, ITALIC), background=backgroundColor,  foreground="white")
    intro_directions.grid(row=2, columnspan=10)
    direction_frame.grid(row=2, column=1, padx=paddingX, pady=10, sticky="w")


    #Is this a file based norm?
    q1_frame = tk.Frame(background=backgroundColor)
    question_1_label = tk.Label(master=q1_frame, text="Is this going to be a CSV file based normalization?", font=("Arial", 14), background=backgroundColor)
    question_1_label.grid(row=1, column=1, sticky="w")
    question_1_answer = tk.IntVar()
    tk.Radiobutton(master=q1_frame, text="Yes", variable=question_1_answer, value=1, font=("Arial", 14), background=backgroundColor).grid(row=1, column=2, sticky="w")
    tk.Radiobutton(master=q1_frame, text="No", variable=question_1_answer, value=0, font=("Arial", 14), background=backgroundColor).grid(row=1, column=3, sticky="w")
    q1_frame.grid(row=3, column=1, padx=paddingX, pady=paddingY,sticky="w")



    def submitForum():
        if question_1_answer.get() == 1:
            pageOneDict["fileBasedNorm"] = "yes"
        else:
            pageOneDict["fileBasedNorm"] = "no"
        
        master.destroy()

    bSubmit = tk.Button(master , text="OK", bg="white", font=("Arial"), command=submitForum)
    bSubmit.grid(row=5, column=1, padx=10,pady=10,ipadx=15,ipady=5, sticky="s")


    progressBarGreen =tk.Frame(master, bg="green", height=12, width=5)
    progressBarWhite =tk.Frame(master, bg="white", height=12, width=400)
    progressPercent = tk.Label(master, text="0%",  font=("Arial", 10), background=backgroundColor, foreground="white")
    progressPercent.place(x=415, y=210)
    progressBarGreen.place(x=10, y=210)
    progressBarWhite.place(x=15, y=210)

    master.mainloop()

    return pageOneDict
    


#pageOne.py

#./dL