import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y
import DECOdificador  # Importar el módulo logica

# Función para mostrar el resultado en el cuadro de texto principal
def mostrar_resultado(resultado):
    entrada_texto.config(state=tk.NORMAL)
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, f"{resultado}")
    entrada_texto.config(state=tk.DISABLED)

# Función para limpiar el cuadro de texto
def limpiar_campo():
    entrada_texto.config(state=tk.NORMAL)
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.config(state=tk.NORMAL)

# Función para codificar
def codificar_mensaje():
    mensaje = entrada_texto.get("1.0", tk.END).strip()
    resultado = DECOdificador.codificar(mensaje)
    mostrar_resultado(resultado)

# Función para decodificar
def decodificar_mensaje():
    mensaje = entrada_texto.get("1.0", tk.END).strip()
    resultado = DECOdificador.decodificar(mensaje)
    mostrar_resultado(resultado)

# Función personalizada para pegar texto
def pegar_texto(event=None):
    entrada_texto.event_generate("<<Paste>>")
    return "break"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("DE-CO-dificador de Mensajes")
ventana.geometry("600x400")

# Crear widgets
label = tk.Label(ventana, text="Ingresa el mensaje:")
label.pack(pady=10)

# Crear frame para entrada de texto y barra de desplazamiento
frame_texto = tk.Frame(ventana)
frame_texto.pack(pady=10)

scrollbar = Scrollbar(frame_texto)
scrollbar.pack(side=RIGHT, fill=Y)

entrada_texto = tk.Text(frame_texto, height=10, width=70, yscrollcommand=scrollbar.set)
entrada_texto.pack(pady=10)
scrollbar.config(command=entrada_texto.yview)

# Habilitar funciones de borrar, cortar, copiar y pegar
entrada_texto.bind("<Control-Key-a>", lambda e: entrada_texto.tag_add("sel", "1.0", "end"))
entrada_texto.bind("<Control-Key-x>", lambda e: entrada_texto.event_generate("<<Cut>>"))
entrada_texto.bind("<Control-Key-c>", lambda e: entrada_texto.event_generate("<<Copy>>"))
entrada_texto.bind("<Control-Key-v>", pegar_texto)

boton_codificar = tk.Button(ventana, text="Codificar", command=codificar_mensaje)
boton_codificar.pack(side=tk.LEFT, padx=20)

boton_decodificar = tk.Button(ventana, text="Decodificar", command=decodificar_mensaje)
boton_decodificar.pack(side=tk.LEFT, padx=20)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campo)
boton_limpiar.pack(side=tk.LEFT, padx=20)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(side=tk.RIGHT, padx=20)

# Iniciar el bucle de la aplicación
ventana.mainloop()
