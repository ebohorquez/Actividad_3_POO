import tkinter as tk
import math

class Triangulo:
    def __init__(self, lado):
        self.lado = lado
        self.altura1 = 0.0
        self.area1 = 0.0

    def perimetro(self):
        return self.lado * 3

    def altura(self):
        self.altura1 = math.sqrt((self.lado**2) - ((self.lado / 2)**2))
        return self.altura1

    def area(self):
        self.area1 = (self.lado * self.altura1) / 2
        return self.area1

class TrianguloApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 19")

        tk.Label(raiz, text="Lado del triángulo:").grid(row=0, column=0, padx=10, pady=5)
        self.lado_entry = tk.Entry(raiz)
        self.lado_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=1, column=1, padx=10, pady=5)

        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=2, column=0, columnspan=2, pady=5)

        self.result_altura = tk.Label(raiz, text="Altura: -")
        self.result_altura.grid(row=3, column=0, columnspan=2, pady=5)

        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=4, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            
            lado = float(self.lado_entry.get())
            if lado <= 0:
                raise ValueError()

            triangulo = Triangulo(lado)
            perimetro = triangulo.perimetro()
            altura = triangulo.altura()
            area = triangulo.area()

            self.result_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
            self.result_altura.config(text=f"Altura: {altura:.2f}")
            self.result_area.config(text=f"Área: {area:.2f}")
        except (ValueError, TypeError):
            
            self.result_perimetro.config(text="Perímetro: NaN")
            self.result_altura.config(text="Altura: NaN")
            self.result_area.config(text="Área: NaN")

    def limpiar(self):
        
        self.lado_entry.delete(0, tk.END)
        self.result_perimetro.config(text="Perímetro: -")
        self.result_altura.config(text="Altura: -")
        self.result_area.config(text="Área: -")

raiz = tk.Tk()
app = TrianguloApp(raiz)
raiz.mainloop()