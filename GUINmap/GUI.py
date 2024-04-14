import tkinter as tk

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

fields_frame = tk.LabelFrame(frame)
fields_frame.grid(row=0, column=0,pady=20)

# formulario scaneo
Target_label = tk.Label(fields_frame, text="Target: ", font=("Inter", 10), pady=10)
Target_entry = tk.Entry(fields_frame, width=60)
profile_label = tk.Label(fields_frame, text="Profile: ", font=("Inter", 10))
profile_entry = tk.Entry(fields_frame, width=60)
command_label = tk.Label(fields_frame, text="Command: ", font=("Inter", 10),pady=10)
command_entry = tk.Entry(fields_frame, width=60)

btn_frame = tk.LabelFrame(frame)
btn_frame.grid(row=0, column=1, pady=20, padx=10)

scan_btn = tk.Button(btn_frame, text="Scan", bg="#3A71F2", fg="#FFFFFF", font=("Inter", 10))
cancel_btn = tk.Button(btn_frame, text="Cancel", bg="#3A71F2", fg="#FFFFFF", font=("Inter", 10))

for widget in fields_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Placing (consider using grid or pack for better layout control)
Target_label.grid(row=1, column=0)
Target_entry.grid(row=1, column=1)
profile_label.grid(row=2, column=0)
profile_entry.grid(row=2, column=1)
command_label.grid(row=3, column=0)
command_entry.grid(row=3, column=1)
#Cambiar al la horientacion al lado de las columas
scan_btn.grid(row=1, column=0, pady=10, padx=5)
cancel_btn.grid(row=2, column=0, pady=10, padx=5)

area_frame = tk.LabelFrame(frame)
area_frame.grid(row=1, column=0, padx=20, pady=20)

# TextArea para mostrar los resultados
text_area = tk.Text(area_frame, height=30, width=90)
text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
                   
NmapGui.mainloop()
