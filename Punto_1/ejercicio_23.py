import tkinter as tk
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def soluciones(self):
        if self.a == 0:
            return "No es una ecuación cuadrática", None

        discriminante = (self.b ** 2) - (4 * self.a * self.c)
        if discriminante < 0:
            return "No tiene soluciones reales", None

        x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
        x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
        return x1, x2


class EcuacionApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 23")

        
        tk.Label(raiz, text="Valor de A:").grid(row=0, column=0, padx=10, pady=5)
        self.a_entry = tk.Entry(raiz)
        self.a_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Valor de B:").grid(row=1, column=0, padx=10, pady=5)
        self.b_entry = tk.Entry(raiz)
        self.b_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Valor de C:").grid(row=2, column=0, padx=10, pady=5)
        self.c_entry = tk.Entry(raiz)
        self.c_entry.grid(row=2, column=1, padx=10, pady=5)
      
        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=3, column=1, padx=10, pady=5)

        self.resultado_label = tk.Label(raiz, text="Resultado: -", anchor="w", justify="left")
        self.resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def calcular(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            ecuacion = EcuacionCuadratica(a, b, c)
            soluciones = ecuacion.soluciones()

            if isinstance(soluciones, tuple) and soluciones[1] is not None:
                self.resultado_label.config(
                    text=f"Soluciones:\nX1 = {soluciones[0]:.2f}\nX2 = {soluciones[1]:.2f}"
                )
            else:
                self.resultado_label.config(text=f"Resultado: {soluciones[0]}")
        except ValueError:
            self.resultado_label.config(text="Resultado: NaN\nError en los datos de entrada.")

    def limpiar(self):
        
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)
        self.resultado_label.config(text="Resultado: -")

raiz = tk.Tk()
app = EcuacionApp(raiz)
raiz.mainloop()
