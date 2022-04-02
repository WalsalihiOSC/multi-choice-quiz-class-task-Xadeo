#Starting Week 9 task 1

from tkinter import *

class Multi_ChoiceGUI:
    def __init__(self, parent):
        self.choice_var = StringVar()
        self.choice_var.set("")
        
        font = ("Comic Sans MS", "10", "bold")

        self.RBchoices_list = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]

        prompt_Label = Label(parent, text = "Question.", font = font)
        prompt_Label.grid(row = 0, column = 0)

        quesiton_Label = Label(parent, text = "What is the capital of Mongolia?", font = font,  width = 30, height = 1)
        quesiton_Label.grid(row = 0, column = 1)

        for choice in range(len(self.RBchoices_list)):
            RBbtn = Radiobutton(parent, variable = self.choice_var, value = str(self.RBchoices_list[choice]), text = str(self.RBchoices_list[choice])
                                        )
            RBbtn.grid(row = 1 + choice, column = 1, sticky = N)

        self.output_label = Label(parent, text = "Let's see if your knowlegde is impressive!", font = font)
        self.output_label.grid(row = 5, column = 1, sticky = N)


#main routine
if __name__ == "__main__":        
    root = Tk()
    Multi_Choice = Multi_ChoiceGUI(root)
    root.mainloop()