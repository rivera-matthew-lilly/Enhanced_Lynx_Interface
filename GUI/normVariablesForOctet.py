import tkinter as tk
from tkinter.font import ITALIC, BOLD
from tkinter import StringVar, filedialog, ttk

def normVariablesOctet_function():
    Octet_Info_Dict = {}

    master = tk.Tk()
    master.geometry("550x350")
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

    # direction_frame =tk.Frame(background="#a3a3c2")
    # intro_directions = tk.Label(master=direction_frame, text="Hello, I am ELI! Please answer the questions below and I will take care of the rest.", font=("Monospace", 12, ITALIC), background="#a3a3c2")
    # intro_directions.grid(row=2, columnspan=10)
    # direction_frame.grid(row=2, column=1, padx=paddingX, pady=paddingY, sticky="w")

    ######################### QUESTION #1 ################################

    def open_fileInput():
        new_window = tk.Toplevel(master)
        new_window.title("Input Octet Files")
        new_window.config(background=backgroundColor)

        def question_1_selected():

            choice = question_1_answer.get()

            def browse_file_1():
                filename_1 = filedialog.askopenfilename(initialdir="C:\codeBASE\Lynx", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
                ent1.configure(text=filename_1, font=10)
                Octet_Info_Dict["octetFile_1"] = filename_1
            
            def browse_file_2():
                filename_2 = filedialog.askopenfilename(initialdir="C:\codeBASE\Lynx", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
                ent2.configure(text=filename_2, font=10)
                Octet_Info_Dict["octetFile_2"] = filename_2

            def browse_file_3():
                filename_3 = filedialog.askopenfilename(initialdir="C:\codeBASE\Lynx", title="Select a File", filetypes=(("CSV files","*.csv"),("All files","*.*")))
                ent3.configure(text=filename_3, font=10)
                Octet_Info_Dict["octetFile_3"] = filename_3
    ######################################################################
            def new_ok_button():
                normalizedPlatCount = 0
                if choice >= 1:
                    octet_active_quads_1 = active_quads_1.get()
                    Octet_Info_Dict["Octet Active Quads 1"] = octet_active_quads_1
                    normalizedPlatCount = normalizedPlatCount + int(octet_active_quads_1)
                if choice >= 2:
                    octet_active_quads_2 = active_quads_2.get()
                    Octet_Info_Dict["Octet Active Quads 2"] = octet_active_quads_2
                    normalizedPlatCount = normalizedPlatCount + int(octet_active_quads_2)
                if choice >= 3:
                    octet_active_quads_3 = active_quads_3.get()
                    Octet_Info_Dict["Octet Active Quads 3"] = octet_active_quads_3
                    normalizedPlatCount = normalizedPlatCount + int(octet_active_quads_3)
                Octet_Info_Dict["Normalized Plate Count"] = normalizedPlatCount
                new_window.destroy()
    ################################################################################
            def ok_button(row_place):
                bOK = tk.Button(new_window ,text="OK",command=new_ok_button)
                bOK.grid(row=row_place,column=2, padx=10,pady=10,ipadx=15,ipady=5)

            if choice == 1:
                #row 1
                new_window.geometry("800x200")
                question_2_label_1 = tk.Label(new_window, text="Select first octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_1.grid(row=1,column=1,padx=20,pady=10,sticky="w")
                ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent1.grid(row=1, column=2, padx=10)
                b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
                b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 2
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=2, column=1, padx=20,pady=10,sticky="w")
                #row 3
                active_quads_1 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_1.grid(row=3, column=1)
                #row 4
                ok_button(4)


            elif choice == 2:
                new_window.geometry("900x300")
                #row 1
                question_2_label_1 = tk.Label(new_window, text="Select first octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_1.grid(row=1,column=1,padx=25,pady=2,sticky="w")
                ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent1.grid(row=1, column=2, padx=10)
                b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
                b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 2
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=2, column=1, padx=20,pady=10,sticky="w")
                #row 3
                active_quads_1 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_1.grid(row=3, column=1)
                #row 4
                question_2_label_2 = tk.Label(new_window, text="Select second octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_2.grid(row=4,column=1,padx=25,pady=2,sticky="w")
                ent2=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent2.grid(row=4, column=2, padx=10)
                b2 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_2)
                b2.grid(row=4,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 5
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=5, column=1, padx=20,pady=10,sticky="w")
                #row 6
                active_quads_2 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_2.grid(row=6, column=1)
                #row 7
                ok_button(7)

            elif choice == 3:
                new_window.geometry("900x420")
                #row 1
                question_2_label_1 = tk.Label(new_window, text="Select first octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_1.grid(row=1,column=1,padx=25,pady=2,sticky="w")
                ent1=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent1.grid(row=1, column=2, padx=10)
                b1 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_1)
                b1.grid(row=1,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 2
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=2, column=1, padx=20,pady=10,sticky="w")
                #row 3
                active_quads_1 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_1.grid(row=3, column=1)
                #row 4
                question_2_label_2 = tk.Label(new_window, text="Select second octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_2.grid(row=4,column=1,padx=25,pady=2,sticky="w")
                ent2=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent2.grid(row=4, column=2, padx=10)
                b2 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_2)
                b2.grid(row=4,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 5
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=5, column=1, padx=20,pady=10,sticky="w")
                #row 6
                active_quads_2 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_2.grid(row=6, column=1)
                #row 7
                question_2_label_3 = tk.Label(new_window, text="Select third octet quant file: ",  font=("Arial", 14), background=backgroundColor)
                question_2_label_3.grid(row=7,column=1,padx=25,pady=5,sticky="w")
                ent3=tk.Label(new_window, font=12, text="                                                             ", background="white", borderwidth=3, relief="sunken")
                ent3.grid(row=7, column=2, padx=10)
                b3 = tk.Button(new_window ,background="white", text="Browse",command=browse_file_3)
                b3.grid(row=7,column=3, padx=10,pady=10,ipadx=15,ipady=5)
                #row 8
                active_quads_label = tk.Label(new_window, text="How many active quads are in this file?", font=("Arial", 14), background=backgroundColor)
                active_quads_label.grid(row=8, column=1, padx=20,pady=10,sticky="w")
                #row 9
                active_quads_3 = ttk.Combobox(new_window, values=["1", "2", "3", "4"])
                active_quads_3.grid(row=9, column=1)
                #row 10
                ok_button(10)

        question_1_selected()

        


    first_frame = tk.Frame(background=backgroundColor)
    question_1_label = tk.Label(master=first_frame, text="How many octet files need parsed (Max 3 files)?", font=("Arial", 14), background=backgroundColor)
    question_1_label.grid(columnspan=2, row=3, padx=paddingX, pady=paddingY, sticky="w")

    question_1_answer = tk.IntVar()
    tk.Radiobutton(master=first_frame, text="1", variable=question_1_answer, value=1, font=("Arial", 14), background=backgroundColor, command=open_fileInput).grid(row=3, column=2, sticky="w")
    tk.Radiobutton(master=first_frame, text="2", variable=question_1_answer, value=2, font=("Arial", 14), background=backgroundColor, command=open_fileInput).grid(row=3, column=3, sticky="w")
    tk.Radiobutton(master=first_frame, text="3", variable=question_1_answer, value=3, font=("Arial", 14), background=backgroundColor, command=open_fileInput).grid(row=3, column=4, sticky="w")
    first_frame.grid(row=3, column=1, sticky="w")


    #######################################################################################################################
    #Norm Vars
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
    second_frame.grid(row=4, column=1, sticky="w")

    #######################################################################################################################

    def submitForum():
        Octet_Info_Dict["OctetPlateCount"] = question_1_answer.get()
        Octet_Info_Dict["targetVol"] = targetVol.get()
        Octet_Info_Dict["targetConc"] = targetConc.get()
        Octet_Info_Dict["neatTransfer"] = neatTransfer.get()

        master.destroy()


    bOK = tk.Button(master ,text="OK",command=submitForum)
    bOK.grid(row=25, column=1, padx=10,pady=10,ipadx=15,ipady=5)


    progressBarGreen =tk.Frame(master, bg="green", height=12, width=205)
    progressBarWhite =tk.Frame(master, bg="white", height=12, width=200)
    progressPercent = tk.Label(master, text="50%",  font=("Arial", 10), background=backgroundColor, foreground="white")
    progressPercent.place(x=415, y=310)
    progressBarGreen.place(x=10, y=310)
    progressBarWhite.place(x=215, y=310)

    master.mainloop()
    return Octet_Info_Dict





#normVariablesForOctet.py