import tkinter as tk

class Empleado:
    def __init__(self, codigo, nombre, numhoras, valhoras, retencion):
        self.codigo = codigo
        self.nombre = nombre
        self.numhoras = numhoras
        self.valhoras = valhoras
        self.retencion = retencion

    def salario_bruto(self):
        return self.numhoras * self.valhoras

    def salario_neto(self, sal_bruto):
        return sal_bruto - (sal_bruto * self.retencion / 100)

class EmpleadoApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 18")

        tk.Label(raiz, text="Código:").grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entry = tk.Entry(raiz)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(raiz)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Horas trabajadas:").grid(row=2, column=0, padx=10, pady=5)
        self.numhoras_entry = tk.Entry(raiz)
        self.numhoras_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Valor por hora:").grid(row=3, column=0, padx=10, pady=5)
        self.valhoras_entry = tk.Entry(raiz)
        self.valhoras_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Retención (%):").grid(row=4, column=0, padx=10, pady=5)
        self.retencion_entry = tk.Entry(raiz)
        self.retencion_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=5, column=1, padx=10, pady=5)

        self.result_bruto = tk.Label(raiz, text="Salario Bruto: -")
        self.result_bruto.grid(row=6, column=0, columnspan=2, pady=5)

        self.result_neto = tk.Label(raiz, text="Salario Neto: -")
        self.result_neto.grid(row=7, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            
            codigo = int(self.codigo_entry.get())
            nombre = self.nombre_entry.get()
            numhoras = float(self.numhoras_entry.get())
            valhoras = float(self.valhoras_entry.get())
            retencion = float(self.retencion_entry.get())

            empleado = Empleado(codigo, nombre, numhoras, valhoras, retencion)
            sal_bruto = empleado.salario_bruto()
            sal_neto = empleado.salario_neto(sal_bruto)

            self.result_bruto.config(text=f"Salario Bruto: {sal_bruto:.2f}")
            self.result_neto.config(text=f"Salario Neto: {sal_neto:.2f}")
        except ValueError:
    
            self.result_bruto.config(text="Salario Bruto: NaN")
            self.result_neto.config(text="Salario Neto: NaN")

    def limpiar(self):
        
        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.numhoras_entry.delete(0, tk.END)
        self.valhoras_entry.delete(0, tk.END)
        self.retencion_entry.delete(0, tk.END)
        self.result_bruto.config(text="Salario Bruto: -")
        self.result_neto.config(text="Salario Neto: -")

raiz = tk.Tk()
app = EmpleadoApp(raiz)
raiz.mainloop()
