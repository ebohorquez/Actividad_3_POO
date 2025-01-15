import tkinter as tk

class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def salario_mensual(self):
        return self.salario_hora * self.horas_trabajadas


class EmpleadoApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 22")

        # Etiquetas y entradas
        tk.Label(raiz, text="Nombre del empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(raiz)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Salario por hora:").grid(row=1, column=0, padx=10, pady=5)
        self.salario_entry = tk.Entry(raiz)
        self.salario_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Horas trabajadas al mes:").grid(row=2, column=0, padx=10, pady=5)
        self.horas_entry = tk.Entry(raiz)
        self.horas_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botones
        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=3, column=1, padx=10, pady=5)

        # Resultados
        self.resultado_label = tk.Label(raiz, text="Resultado: -", anchor="w", justify="left")
        self.resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def calcular(self):
        try:
            nombre = self.nombre_entry.get().strip()
            salario_hora = float(self.salario_entry.get())
            horas_trabajadas = float(self.horas_entry.get())

            empleado = Empleado(nombre, salario_hora, horas_trabajadas)
            salario_mensual = empleado.salario_mensual()

            if salario_mensual > 450000:
                self.resultado_label.config(text=f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:,.2f}")
            else:
                self.resultado_label.config(text=f"Nombre: {nombre}\nSalario Mensual: No aplica.")
        except ValueError:
            self.resultado_label.config(text="Resultado: NaN\nError en los datos de entrada.")

    def limpiar(self):
        # Limpiar entradas y resultados
        self.nombre_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.horas_entry.delete(0, tk.END)
        self.resultado_label.config(text="Resultado: -")


# Crear la ventana principal
raiz = tk.Tk()
app = EmpleadoApp(raiz)
raiz.mainloop()
