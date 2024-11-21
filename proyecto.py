import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def login():
    
    global root
    
    def verificar_usuario():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
    
        try:
            conn = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='',  
                database='proyecto'    
                )
    
            cursor = conn.cursor()
    
            cursor.execute('''
                SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
            ''', (usuario, contraseña))
    
            usuario = cursor.fetchone()
            
            
    
            if usuario:
                messagebox.showinfo("Login exitoso", f"Bienvenido(a) {usuario[1]}")
                if usuario[5] == "Administrador":
                    messagebox.showinfo("Informacion", "Ingreso como Administrador")
                    root.withdraw()
                    pantalla_admin()
                    
                elif usuario[5] == "Empleado":
                    messagebox.showinfo("Informacion", "Ingreso como Empleado")
                    root.withdraw()
                    pantalla_empleado() 
            else:
                messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
    
        except mysql.connector.Error as err:
            messagebox.showerror("Error de conexión", f"Error: {err}")
    
        finally:
            if conn.is_connected():
                conn.close()  
    
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")
    
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(root, width=30)
    entry_usuario.pack(pady=5)
    
    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(root, width=30, show="*")
    entry_contraseña.pack(pady=5)
    
    btn_login = tk.Button(root, text="Login", command=verificar_usuario)
    btn_login.pack(pady=20)
    
    root.mainloop()


def registrar_empleado(ventana_actual):
    ventana_actual.destroy()
    
    def mostrar():
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        micursos.execute("select * from usuarios")
        lista = micursos.fetchall()
        
        for i,(id,nombre,apellido,usuario,contraseña,rol) in enumerate(lista, start=1):
            listbox.insert("","end", values=(id,nombre,apellido,usuario,contraseña,rol))
            mysqlC.close()
            
    def add():
        idAdd = identificador.get()
        nombreAdd = name.get()
        apellidoAdd = apellido.get()
        usuarioAdd = usuario.get()
        contraAdd = password.get()
        rolAdd = rol.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"insert into usuarios(id,nombre,apellido,usuario,contraseña,rol) values('{idAdd}','{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraAdd}','{rolAdd}')")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            messagebox.showinfo("Informacion", "Usuario agregado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
            
    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()
        
    def obtenerR(event):
        identificador.delete(0,END)
        name.delete(0,END)
        apellido.delete(0,END)
        usuario.delete(0,END)
        password.delete(0,END)
        rol.delete(0,END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["Id"])
        name.insert(0,seleccion["Nombre"])
        apellido.insert(0,seleccion["Apellido"])
        usuario.insert(0,seleccion["Usuario"])
        password.insert(0,seleccion["Contraseña"])
        rol.insert(0,seleccion["Rol"])
        
    def delete():
        
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"DELETE FROM USUARIOS WHERE id={idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            messagebox.showinfo("Informacion", "Usuario eliminado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
            
    def edit():
        idAdd = identificador.get()
        nombreAdd = name.get()
        apellidoAdd = apellido.get()
        usuarioAdd = usuario.get()
        contraAdd = password.get()
        rolAdd = rol.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"UPDATE usuarios set nombre='{nombreAdd}', apellido='{apellidoAdd}', usuario='{usuarioAdd}', contraseña='{contraAdd}', rol='{rolAdd}' where id={idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            name.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            password.delete(0,END)
            rol.delete(0,END)
            messagebox.showinfo("Informacion", "Usuario editado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
        

    empleado = tk.Toplevel()
    empleado.geometry("1200x500")
    
    label1 = tk.Label(empleado,text="Registro de usuarios", fg="red",font=("Arial",28)).place(x=500,y=0)
    
    
    labelid = tk.Label(empleado, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labelnombre = tk.Label(empleado, text="Nombre", font=("Arial", 12))
    labelnombre.place(x=100, y=80)
    
    labelapellido = tk.Label(empleado, text="Apellido", font=("Arial", 12))
    labelapellido.place(x=100, y=110)
    
    labelusuario = tk.Label(empleado, text="Usuario", font=("Arial", 12))
    labelusuario.place(x=100, y=140)
    
    labelcontraseña = tk.Label(empleado, text="Contraseña", font=("Arial", 12))
    labelcontraseña.place(x=100, y=170)
    
    labelrol = tk.Label(empleado, text="Rol", font=("Arial", 12))
    labelrol.place(x=100, y=200)
    
    identificador = tk.Entry(empleado)
    identificador.place(x=270, y=50)
    
    name = tk.Entry(empleado)
    name.place(x=270, y=80)
    
    apellido = tk.Entry(empleado)
    apellido.place(x=270, y=110)
    
    usuario = tk.Entry(empleado)
    usuario.place(x=270, y=140)
    
    password = tk.Entry(empleado)
    password.place(x=270, y=170)
    
    rol = tk.Entry(empleado)
    rol.place(x=270, y=200)
    
    tk.Button(empleado,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(empleado,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(empleado,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    tk.Button(empleado,text="Regresar",command=lambda: regresar_login(empleado), height=5, width=10, font=("Arial", 12)).place(x=550,y=230)
    
    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(empleado,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    
  
    
def registrar_libro(ventana_actual):
    ventana_actual.destroy()
    
    def mostrar():
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        micursos.execute("select * from libros")
        lista = micursos.fetchall()
        
        for i,(id,titulo,autor,editorial,año,precio) in enumerate(lista, start=1):
            listbox.insert("","end", values=(id,titulo,autor,editorial,año,precio))
            mysqlC.close()
            
    def add():
        idAdd = identificador.get()
        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        añoAdd = año.get()
        precioAdd = precio.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"insert into libros(id,titulo,autor,editorial,año,precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editorialAdd}','{añoAdd}','{precioAdd}')")
            mysqlC.commit()
            identificador.delete(0,END)
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("Informacion", "Libro agregado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
            
    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()
        
    def obtenerR(event):
        identificador.delete(0,END)
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año.delete(0,END)
        precio.delete(0,END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["Id"])
        titulo.insert(0,seleccion["Titulo"])
        autor.insert(0,seleccion["Autor"])
        editorial.insert(0,seleccion["Editorial"])
        año.insert(0,seleccion["Año"])
        precio.insert(0,seleccion["Precio"])
        
    def delete():
        
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"DELETE FROM LIBROS WHERE id={idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("Informacion", "Libro eliminado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
            
    def edit():
        idAdd = identificador.get()
        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        añoAdd = año.get()
        precioAdd = precio.get()
        mysqlC = mysql.connector.connect(host= "localhost", user="root", password="", database="proyecto")
        micursos=mysqlC.cursor()
        
        try:
            micursos.execute(f"UPDATE libros set titulo='{tituloAdd}', autor='{autorAdd}', editorial='{editorialAdd}', año='{añoAdd}', precio='{precioAdd}' where id={idAdd}")
            mysqlC.commit()
            identificador.delete(0,END)
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("Informacion", "Libro editado")
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()
        

    book = tk.Toplevel()
    book.geometry("1200x500")
    
    label1 = tk.Label(book,text="Registro de Libros", fg="red",font=("Arial",28)).place(x=500,y=0)
     
    labelid = tk.Label(book, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labeltitulo = tk.Label(book, text="Titulo", font=("Arial", 12))
    labeltitulo.place(x=100, y=80)
    
    labelautor = tk.Label(book, text="Autor", font=("Arial", 12))
    labelautor.place(x=100, y=110)
    
    labeleditorial = tk.Label(book, text="Editorial", font=("Arial", 12))
    labeleditorial.place(x=100, y=140)
    
    labelaño = tk.Label(book, text="Año de Publicacion", font=("Arial", 12))
    labelaño.place(x=100, y=170)
    
    labelprecio = tk.Label(book, text="Precio", font=("Arial", 12))
    labelprecio.place(x=100, y=200)
    
    identificador = tk.Entry(book)
    identificador.place(x=270, y=50)
    
    titulo = tk.Entry(book)
    titulo.place(x=270, y=80)
    
    autor = tk.Entry(book)
    autor.place(x=270, y=110)
    
    editorial = tk.Entry(book)
    editorial.place(x=270, y=140)
    
    año = tk.Entry(book)
    año.place(x=270, y=170)
    
    precio = tk.Entry(book)
    precio.place(x=270, y=200)
    
    tk.Button(book,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(book,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(book,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    tk.Button(book,text="Regresar",command=lambda: regresar_login(book), height=5, width=10, font=("Arial",12)).place(x=550,y=230)
    
    columnas = ("Id","Titulo","Autor","Editorial","Año de Publicacion","Precio")
    listbox = ttk.Treeview(book,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    
def pantalla_admin():
    ventana_admin = tk.Toplevel()
    ventana_admin.title("Administrador")
    ventana_admin.geometry("400x300")
    
    tk.Label(ventana_admin, text="Ventana Administrador", font=("Arial, 16")).pack(pady=20)
    tk.Button(ventana_admin, text="Registrar Empleado", command=lambda: registrar_empleado(ventana_admin)).pack(pady=10)
    tk.Button(ventana_admin, text="Regresar al Login",command=lambda: regresar_login(ventana_admin)).pack(pady=10)

def pantalla_empleado():
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title("Empleado")
    ventana_empleado.geometry("400x300")
    
    tk.Label(ventana_empleado, text="Pantalla de Empleado", font=("Arial", 16)).pack(pady=20)
    tk.Button(ventana_empleado, text="Registrar Libro", command=lambda: registrar_libro(ventana_empleado)).pack(pady=10)
    tk.Button(ventana_empleado, text="Regresar al Login", command=lambda: regresar_login(ventana_empleado)).pack(pady=10)

def regresar_login(ventana_actual):
    ventana_actual.destroy()
    root.deiconify()

login()

#! FALTA EL FILTRO