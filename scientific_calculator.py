import tkinter as tk
from tkinter import TclError
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibya Scientific Calculator")
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#2a2a2a")  # Dark gray casing

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Main Frame for Casing
        casing = tk.Frame(self.root, bg="#2a2a2a", bd=10, relief="raised")
        casing.pack(padx=15, pady=15, fill="both", expand=True)

        # Display Frame
        display_frame = tk.Frame(casing, bg="#1c2526")
        display_frame.pack(pady=20, padx=20, fill="x")

        # Display Entry
        entry_field = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Arial", 20, "bold"),
            bg="#e0f7fa",
            fg="#000000",
            bd=0,
            justify="right",
            insertbackground="black",
            width=20
        )
        entry_field.pack(padx=10, pady=10, ipady=15)
        entry_field.config(highlightthickness=2, highlightbackground="#4f5b62")

        # Brand Label
        brand_label = tk.Label(
            casing,
            text="Dibya",
            font=("Arial", 16, "bold italic"),
            fg="#00ffcc",
            bg="#2a2a2a"
        )
        brand_label.place(x=20, y=10)

        # Button Frame
        button_frame = tk.Frame(casing, bg="#2a2a2a")
        button_frame.pack(padx=10, pady=10)

        # Button Layout
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('−', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('⌫', 5, 3),
            ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('√', 4, 4),
            ('x²', 5, 4), ('log', 1, 5), ('ln', 2, 5), ('π', 3, 5),
            ('e', 4, 5), ('!', 5, 5)
        ]

        for (text, row, col) in buttons:
            # Different colors for different button types
            if text in ['C', '⌫']:
                bg_color = "#ff6e40"  # Red for clear/backspace
            elif text in ['+', '−', '×', '÷', '=']:
                bg_color = "#0288d1"  # Blue for operators
            elif text in ['sin', 'cos', 'tan', '√', 'x²', 'log', 'ln', 'π', 'e', '!']:
                bg_color = "#455a64"  # Dark gray for scientific functions
            else:
                bg_color = "#78909c"  # Light gray for numbers

            button = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 12, "bold"),
                bg=bg_color,
                fg="#ffffff",
                bd=0,
                width=5,
                height=2,
                relief="raised",
                command=lambda t=text: self.click(t)
            )
            button.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
            button.config(
                activebackground="#b0bec5",
                highlightthickness=1,
                highlightbackground="#263238"
            )

            # Hover effect
            button.bind("<Enter>", lambda e, b=button: b.config(relief="sunken"))
            button.bind("<Leave>", lambda e, b=button: b.config(relief="raised"))

        # Configure grid weights for uniform button sizes
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)

    def click(self, item):
        if item == 'C':
            self.expression = ""
        elif item == '=':
            try:
                result = self.evaluate_expression()
                self.expression = str(result)
            except Exception:
                self.expression = "Error"
        elif item == '⌫':
            self.expression = self.expression[:-1]
        elif item == 'sin':
            self.expression += "math.sin("
        elif item == 'cos':
            self.expression += "math.cos("
        elif item == 'tan':
            self.expression += "math.tan("
        elif item == '√':
            self.expression += "math.sqrt("
        elif item == 'x²':
            try:
                last_num = self.get_last_number()
                self.expression = self.expression[:-len(last_num)] + f"({last_num}**2)"
            except Exception:
                self.expression = "Error"
        elif item == 'log':
            self.expression += "math.log10("
        elif item == 'ln':
            self.expression += "math.log("
        elif item == 'π':
            self.expression += "math.pi"
        elif item == 'e':
            self.expression += "math.e"
        elif item == '!':
            try:
                last_num = self.get_last_number()
                self.expression = self.expression[:-len(last_num)] + f"math.factorial(int({last_num}))"
            except Exception:
                self.expression = "Error"
        elif item == '÷':
            self.expression += "/"
        elif item == '×':
            self.expression += "*"
        elif item == '−':
            self.expression += "-"
        else:
            self.expression += item

        self.input_text.set(self.expression)

    def get_last_number(self):
        num = ""
        for char in reversed(self.expression):
            if char in "0123456789.":
                num = char + num
            else:
                break
        return num

    def evaluate_expression(self):
        try:
            expr = self.expression.replace('×', '*').replace('÷', '/').replace('−', '-')
            return eval(expr, {"__builtins__": None}, {
                "math": math,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "log10": math.log10,
                "pi": math.pi,
                "e": math.e,
                "factorial": math.factorial
            })
        except Exception:
            return "Error"

if __name__ == "__main__":
	
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()