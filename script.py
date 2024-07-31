import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        
        cm = float(entry_cm.get())
      
        metros = cm / 100

        label_resultado.config(text=f"{cm} cm é igual a {metros:.2f} metros")
    except ValueError:
       
        messagebox.showerror("Erro", "Por favor, insira um número válido.")


root = tk.Tk()
root.title("Conversor de Centímetros para Metros")


label_cm = tk.Label(root, text="Centímetros:")
entry_cm = tk.Entry(root)
button_converter = tk.Button(root, text="Converter", command=converter)
label_resultado = tk.Label(root, text="")


label_cm.pack(pady=5)
entry_cm.pack(pady=5)
button_converter.pack(pady=10)
label_resultado.pack(pady=5)

root.mainloop()