from tkinter import*


def convert():
    celTemp= celTempVar.get()
    fahTemp= fahTempVar.get()



    if celTempVar.get() != 0.0:
        celToFah = (celTemp *  9/5 + 32)
        print(celToFah)
        fahTempVar.set(celToFah)

    elif fahTempVar.get() != 0.0:
        fahToCel = ((fahTemp - 32) * (5/9))
        print(fahToCel)
        celTempVar.set(fahToCel)


def reset():
    top = Toplevel(padx=50, pady=50)
    top.grid()
    message = Label(top, text = "Reset Complete")
    button = Button(top, text="OK", command=top.destroy)

    message.grid(row = 0, padx = 5, pady = 5)
    button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

    fahTempVar.set(int(0))
    celTempVar.set(int(0))





###MAIN###
root= Tk()
root.title("Temperature Conversion")
mainframe= Frame(root)
mainframe.grid()

celTempVar = IntVar()
celTempVar.set(int(0))
fahTempVar = IntVar()
fahTempVar.set(int(0))


titleLabel = Label (mainframe, text = "Celcius/Fahrenheit Converter", font = ("Arial", 20, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

celLabel = Label (mainframe, text = "°C: ", font = ("Arial", 16), fg = "red")
celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

fahLabel = Label (mainframe, text = "°F: ", font = ("Arial", 16), fg = "blue")
fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

celEntry = Entry (mainframe, width = 10, bd = 5, textvariable = celTempVar)
celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


fahEntry = Entry (mainframe, width = 10, bd = 5, textvariable = fahTempVar)
fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

convertButton =Button (mainframe, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "black", overrelief = GROOVE, activebackground = "white", activeforeground="#65ff00", command = convert)
convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

resetButton = Button (mainframe, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "black", overrelief = GROOVE, activebackground = "white", activeforeground="#65ff00", command = reset)
resetButton.grid(row = 5, column = 1,ipady = 8, ipadx = 12, pady = 5, sticky = NW)

root.mainloop()
