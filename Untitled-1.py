import tkinter as tk
from tkinter import messagebox
import math

def suma_numeros():
    numeros = entry_suma.get().split()
    suma = sum(map(int, numeros))
    messagebox.showinfo("Resultado", f"La suma es: {suma}")

def producto_numeros():
    numeros = entry_producto.get().split()
    producto = math.prod(map(int, numeros))
    messagebox.showinfo("Resultado", f"El producto es: {producto}")

def division_numeros():
    try:
        num1 = float(entry_division1.get())
        num2 = float(entry_division2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"La división es: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")

def calcular_factorial():
    num = int(entry_factorial.get())
    resultado = math.factorial(num)
    messagebox.showinfo("Resultado", f"El factorial de {num} es: {resultado}")

def imprimir_tabla():
    num = int(entry_tabla.get())
    tabla = "\n".join([f"{num} x {i} = {num * i}" for i in range(1, 11)])
    messagebox.showinfo("Tabla de multiplicar", tabla)

def calcular_cuadrado_cubo():
    num = float(entry_cuadrado_cubo.get())
    cuadrado = num ** 2
    cubo = num ** 3
    messagebox.showinfo("Resultado", f"Cuadrado: {cuadrado}, Cubo: {cubo}")

def calcular_promedio():
    numeros = []
    while True:
        num = float(entry_promedio.get())
        if num == -1:
            break
        numeros.append(num)
    promedio = sum(numeros) / len(numeros) if numeros else 0
    messagebox.showinfo("Resultado", f"El promedio es: {promedio}")

def max_min_numeros():
    numeros = list(map(int, entry_maxmin.get().split()))
    maximo = max(numeros)
    minimo = min(numeros)
    total = len(numeros)
    messagebox.showinfo("Resultado", f"Máximo: {maximo}, Mínimo: {minimo}, Total: {total}")

# --- Configuración de la ventana principal ---

ventana = tk.Tk()
ventana.title("CalculaThor")
ventana.configure(bg="#393e3c")

try:
    ventana.iconbitmap("C:/Users/Samuel Cervantes/Documents/P01/images.ico")
except tk.TclError:
    print("Error: No se encontró el archivo del icono o formato incorrecto.")

# Estilo de los widgets
estilo_label = {"font": ("Arial", 12), "bg": "#393e3c", "fg": "#ffffff"}
estilo_entry = {"font": ("Arial", 12), "bg": "#393e3c", "fg": "#ffffff", "borderwidth": 1, "relief": "solid"}
estilo_boton = {"font": ("Arial", 12), "bg": "#e0e0e0", "borderwidth": 1, "relief": "raised"}

# Suma de n números
label_suma = tk.Label(ventana, text="Ingrese números para sumar (separados por espacio):", **estilo_label)
label_suma.grid(row=0, column=0, padx=5, pady=5)
entry_suma = tk.Entry(ventana, **estilo_entry)
entry_suma.grid(row=0, column=1, padx=5, pady=5)
boton_suma = tk.Button(ventana, text="Calcular Suma", command=suma_numeros, **estilo_boton)
boton_suma.grid(row=1, column=0, columnspan=2, pady=10)

# Producto entre n números
label_producto = tk.Label(ventana, text="Ingrese números para multiplicar (separados por espacio):", **estilo_label)
label_producto.grid(row=2, column=0, padx=5, pady=5)
entry_producto = tk.Entry(ventana, **estilo_entry)
entry_producto.grid(row=2, column=1, padx=5, pady=5)
boton_producto = tk.Button(ventana, text="Calcular Producto", command=producto_numeros, **estilo_boton)
boton_producto.grid(row=3, column=0, columnspan=2, pady=10)

# División entre 2 números
label_division1 = tk.Label(ventana, text="Ingrese el primer número para dividir:", **estilo_label)
label_division1.grid(row=4, column=0, padx=5, pady=5)
entry_division1 = tk.Entry(ventana, **estilo_entry)
entry_division1.grid(row=4, column=1, padx=5, pady=5)
label_division2 = tk.Label(ventana, text="Ingrese el segundo número para dividir:", **estilo_label)
label_division2.grid(row=5, column=0, padx=5, pady=5)
entry_division2 = tk.Entry(ventana, **estilo_entry)
entry_division2.grid(row=5, column=1, padx=5, pady=5)
boton_division = tk.Button(ventana, text="Calcular División", command=division_numeros, **estilo_boton)
boton_division.grid(row=6, column=0, columnspan=2, pady=10)

# Factorial de un número
label_factorial = tk.Label(ventana, text="Ingrese un número para calcular el factorial:", **estilo_label)
label_factorial.grid(row=7, column=0, padx=5, pady=5)
entry_factorial = tk.Entry(ventana, **estilo_entry)
entry_factorial.grid(row=7, column=1, padx=5, pady=5)
boton_factorial = tk.Button(ventana, text="Calcular Factorial", command=calcular_factorial, **estilo_boton)
boton_factorial.grid(row=8, column=0, columnspan=2, pady=10)

# Tabla de multiplicar
label_tabla = tk.Label(ventana, text="Ingrese un número para imprimir su tabla de multiplicar:", **estilo_label)
label_tabla.grid(row=9, column=0, padx=5, pady=5)
entry_tabla = tk.Entry(ventana, **estilo_entry)
entry_tabla.grid(row=9, column=1, padx=5, pady=5)
boton_tabla = tk.Button(ventana, text="Imprimir Tabla", command=imprimir_tabla, **estilo_boton)
boton_tabla.grid(row=10, column=0, columnspan=2, pady=10)

# Cuadrado y cubo de un número
label_cuadrado_cubo = tk.Label(ventana, text="Ingrese un número para calcular su cuadrado y cubo:", **estilo_label)
label_cuadrado_cubo.grid(row=11, column=0, padx=5, pady=5)
entry_cuadrado_cubo = tk.Entry(ventana, **estilo_entry)
entry_cuadrado_cubo.grid(row=11, column=1, padx=5, pady=5)
boton_cuadrado_cubo = tk.Button(ventana, text="Calcular Cuadrado y Cubo", command=calcular_cuadrado_cubo, **estilo_boton)
boton_cuadrado_cubo.grid(row=12, column=0, columnspan=2, pady=10)

# Promedio de una serie de números
label_promedio = tk.Label(ventana, text="Ingrese números para calcular el promedio (-1 para terminar):", **estilo_label)
label_promedio.grid(row=13, column=0, padx=5, pady=5)
entry_promedio = tk.Entry(ventana, **estilo_entry)
entry_promedio.grid(row=13, column=1, padx=5, pady=5)
boton_promedio = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio, **estilo_boton)
boton_promedio.grid(row=14, column=0, columnspan=2, pady=10)

# Máximo y mínimo de una serie de números
label_maxmin = tk.Label(ventana, text="Ingrese números para encontrar el máximo y mínimo (separados por espacio):", **estilo_label)
label_maxmin.grid(row=15, column=0, padx=5, pady=5)
entry_maxmin = tk.Entry(ventana, **estilo_entry)
entry_maxmin.grid(row=15, column=1, padx=5, pady=5)
boton_maxmin = tk.Button(ventana, text="Calcular Máximo y Mínimo", command=max_min_numeros, **estilo_boton)
boton_maxmin.grid(row=16, column=0, columnspan=2, pady=10)

def limpiar_campos():
    entry_suma.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_division1.delete(0, tk.END)
    entry_division2.delete(0, tk.END)
    entry_factorial.delete(0, tk.END)
    entry_tabla.delete(0, tk.END)
    entry_cuadrado_cubo.delete(0, tk.END)
    entry_promedio.delete(0, tk.END)
    entry_maxmin.delete(0, tk.END)

# Botón para limpiar campos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos, **estilo_boton)
boton_limpiar.grid(row=17, column=0, columnspan=2, pady=10)

ventana.mainloop()