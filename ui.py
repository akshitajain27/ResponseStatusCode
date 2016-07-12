import Tkinter


class simpleapp_tk(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()

    def initialize(self):
        self.grid()
        button = Tkinter.Button(self,text=u"Button",width=30,
                                command=self.OnButtonClick)

        button.grid(column=1,row=0)


        self.labelVariable = Tkinter.StringVar()
        label3 = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w")
        label3.grid(column=0,row=1,columnspan=2,sticky='EW')


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)

    def OnButtonClick(self):

        for i in range(1,5):
            import code
        #from code import status_code

            a= code.status_code()
            print a

            self.labelVariable.set(a)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('status code')
    app.geometry("500x400")
    app.mainloop()
