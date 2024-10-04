import customtkinter
import math

customtkinter.set_appearance_mode("dark")

# Configure the main window
janela = customtkinter.CTk()
janela.geometry("472x530+423+159")
janela.title("Scientific Calculator")

# Calculator operator
calc_operator = ""


# Function to update text in the display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    output.delete("0.0", "end")
    output.insert("end", calc_operator)


# Function to clear the display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    output.delete("0.0", "end")


# Function to evaluate the current expression
def calcular():
    global calc_operator
    try:
        # Replace custom functions with their math equivalents for eval()
        expression = calc_operator.replace("log", "math.log10").replace("^", "**")
        result = eval(expression)

        # Format large results (show in scientific notation if needed)
        if isinstance(result, float) and len(str(result)) > 10:
            result = f"{result:.5e}"
        else:
            result = str(result)

        output.delete("0.0", "end")
        output.insert("end", result)
        calc_operator = result
    except ZeroDivisionError:
        output.delete("0.0", "end")
        output.insert("end", "ERROR: Div by 0")
        calc_operator = ""
    except Exception as e:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


# Function for factorial
def fact_func():
    global calc_operator
    try:
        result = str(math.factorial(int(calc_operator)))
        output.delete("0.0", "end")
        output.insert("end", result)
        calc_operator = result
    except ValueError:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""
    except Exception:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


# Function to handle trigonometry
def trig_func(trig_type):
    global calc_operator
    try:
        if calc_operator:  # Ensure calc_operator has a value
            angle = float(calc_operator)
            if trig_type == "sin":
                result = str(math.sin(math.radians(angle)))
            elif trig_type == "cos":
                result = str(math.cos(math.radians(angle)))
            elif trig_type == "tan":
                result = str(math.tan(math.radians(angle)))

            if len(result) > 10:
                result = f"{float(result):.5e}"  # Format large trigonometric results

            output.delete("0.0", "end")
            output.insert("end", result)
            calc_operator = result
        else:
            raise ValueError  # Handle empty calc_operator
    except Exception:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


# Function to calculate square root
def square_root():
    global calc_operator
    try:
        result = str(math.sqrt(float(calc_operator)))
        output.delete("0.0", "end")
        output.insert("end", result)
        calc_operator = result
    except ValueError:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""
    except:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


# Function for logarithm (log base 10)
def log_func():
    global calc_operator
    try:
        result = str(math.log10(float(calc_operator)))
        output.delete("0.0", "end")
        output.insert("end", result)
        calc_operator = result
    except ValueError:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""
    except:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


# Function for power (x^y)
def pow_func():
    global calc_operator
    try:
        calc_operator += "**"
        output.delete("0.0", "end")
        output.insert("end", calc_operator)
    except:
        output.delete("0.0", "end")
        output.insert("end", "ERROR")
        calc_operator = ""


output = customtkinter.CTkTextbox(
    janela,
    width=440,
    height=70,
    corner_radius=10,
    border_width=5,
    border_color="#042940",
    font=(("Arial", 35)),
)
output.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# Numeric buttons and operator buttons
button_list = [
    ("1", 1, 0),
    ("2", 1, 1),
    ("3", 1, 2),
    ("(", 1, 3),
    (")", 1, 4),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("+", 2, 3),
    ("-", 2, 4),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 3, 2),
    ("*", 3, 3),
    ("/", 3, 4),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2, calcular),
    ("C", 4, 3, button_clear_all),
]

# Dynamically generate buttons with different colors and styling
for text, row, col, *action in button_list:
    if action:
        command = action[0]
    else:
        command = lambda t=text: button_click(t)
    btn = customtkinter.CTkButton(
        janela,
        text=text,
        command=command,
        corner_radius=15,
        width=85,
        height=60,
        fg_color="#333333",
        hover_color="#444444",
        text_color="white",
        font=(("arial", 25)),
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Scientific buttons (Factorial, Square Root, Trigonometry, Log, Power)
btn_factorial = customtkinter.CTkButton(
    janela,
    text="x!",
    command=fact_func,
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",  # Blue for scientific buttons
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_factorial.grid(row=5, column=0, padx=5, pady=5)

btn_sqrt = customtkinter.CTkButton(
    janela,
    text="√",
    command=square_root,
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_sqrt.grid(row=5, column=1, padx=5, pady=5)

btn_sin = customtkinter.CTkButton(
    janela,
    text="sin",
    command=lambda: trig_func("sin"),
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_sin.grid(row=5, column=2, padx=5, pady=5)

btn_cos = customtkinter.CTkButton(
    janela,
    text="cos",
    command=lambda: trig_func("cos"),
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_cos.grid(row=5, column=3, padx=5, pady=5)

btn_tan = customtkinter.CTkButton(
    janela,
    text="tan",
    command=lambda: trig_func("tan"),
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_tan.grid(row=5, column=4, padx=5, pady=5)

btn_log = customtkinter.CTkButton(
    janela,
    text="log",
    command=log_func,
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_log.grid(row=6, column=0, padx=5, pady=5)

btn_pow = customtkinter.CTkButton(
    janela,
    text="^",
    command=pow_func,
    corner_radius=15,
    width=85,
    height=60,
    fg_color="#1e81b0",
    hover_color="#16658c",
    text_color="white",
    font=(("arial", 25)),
)
btn_pow.grid(row=6, column=1, padx=5, pady=5)

janela.mainloop()
