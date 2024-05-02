import tkinter as tk
from tkinter import messagebox
import subprocess

# Función para obtener el comando según el perfil seleccionado
def get_command(profile, target):
    if profile == "Escaneo básico":
        return f"nmap {target}"
    elif profile == "Escaneo rápido":
        return f"nmap -T4 -F {target}"
    elif profile == "Escaneo profundo":
        return f"nmap -T4 -A {target}"
    elif profile == "Escaneo de vulnerabilidades":
        return f"nmap --script vuln {target}"
    elif profile == "Escaneo de red":
        return f"nmap -sn {target}"
    elif profile == "Escaneo personalizado":
        # Deja el campo de comando para que el usuario lo complete
        return ""

# Función para actualizar el campo de comando
def update_command(*args):
    target = Target_entry.get()
    profile = profile_var.get()
    command = get_command(profile, target)
    command_entry.delete(0, tk.END)
    command_entry.insert(0, command)

# Crear la ventana principal
NmapGui = tk.Tk()
NmapGui.title("Nmap")

frame = tk.Frame(NmapGui)
frame.pack()

# Menu
menu = tk.Menu()

# Opciones principales
menu_scan = tk.Menu(menu, tearoff=0)
menu_tools = tk.Menu(menu, tearoff=0)
menu_help = tk.Menu(menu, tearoff=0)

# Opciones principales del menu
menu.add_cascade(label="Scan", menu=menu_scan)
menu.add_cascade(label="Tools", menu=menu_tools)
menu.add_cascade(label="Help", menu=menu_help)

# Mostrar menu
NmapGui.config(menu=menu)

# Frame para los campos
fields_frame = tk.LabelFrame(frame, text="Escaneo")
fields_frame.grid(row=0, column=0, pady=20)

# Label y entrada para el target
Target_label = tk.Label(fields_frame, text="Target: ", font=("Inter", 10), pady=10)
Target_entry = tk.Entry(fields_frame, width=60)

# Lista desplegable para perfiles de exploración
profile_label = tk.Label(fields_frame, text="Profile: ", font=("Inter", 10))
profiles = ["Escaneo básico", "Escaneo rápido", "Escaneo profundo", "Escaneo de vulnerabilidades", "Escaneo de red", "Escaneo personalizado"]
profile_var = tk.StringVar(value=profiles[0])

# Conectar el trace para actualizar el comando cuando cambia el perfil
profile_var.trace("w", update_command)

profile_menu = tk.OptionMenu(fields_frame, profile_var, *profiles)

# Label y entrada para el comando
command_label = tk.Label(fields_frame, text="Command: ", font=("Inter", 10), pady=10)
command_entry = tk.Entry(fields_frame, width=60)

# Ubicación de los elementos
Target_label.grid(row=1, column=0)
Target_entry.grid(row=1, column=1)
profile_label.grid(row=2, column=0)
profile_menu.grid(row=2, column=1)
command_label.grid(row=3, column=0)
command_entry.grid(row=3, column=1)

# Botón para iniciar el escaneo
btn_frame = tk.LabelFrame(frame, text="Acciones")
btn_frame.grid(row=0, column=1, pady=20, padx=10)

# Botón de escaneo
def execute_scan():
    target = Target_entry.get()
    profile = profile_var.get()

    if not target:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un objetivo.")
        return
    
    command = command_entry.get()  # Obtén el comando actual

    # Ejecutar el comando y mostrar el resultado
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        text_area.delete(1.0, tk.END)  # Limpiar el área de texto antes de mostrar nuevos resultados
        text_area.insert(tk.END, result)  # Mostrar el resultado del escaneo
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar Nmap: {e}")

scan_btn = tk.Button(btn_frame, text="Scan", bg="#3A71F2", fg="#FFFFFF", font=("Inter", 10), command=execute_scan)
scan_btn.grid(row=1, column=0, pady=10, padx=5)

# Área para mostrar resultados
area_frame = tk.LabelFrame(frame, text="Resultados")
area_frame.grid(row=1, column=0, padx=20, pady=20)

# TextArea para mostrar los resultados
text_area = tk.Text(area_frame, height=30, width=90)
text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz gráfica
NmapGui.mainloop()
