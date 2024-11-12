from inventario import Inventario
from productos import Producto
import tkinter as tk
from tkinter import messagebox
from excepciones import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ProductoInvalidoException()
        if precio <= 0:
            raise PrecioInvalidoException()
        if cantidad < 0:
            raise CantidadInvalidaException()

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def mostrar_detalles(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}, Valor Total: ${self.calcular_valor_total():.2f}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def mostrar_productos(self):
        if not self.productos:
            return "No hay productos en el inventario."
        return "\n".join([producto.mostrar_detalles() for producto in self.productos])

class TiendaGUI:
    def __init__(self, inventario):
        self.inventario = inventario
        self.ventana = tk.Tk()
        self.ventana.title(""" Abarrotes "Don Gato" """)
        self.ventana.configure(bg="#4d6a8a")  # Fondo principal de la ventana
        self.ventana.geometry("350x400")

        tk.Label(self.ventana, text=""" Abarrotes "Don Gato" """, font=("Comic Sans MS", 16, "bold"), bg="#b3c1d6", fg="#333333").pack(pady=10)

        tk.Label(self.ventana, text="Nombre del Producto:", font=("Comic Sans MS", 10), bg="#b3c1d6", fg="#333333").pack()
        self.nombre_entry = tk.Entry(self.ventana, font=("Comic Sans MS", 10), width=25, bg="#ffffff")
        self.nombre_entry.pack(pady=5)

        tk.Label(self.ventana, text="Precio del Producto:", font=("Comic Sans MS", 10), bg="#b3c1d6", fg="#333333").pack()
        self.precio_entry = tk.Entry(self.ventana, font=("Comic Sans MS", 10), width=25, bg="#ffffff")
        self.precio_entry.pack(pady=5)

        tk.Label(self.ventana, text="Cantidad en Inventario:", font=("Comic Sans MS", 10), bg="#b3c1d6", fg="#333333").pack()
        self.cantidad_entry = tk.Entry(self.ventana, font=("Comic Sans MS", 10), width=25, bg="#ffffff")
        self.cantidad_entry.pack(pady=5)

        tk.Button(self.ventana, text="Agregar Producto", font=("Comic Sans MS", 10, "bold"), command=self.agregar_producto, bg="#7197a4", fg="white", activebackground="#597a88", width=20).pack(pady=10)

        tk.Button(self.ventana, text="Mostrar Inventario", font=("Comic Sans MS", 10, "bold"), command=self.mostrar_inventario, bg="#b57e87", fg="white", activebackground="#936366", width=20).pack(pady=10)


    def agregar_producto(self):
        try:
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())

            producto = Producto(nombre, precio, cantidad)
            self.inventario.agregar_producto(producto)
            messagebox.showinfo("Éxito", "Producto agregado exitosamente.")
            self.nombre_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)

        except ProductoInvalidoException as e:
            messagebox.showerror("Error", str(e))
        except PrecioInvalidoException as e:
            messagebox.showerror("Error", str(e))
        except CantidadInvalidaException as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para precio y cantidad.")

    def mostrar_inventario(self):
        inventario_info = self.inventario.mostrar_productos()
        valor_total = self.inventario.calcular_valor_inventario()
        messagebox.showinfo("Inventario", f"{inventario_info}\n\nValor Total del Inventario: ${valor_total:.2f}")

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    inventario = Inventario()
    app = TiendaGUI(inventario)
    app.ejecutar()