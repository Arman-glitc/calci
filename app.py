import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        
        self.display = tk.Entry(root, font=("Helvetica", 16), borderwidth=5, relief=tk.RIDGE)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val == 4:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, col):
        if value == "=":
            btn = tk.Button(self.root, text=value, width=10, height=3, command=self.evaluate)
        else:
            btn = tk.Button(self.root, text=value, width=10, height=3, command=lambda: self.click(value))
        
        btn.grid(row=row, column=col)

    def click(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = ""
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
