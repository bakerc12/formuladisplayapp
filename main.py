
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io


formulas = {
    "Area of a parallelogram": r"A = bh",
    "Area of a triangle": r"A = \frac{1}{2}bh",
    "Area of a trapezoid": r"A = \frac{1}{2}(a + b)h",
    "Area of a circle": r"A = \pi r^2",
    "Circumference of a circle": r"C = 2\pi r",
    "Volume of a cuboid": r"V = lwh",
    "Volume of a cylinder": r"V = \pi r^2h",
    "Volume of prism": r"V = Ah",
    "Area of the curved surface of a cylinder": r"A = 2\pi rh",
    "Distance between two points": r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
    "Coordinates of the midpoint of a line segment": r"\left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)",
    "Solutions of a quadratic equation": r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}, \quad a \neq 0",
    "The nth term of an arithmetic sequence": r"u_n = u_1 + (n - 1)d",
    "The sum of n terms of an arithmetic sequence": r"S_n = \frac{n}{2}(u_1 + (n - 1)d); \quad S_n = \frac{n}{2}(u_1 + u_n)",
    "The nth term of a geometric sequence": r"u_n = u_1 r^{n - 1}",
    "The sum of n terms of a finite geometric sequence": r"S_n = \frac{u_1(1 - r^n)}{1 - r}, \quad r \neq 1; \quad S_n = \frac{u_1(r^n - 1)}{r - 1}, \quad r \neq 1",
    "Compound interest": r"FV = PV \left( 1 + \frac{r}{100k} \right)^{kn}",
    "Exponents and logarithms": r"\log_a x = b \Leftrightarrow a^b = x, \quad a > 0, b > 0, a \neq 1",
    "Percentage error": r"\varepsilon = \frac{v_A - v_E}{v_E} \times 100\%"
}


def latex_to_image(latex_string):
    fig = plt.figure()
    plt.axis('off')
    plt.text(0.5, 0.5, f'${latex_string}$', size=20, ha='center', va='center')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)

    buf.seek(0)
    img = Image.open(buf)
    return img


class FormulaDisplayApp:
    def __init__(self, master):
        self.master = master
        master.title("Formula Display")

        self.label = ttk.Label(master, text="Select a formula:")
        self.label.pack(pady=10)

        self.selected_formula = tk.StringVar()

        self.dropdown = ttk.Combobox(master, textvariable=self.selected_formula)
        self.dropdown['values'] = list(formulas.keys())
        self.dropdown.pack(pady=10)

        self.button = ttk.Button(master, text="Display Formula", command=self.display_formula)
        self.button.pack(pady=10)

        self.image_label = ttk.Label(master)
        self.image_label.pack(pady=10)

    def display_formula(self):
        formula_name = self.selected_formula.get()
        if formula_name in formulas:
            latex_string = formulas[formula_name]
            img = latex_to_image(latex_string)
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference


if __name__ == "__main__":
    root = tk.Tk()
    app = FormulaDisplayApp(root)
    root.mainloop()