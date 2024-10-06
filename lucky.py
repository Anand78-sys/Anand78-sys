import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.equation = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.equation, width=25, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        buttons = [
            'MC', 'MR', 'M+', 'M-', 'MS', 'Mv',
            '%', 'CE', 'C', '<-', '√x', 'x²',
            '7', '8', '9', '÷', '1/x', '+/-',
            '4', '5', '6', 'x', '(', ')',
            '1', '2', '3', '-', '{', '}',
            '+/-', '0', '.', '+', '=', ''
        ]

        row = 1
        col = 0
        for text in buttons:
            button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                col = 0
                row += 1

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)

    def click(self, text):
        if text == '=':
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except:
                self.equation.set("Error")
        elif text == 'C':
            self.equation.set("")
        elif text == '<-':
            self.equation.set(self.equation.get()[:-1])
        elif text == '√x':
            try:
                self.equation.set(str(float(self.equation.get())**0.5))
            except:
                self.equation.set("Error")
        elif text == 'x²':
            try:
                self.equation.set(str(float(self.equation.get())**2))
            except:
                self.equation.set("Error")
        elif text == '1/x':
            try:
                self.equation.set(str(1/float(self.equation.get())))
            except:
                self.equation.set("Error")
        elif text == '+/-':
            try:
                if self.equation.get()[0] == '-':
                    self.equation.set(self.equation.get()[1:])
                else:
                    self.equation.set('-' + self.equation.get())
            except:
                pass  # Ignore if the input is empty
        else:
            self.equation.set(self.equation.get() + text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()