import tkinter as tk
from tkinter.font import BOLD

def worktableImage_Function(worktableImageName, sourceType, desType, tipType):
    master = tk.Tk()
    master.geometry("1000x800")
    master.title("E.L.I. | Enhanced Lynx Interface")
    backgroundColor = "#e06666"
    master.config(background=backgroundColor)

    worktableImage = tk.PhotoImage(file=worktableImageName)

    pageOneDict = {}
    paddingX = 5
    paddingY = 5

    intro_frame = tk.Frame(background=backgroundColor)
    intro_label = tk.Label(master=intro_frame, text="E.L.I. | Enhanced Lynx Interface", font=("Monospace", 20, BOLD), background=backgroundColor, foreground="white")
    intro_label.grid(row=1, columnspan=3)
    intro_frame.grid(row=1, column=1, padx=paddingX, pady=paddingY, sticky="w")

    horizontal =tk.Frame(master, bg="white", height=2,width=415)
    horizontal.place(x=10, y=45)

    worktable_frame = tk.Frame(background=backgroundColor)
    worktable_label = tk.Label(master=worktable_frame, text="Load Deck...", font=("Arial", 14, BOLD), background=backgroundColor)
    worktable_label.grid(row=1, column=2, sticky="w")
    source_label = tk.Label(master=worktable_frame, text=("Sup: " + str(sourceType)), font=("Arial", 14), background=backgroundColor)
    source_label.grid(row=2, column=3, sticky="w")
    des_label = tk.Label(master=worktable_frame, text=("Norm: " + str(desType)), font=("Arial", 14), background=backgroundColor)
    des_label.grid(row=2, column=2, sticky="w")
    tip_label = tk.Label(master=worktable_frame, text=("Tips: " + str(tipType)), font=("Arial", 14), background=backgroundColor)
    tip_label.grid(row=2, column=1, sticky="w")
    worktable_image = tk.Label(master=worktable_frame, image=worktableImage)
    worktable_image.grid(row=3, columnspan=4)
    worktable_frame.grid(row=2, column=1, padx=paddingX, pady=paddingY, sticky="w")

    progressBarGreen =tk.Frame(master, bg="green", height=12, width=405)
    progressPercent = tk.Label(master, text="100%",  font=("Arial", 10), background=backgroundColor, foreground="white")
    progressPercent.place(x=415, y=600)
    progressBarGreen.place(x=10, y=600)

    remainder_frame = tk.Frame(background=backgroundColor)
    tipCheck_label = tk.Label(master=remainder_frame, text="DON'T FORGET TO MAKE SURE TIPS & PLATES ARE SEATED CORRECTLY IN THEIR NEST!", font=("Arial", 16), background=backgroundColor, foreground="white")
    tipCheck_label.grid(row=1, column=1)
    remainder_frame.grid(row=3, column=1)

    bOK = tk.Button(master ,text="OK",command=master.destroy)
    bOK.grid(row=4, column=1, padx=10,pady=10,ipadx=15,ipady=5)

    master.mainloop()