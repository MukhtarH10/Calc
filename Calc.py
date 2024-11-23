import tkinter as tk

# Global variable to store the current calculation
calculation = ""  # Initialize the calculation variable

# Handles logic for adding numbers/operators to the display field
def add_to_calculation(symbol):
    global calculation
    # Adds the pressed button's symbol to the calculation string
    calculation += str(symbol)
    # Clear the current text in the result display
    text_result.delete(1.0, "end")
    # Update the display with the new calculation string
    text_result.insert(1.0, calculation)

# Evaluates the mathematical expression in the calculation string
def evaluate_calculation():
    global calculation
    try:
        # Evaluate the calculation string and store the result
        calculation = str(eval(calculation))
        # Clear the current text in the result display
        text_result.delete(1.0, "end")
        # Display the result of the calculation
        text_result.insert(1.0, calculation)
    except:
        # If an error occurs (e.g., invalid expression), clear the field
        clear_field()
        # Display an error message
        text_result.insert(1.0, "error")

# Clears the calculation string and the display field
def clear_field():
    global calculation
    # Reset the calculation string to empty
    calculation = ""
    # Clear the current text in the result display
    text_result.delete(1.0, "end")

# Initializes the main application window
window = tk.Tk()
# Sets the dimensions of the window
window.geometry("300x275")

# Creates a multi-line text box to display the current calculation or result
text_result = tk.Text(window, height=2, width=16, font=("Arial", 24))
# Ensures the text box spans across multiple columns in the grid layout
text_result.grid(columnspan=5)

# Buttons for digits 1-9 and 0, each adding their number to the calculation
button_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14), bg="turquoise")
button_1.grid(row=2, column=1)

button_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14), bg="turquoise")
button_2.grid(row=2, column=2)

button_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14), bg="turquoise")
button_3.grid(row=2, column=3)

button_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14), bg="turquoise")
button_4.grid(row=3, column=1)

button_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14), bg="turquoise")
button_5.grid(row=3, column=2)

button_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14), bg="turquoise")
button_6.grid(row=3, column=3)

button_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14), bg="turquoise")
button_7.grid(row=4, column=1)

button_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14), bg="turquoise")
button_8.grid(row=4, column=2)

button_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14), bg="turquoise")
button_9.grid(row=4, column=3)

button_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14), bg="turquoise")
button_0.grid(row=5, column=2)

# Buttons for mathematical operators (+, -, *, /) and parentheses
button_plus = tk.Button(window, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14), bg="orange")
button_plus.grid(row=2, column=4)

button_minus = tk.Button(window, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14), bg="orange")
button_minus.grid(row=3, column=4)

button_mult = tk.Button(window, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14), bg="orange")
button_mult.grid(row=4, column=4)

button_div = tk.Button(window, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14), bg="orange")
button_div.grid(row=5, column=4)

button_open = tk.Button(window, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14), bg="orange")
button_open.grid(row=5, column=1)

button_close = tk.Button(window, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14), bg="orange")
button_close.grid(row=5, column=3)

# Equals Button
button_equals = tk.Button(window, text="=", command=evaluate_calculation, width=11, font=("Arial", 14), bg="green", fg="white")
button_equals.grid(row=6, column=3, columnspan=2)

# Clear Button
button_clear = tk.Button(window, text="C", command=clear_field, width=11, font=("Arial", 14), bg="red", fg="white")
button_clear.grid(row=6, column=1, columnspan=2)

# Starts the Tkinter event loop to display the window and handle user interactions
window.mainloop()
