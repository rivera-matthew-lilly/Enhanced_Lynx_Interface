import tkinter as tk
from tkinter.font import BOLD

def gbgOrOctetToggle_function():
    master = tk.Tk()
    master.geometry("600x250")
    master.title("E.L.I. | Enhanced Lynx Interface")
    backgroundColor = "#e06666"
    master.config(background=backgroundColor)

    OctetGBGToggleDict = {}
    paddingX = 5
    paddingY = 5



    intro_frame = tk.Frame(background=backgroundColor)
    intro_label = tk.Label(master=intro_frame, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 20, BOLD), background=backgroundColor, foreground="white")
    intro_label.grid(row=1, columnspan=3)
    intro_frame.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")

    horizontal =tk.Frame(master, bg="white", height=2,width=415)
    horizontal.place(x=10, y=45)



    toggle_frame = tk.Frame(background=backgroundColor)
    gbgOrOctet_label = tk.Label(master=toggle_frame, text="Does this file orginate from the Octet or GBG?", font=("Arial", 14), background=backgroundColor)
    gbgOrOctet_label.grid(row=1, column=1, sticky="w")
    gbgOrOctetToggle_answer = tk.IntVar()
    tk.Radiobutton(master=toggle_frame, text="GBG", variable=gbgOrOctetToggle_answer, value=1, font=("Arial", 14), background=backgroundColor).grid(row=1, column=2, sticky="w")
    tk.Radiobutton(master=toggle_frame, text="Octet", variable=gbgOrOctetToggle_answer, value=0, font=("Arial", 14), background=backgroundColor).grid(row=1, column=3, sticky="w")
    toggle_frame.grid(row=4, column=1, padx=paddingX, pady=paddingY, sticky="w")



    def submitForum():
        if gbgOrOctetToggle_answer.get() == 1:
            OctetGBGToggleDict["fileOrigin"] = "GBG"
        else:
            OctetGBGToggleDict["fileOrigin"] = "Octet"
        master.destroy()

    bSubmit = tk.Button(master , text="OK", bg="white", font=("Arial"), command=submitForum)
    bSubmit.grid(row=5, column=1, padx=10,pady=10,ipadx=15,ipady=5, sticky="s")


    progressBarGreen =tk.Frame(master, bg="green", height=12, width=105)
    progressBarWhite =tk.Frame(master, bg="white", height=12, width=300)
    progressPercent = tk.Label(master, text="25%",  font=("Arial", 10), background=backgroundColor, foreground="white")
    progressPercent.place(x=415, y=170)
    progressBarGreen.place(x=10, y=170)
    progressBarWhite.place(x=115, y=170)

    master.mainloop()

    return OctetGBGToggleDict

#OctetGBGToggle.py 