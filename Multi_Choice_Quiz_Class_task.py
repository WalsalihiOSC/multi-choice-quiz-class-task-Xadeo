#Starting Week 9 task 1

from tkinter import *

class Multi_ChoiceGUI:
    def __init__(self, parent):
        self.choice_var = StringVar()
        self.choice_var.set("")
        
        font = ("Comic Sans MS", "10", "bold")

        RBchoices_list = ["Vladivostok", "Astana", "Ulaanbaatar", "Lhasa"]

        prompt_Label = Label(parent, text = "Question.", font = font)
        prompt_Label.grid(row = 0, column = 0)

        quesiton_Label = Label(parent, text = "What is the capital of Mongolia?", font = font,  width = 30, height = 1)
        quesiton_Label.grid(row = 0, column = 1)

        for choice in range(len(RBchoices_list)):
            RBbtn = Radiobutton(parent, variable = self.choice_var, value = str(RBchoices_list[choice]), text = str(RBchoices_list[choice]),
                                command = self.display_answer)
            RBbtn.grid(row = 1 + choice, column = 1, sticky = N)

        self.output_label = Label(parent, text = "Let's see if your knowlegde is impressive!", font = font)
        self.output_label.grid(row = 5, column = 1, sticky = N)
    
    def display_answer(self):
        if str(self.choice_var.get()) == "Ulaanbaatar":
            self.output_label.configure(text = str(self.choice_var.get()) + " is correct!!")
        else:
            self.output_label.configure(text = str(self.choice_var.get()) + " is not correct!!")
        
#main routine
if __name__ == "__main__":        
    root = Tk()
    Multi_Choice = Multi_ChoiceGUI(root)
    root.mainloop()