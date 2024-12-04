import tkinter as tk
from tkinter import messagebox

def suma():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        
        suma = num_1 + num_2
        messagebox.showinfo("Resultado",f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa numeros validos")

def resta():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        
        resta = num_1 - num_2
        messagebox.showinfo("Resultado",f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa numeros validos")

def multiplicar():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        
        mult = num_1 * num_2
        messagebox.showinfo("Resultado",f"La multplicacion es: {mult}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa numeros validos")

def dividir():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        
        div = num_1 / num_2
        messagebox.showinfo("Resultado",f"La division es: {div}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division entre cero")
    except ValueError:
        messagebox.showerror("Error", "Ingresa numeros validos")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x500")
ventana.configure(bg="#A1F4F4")

label_numero1 = tk.Label(ventana, text="Numero 1:", )
label_numero1.pack(pady=10)
entry_1 = tk.Entry(ventana)
entry_1.pack(pady=10)

label_numero2 = tk.Label(ventana, text="Numero 2")
label_numero2.pack(pady=10)
entry_2 = tk.Entry(ventana)
entry_2.pack(pady=10)

boton_suma = tk.Button(ventana,text="Suma", command=suma, bg="#76B7F7", fg="black", activebackground="light gray")
boton_suma.pack(pady=20)

boton_resta = tk.Button(ventana,text="Resta", command=resta, bg="light pink", fg="black", activebackground="light gray")
boton_resta.pack(pady=20)

boton_mult = tk.Button(ventana,text="Multiplicar", command=multiplicar, bg="#F77676", fg="black", activebackground="light gray")
boton_mult.pack(pady=20)

boton_div = tk.Button(ventana,text="Dividir", command=dividir, bg="yellow", fg="black", activebackground="light gray")
boton_div.pack(pady=20)

ventana.mainloop()

