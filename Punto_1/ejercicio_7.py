import tkinter as tk

class Numero:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparacion(self):
        if self.a > self.b:
            return f"{self.a} es mayor que {self.b}"
        elif self.a == self.b:
            return f"{self.a} es igual que {self.b}"
        else:
            return f"{self.a} es menor que {self.b}"

class NumeroApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 7")

        tk.Label(raiz, text="Número A:").grid(row=0, column=0, padx=10, pady=5)
        self.a_entry = tk.Entry(raiz)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Número B:").grid(row=1, column=0, padx=10, pady=5)
        self.b_entry = tk.Entry(raiz)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=2, column=1, padx=10, pady=5)

        self.result_label = tk.Label(raiz, text="Resultado: -")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())

            numero = Numero(a, b)
            resultado = numero.comparacion()

            self.result_label.config(text=f"Resultado: {resultado}")

        except ValueError:
            self.result_label.config(text="Resultado: NaN")

    def limpiar(self):

        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.result_label.config(text="Resultado: -")

root = tk.Tk()
app = NumeroApp(root)
root.mainloop()
