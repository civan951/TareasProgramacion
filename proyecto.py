import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *

def login():
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
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
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


def registrar_empleado():
    
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
            micursos.execute(f"UPDATE usuarios set nombre='{nombreAdd}', apellido='{apellidoAdd}', usuario='{usuarioAdd}', contraseña='{contraAdd}', rol='{rolAdd} where id={idAdd}")
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
        

    root = tk.Tk()
    root.geometry("1200x500")
    
    label1 = tk.Label(root,text="Registro de usuarios", fg="red",font=("Arial",28)).place(x=500,y=0)
    
    global identificador
    global name
    global apellido
    global usuario
    global password
    global rol
    
    labelid = tk.Label(root, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12))
    labelnombre.place(x=100, y=80)
    
    labelapellido = tk.Label(root, text="Apellido", font=("Arial", 12))
    labelapellido.place(x=100, y=110)
    
    labelusuario = tk.Label(root, text="Usuario", font=("Arial", 12))
    labelusuario.place(x=100, y=140)
    
    labelcontraseña = tk.Label(root, text="Contraseña", font=("Arial", 12))
    labelcontraseña.place(x=100, y=170)
    
    labelrol = tk.Label(root, text="Rol", font=("Arial", 12))
    labelrol.place(x=100, y=200)
    
    identificador = tk.Entry(root)
    identificador.place(x=270, y=50)
    
    name = tk.Entry(root)
    name.place(x=270, y=80)
    
    apellido = tk.Entry(root)
    apellido.place(x=270, y=110)
    
    usuario = tk.Entry(root)
    usuario.place(x=270, y=140)
    
    password = tk.Entry(root)
    password.place(x=270, y=170)
    
    rol = tk.Entry(root)
    rol.place(x=270, y=200)
    
    tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    
    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(root,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    
    
    root.mainloop()
  
  
    
def registrar_libro():
    
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
            micursos.execute(f"insert into usuarios(id,titulo,autor,editorial,año,precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editorialAdd}','{añoAdd}','{precioAdd}')")
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
        año.insert(0,seleccion["Año de Publicacion"])
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
            micursos.execute(f"UPDATE libros set titulo='{tituloAdd}', autor='{autorAdd}', editorial='{editorialAdd}', año='{añoAdd}', precio='{precioAdd} where id={idAdd}")
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
        

    root = tk.Tk()
    root.geometry("1200x500")
    
    label1 = tk.Label(root,text="Registro de Libros", fg="red",font=("Arial",28)).place(x=500,y=0)
    
    global identificador
    global titulo
    global autor
    global editorial
    global año
    global precio
    
    labelid = tk.Label(root, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labeltitulo = tk.Label(root, text="Titulo", font=("Arial", 12))
    labeltitulo.place(x=100, y=80)
    
    labelautor = tk.Label(root, text="Autor", font=("Arial", 12))
    labelautor.place(x=100, y=110)
    
    labeleditorial = tk.Label(root, text="Editorial", font=("Arial", 12))
    labeleditorial.place(x=100, y=140)
    
    labelaño = tk.Label(root, text="Año de Publicacion", font=("Arial", 12))
    labelaño.place(x=100, y=170)
    
    labelprecio = tk.Label(root, text="Precio", font=("Arial", 12))
    labelprecio.place(x=100, y=200)
    
    identificador = tk.Entry(root)
    identificador.place(x=270, y=50)
    
    titulo = tk.Entry(root)
    titulo.place(x=270, y=80)
    
    autor = tk.Entry(root)
    autor.place(x=270, y=110)
    
    editorial = tk.Entry(root)
    editorial.place(x=270, y=140)
    
    año = tk.Entry(root)
    año.place(x=270, y=170)
    
    precio = tk.Entry(root)
    precio.place(x=270, y=200)
    
    tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    
    columnas = ("Id","Titulo","Autor","Editorial","Año de Publicacion","Precio")
    listbox = ttk.Treeview(root,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>",obtenerR)
    
    
    root.mainloop()

#! Para realizar los cambios de pantalla entre admin y empleado es con un if al momento de realizar el login

# def pantalla_admin():
#     def abrir_segunda_ventana():
#         ventana_principal.withdraw()
        
#         ventana_sec = tk.Toplevel(ventana_principal)
#         ventana_sec.title("Segunda Ventana")
        
#         def regresar_a_principal():
#             ventana_sec.destroy()  
#             ventana_principal.deiconify()  

#         boton_regresar = tk.Button(ventana_sec, text="Regresar a la ventana principal", command=regresar_a_principal)
#         boton_regresar.pack(pady=20)

#     ventana_principal = tk.Tk()
#     ventana_principal.title("Ventana Principal")

#     boton_abrir_segunda_ventana = tk.Button(ventana_principal, text="Abrir segunda ventana", command=abrir_segunda_ventana)
#     boton_abrir_segunda_ventana.pack(pady=20)

#     ventana_principal.mainloop()
