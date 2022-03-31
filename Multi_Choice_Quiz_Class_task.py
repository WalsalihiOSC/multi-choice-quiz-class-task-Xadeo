#Starting Week 9 task 1

from tkinter import *

class Multi_ChoiceGUI:
    def __init__(self, parent):
        self.choice_var = StringVar()
        self.choice_var.set("")
        
        self.font = ("Comic Sans MS", "10", "bold")

        prompt_Label = Label(parent, text = "Question.")
        prompt_Label.grid(row = 0, column = 0)

        quesiton_Label = Label(parent, text = "What is the capital of Mongolia?", font = self.font,  width = 40, height = 30)
        quesiton_Label.grid(row = 0, column = 1)



#main routine
if __name__ == "__main__":        
    root = Tk()
    Multi_Choice = Multi_ChoiceGUI(root)
    root.mainloop()