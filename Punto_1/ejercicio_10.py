import tkinter as tk

class Matricula:
    def __init__(self, ni, nom, pat, estr):
        self.ni = ni
        self.nom = nom
        self.pat = pat
        self.estr = estr
        self.matricu = 50000

    def calcular_matricula(self):
        if self.pat > 2000000 and self.estr > 3:
            self.matricu = self.matricu + (0.03 * self.pat)
        else:
            self.matricu = 50000
        return self.matricu

class MatriculaApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 10")

        tk.Label(raiz, text="Número de inscripción:").grid(row=0, column=0, padx=10, pady=5)
        self.ni_entry = tk.Entry(raiz)
        self.ni_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.nom_entry = tk.Entry(raiz)
        self.nom_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
        self.pat_entry = tk.Entry(raiz)
        self.pat_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(raiz, text="Estrato:").grid(row=3, column=0, padx=10, pady=5)
        self.estr_entry = tk.Entry(raiz)
        self.estr_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(raiz, text="Calcular", command=self.calcular).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(raiz, text="Limpiar", command=self.limpiar).grid(row=4, column=1, padx=10, pady=5)

        self.result_label = tk.Label(raiz, text="Matrícula: -")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            ni = self.ni_entry.get()
            nom = self.nom_entry.get()
            pat = float(self.pat_entry.get())
            estr = int(self.estr_entry.get())

            matricula = Matricula(ni, nom, pat, estr)
            resultado = matricula.calcular_matricula()

            self.result_label.config(text=f"Matrícula: {resultado:.2f}")
        except (ValueError, TypeError):
            self.result_label.config(text="Matrícula: NaN")

    def limpiar(self):

        self.ni_entry.delete(0, tk.END)
        self.nom_entry.delete(0, tk.END)
        self.pat_entry.delete(0, tk.END)
        self.estr_entry.delete(0, tk.END)
        self.result_label.config(text="Recibo: -")

raiz = tk.Tk()
app = MatriculaApp(raiz)
raiz.mainloop()
