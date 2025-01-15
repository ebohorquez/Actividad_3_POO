import tkinter as tk
from tkinter import ttk
import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()
    
    def tipo_triangulo(self):
        hipotenusa = self.hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"


class Rombo:
    def __init__(self, diagonal_max, diagonal_min, lado):
        self.diagonal_max = diagonal_max
        self.diagonal_min = diagonal_min
        self.lado = lado

    def area(self):
        return (self.diagonal_max * self.diagonal_min) / 2

    def perimetro(self):
        return 4 * self.lado


class Trapecio:
    def __init__(self, base_max, base_min, lado_izq, lado_dere, altura):
        self.base_max = base_max
        self.base_min = base_min
        self.lado_izq = lado_izq
        self.lado_dere = lado_dere
        self.altura = altura

    def area(self):
        return ((self.base_max + self.base_min) * self.altura) / 2

    def perimetro(self):
        return self.base_max + self.base_min + self.lado_izq + self.lado_dere


class MDIApp:
    def __init__(self, raiz):
        raiz.geometry("300x300")
        self.raiz = raiz
        self.raiz.title("Gestión Figuras Geométricas")
        
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.raiz)
        self.raiz.config(menu=menu_bar)

        figuras_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Figuras", menu=figuras_menu)

        figuras_menu.add_command(label="Círculo", command=self.abrir_circulo)
        figuras_menu.add_command(label="Rectángulo", command=self.abrir_rectangulo)
        figuras_menu.add_command(label="Cuadrado", command=self.abrir_cuadrado)
        figuras_menu.add_command(label="Triángulo Rectángulo", command=self.abrir_triangulo)
        figuras_menu.add_command(label="Rombo", command=self.abrir_rombo)
        figuras_menu.add_command(label="Trapecio", command=self.abrir_trapecio)

    def abrir_circulo(self):
        ventana = tk.Toplevel(self.raiz)
        CirculoInterface(ventana)

    def abrir_rectangulo(self):
        ventana = tk.Toplevel(self.raiz)
        RectanguloInterface(ventana)

    def abrir_cuadrado(self):
        ventana = tk.Toplevel(self.raiz)
        CuadradoInterface(ventana)

    def abrir_triangulo(self):
        ventana = tk.Toplevel(self.raiz)
        TrianguloInterface(ventana)

    def abrir_rombo(self):
        ventana = tk.Toplevel(self.raiz)
        RomboInterface(ventana)

    def abrir_trapecio(self):
        ventana = tk.Toplevel(self.raiz)
        TrapecioInterface(ventana)


class CirculoInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Círculo")
        tk.Label(raiz, text="Radio:").grid(row=0, column=0)
        self.radio_entry = tk.Entry(raiz)
        self.radio_entry.grid(row=0, column=1,)
        
        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=1, column=0, columnspan=2)
        
        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=2, column=0, columnspan=2)
        
        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=3, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=3, column=1)

    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            circulo = Circulo(radio)
            self.result_area.config(text=f"Área: {circulo.area():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {circulo.perimetro():.2f}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")

    def limpiar(self):
        self.radio_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_perimetro.config(text="Perímetro: -")


class RectanguloInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Rectángulo")
        tk.Label(raiz, text="Base:").grid(row=0, column=0)
        self.base_entry = tk.Entry(raiz)
        self.base_entry.grid(row=0, column=1)

        tk.Label(raiz, text="Altura:").grid(row=1, column=0)
        self.altura_entry = tk.Entry(raiz)
        self.altura_entry.grid(row=1, column=1)
        
        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=2, column=0, columnspan=2)
        
        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=3, column=0, columnspan=2)
        
        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=4, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=4, column=1)

    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            rectangulo = Rectangulo(base, altura)
            self.result_area.config(text=f"Área: {rectangulo.area():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {rectangulo.perimetro():.2f}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")

    def limpiar(self):
        self.base_entry.delete(0, tk.END)
        self.altura_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_perimetro.config(text="Perímetro: -")


class CuadradoInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Cuadrado")
        tk.Label(raiz, text="Lado:").grid(row=0, column=0)
        self.lado_entry = tk.Entry(raiz)
        self.lado_entry.grid(row=0, column=1)
        
        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=1, column=0, columnspan=2)
        
        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=2, column=0, columnspan=2)
        
        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=3, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=3, column=1)

    def calcular(self):
        try:
            lado = float(self.lado_entry.get())
            cuadrado = Cuadrado(lado)
            self.result_area.config(text=f"Área: {cuadrado.area():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {cuadrado.perimetro():.2f}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")

    def limpiar(self):
        self.lado_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_perimetro.config(text="Perímetro: -")


class TrianguloInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Triángulo Rectángulo")
        tk.Label(raiz, text="Base:").grid(row=0, column=0)
        self.base_entry = tk.Entry(raiz)
        self.base_entry.grid(row=0, column=1)

        tk.Label(raiz, text="Altura:").grid(row=1, column=0)
        self.altura_entry = tk.Entry(raiz)
        self.altura_entry.grid(row=1, column=1)

        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=2, column=0, columnspan=2)

        self.result_hipotenusa = tk.Label(raiz, text="Hipotenusa: -")
        self.result_hipotenusa.grid(row=3, column=0, columnspan=2)

        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=4, column=0, columnspan=2)

        self.result_tipo = tk.Label(raiz, text="Tipo: -")
        self.result_tipo.grid(row=5, column=0, columnspan=2)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=6, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=6, column=1)

    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            triangulo = TrianguloRectangulo(base, altura)

            self.result_area.config(text=f"Área: {triangulo.area():.2f}")
            self.result_hipotenusa.config(text=f"Hipotenusa: {triangulo.hipotenusa():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {triangulo.perimetro():.2f}")
            self.result_tipo.config(text=f"Tipo: {triangulo.tipo_triangulo()}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_hipotenusa.config(text="Hipotenusa: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")
            self.result_tipo.config(text="Tipo: -")

    def limpiar(self):
        self.base_entry.delete(0, tk.END)
        self.altura_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_hipotenusa.config(text="Hipotenusa: -")
        self.result_perimetro.config(text="Perímetro: -")
        self.result_tipo.config(text="Tipo: -")


class RomboInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Rombo")
        tk.Label(raiz, text="Diagonal Mayor:").grid(row=0, column=0)
        self.diagonal_mayor_entry = tk.Entry(raiz)
        self.diagonal_mayor_entry.grid(row=0, column=1)

        tk.Label(raiz, text="Diagonal Menor:").grid(row=1, column=0)
        self.diagonal_menor_entry = tk.Entry(raiz)
        self.diagonal_menor_entry.grid(row=1, column=1)

        tk.Label(raiz, text="Lado:").grid(row=2, column=0)
        self.lado_entry = tk.Entry(raiz)
        self.lado_entry.grid(row=2, column=1)

        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=3, column=0, columnspan=2)

        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=4, column=0, columnspan=2)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=5, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=5, column=1)

    def calcular(self):
        try:
            diagonal_mayor = float(self.diagonal_mayor_entry.get())
            diagonal_menor = float(self.diagonal_menor_entry.get())
            lado = float(self.lado_entry.get())
            rombo = Rombo(diagonal_mayor, diagonal_menor, lado)

            self.result_area.config(text=f"Área: {rombo.area():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {rombo.perimetro():.2f}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")

    def limpiar(self):
        self.diagonal_mayor_entry.delete(0, tk.END)
        self.diagonal_menor_entry.delete(0, tk.END)
        self.lado_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_perimetro.config(text="Perímetro: -")


class TrapecioInterface:
    def __init__(self, raiz):
        raiz.geometry("300x200")
        raiz.title("Trapecio")
        tk.Label(raiz, text="Base Mayor:").grid(row=0, column=0)
        self.base_mayor_entry = tk.Entry(raiz)
        self.base_mayor_entry.grid(row=0, column=1)

        tk.Label(raiz, text="Base Menor:").grid(row=1, column=0)
        self.base_menor_entry = tk.Entry(raiz)
        self.base_menor_entry.grid(row=1, column=1)

        tk.Label(raiz, text="Altura:").grid(row=2, column=0)
        self.altura_entry = tk.Entry(raiz)
        self.altura_entry.grid(row=2, column=1)

        tk.Label(raiz, text="Lado 1:").grid(row=3, column=0)
        self.lado1_entry = tk.Entry(raiz)
        self.lado1_entry.grid(row=3, column=1)

        tk.Label(raiz, text="Lado 2:").grid(row=4, column=0)
        self.lado2_entry = tk.Entry(raiz)
        self.lado2_entry.grid(row=4, column=1)

        self.result_area = tk.Label(raiz, text="Área: -")
        self.result_area.grid(row=5, column=0, columnspan=2)

        self.result_perimetro = tk.Label(raiz, text="Perímetro: -")
        self.result_perimetro.grid(row=6, column=0, columnspan=2)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=7, column=0)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=7, column=1)

    def calcular(self):
        try:
            base_mayor = float(self.base_mayor_entry.get())
            base_menor = float(self.base_menor_entry.get())
            altura = float(self.altura_entry.get())
            lado1 = float(self.lado1_entry.get())
            lado2 = float(self.lado2_entry.get())
            trapecio = Trapecio(base_mayor, base_menor, altura, lado1, lado2)

            self.result_area.config(text=f"Área: {trapecio.area():.2f}")
            self.result_perimetro.config(text=f"Perímetro: {trapecio.perimetro():.2f}")
        except ValueError:
            self.result_area.config(text="Área: NaN")
            self.result_perimetro.config(text="Perímetro: NaN")

    def limpiar(self):
        self.base_mayor_entry.delete(0, tk.END)
        self.base_menor_entry.delete(0, tk.END)
        self.altura_entry.delete(0, tk.END)
        self.lado1_entry.delete(0, tk.END)
        self.lado2_entry.delete(0, tk.END)
        self.result_area.config(text="Área: -")
        self.result_perimetro.config(text="Perímetro: -")

if __name__ == "__main__":
    raiz = tk.Tk()
    app = MDIApp(raiz)
    raiz.mainloop()
