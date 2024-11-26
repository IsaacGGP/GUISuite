from tkinter import *
import customtkinter
import os
from Interfaces.GUINmap.NmapGUI import NmapGUI
from Interfaces.GUINmap.AboutNmap import AboutNmap
from Interfaces.GUISherlock.Sherlock import SherlockGUI
from Interfaces.GUISherlock.AboutSherlock import AboutSherlock
from PIL import Image
from customtkinter import CTkImage

def open_NmapGUI():
    app.withdraw()
    NmapGUI(app)

def open_SherlockGUI():
    app.withdraw()  # Oculta la ventana de la suite
    SherlockGUI(app)

# Configuración del tema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Inicializar la aplicación
app = customtkinter.CTk()
app.title("CyberXplore")
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.abspath(os.path.join(script_dir, "./img/SuiteIcon.ico"))
app.iconbitmap(icon_path)
app.minsize(750, 480)

window_width = 750
window_height = 480
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


# Frame para el logo de la suite
logo_frame = customtkinter.CTkFrame(master=app, fg_color="transparent")
logo_frame.pack(pady=20)

title_label = customtkinter.CTkLabel(logo_frame, text="Bienvenido a CyberXplore ", font=("Helvetica", 18, "bold"), fg_color="transparent")
title_label.pack(pady=(0, 10))

# Cargar y mostrar la imagen del logo de la suite
suite_logo_path = os.path.join(script_dir, "./img/SuiteIcon.png")
suite_img = Image.open(suite_logo_path)
logo_suite = customtkinter.CTkImage(light_image=suite_img, size=(100, 100))

suite_logo_label = customtkinter.CTkLabel(logo_frame, image=logo_suite, text="")
suite_logo_label.pack()

# Frame para las herramientas (Nmap y Sherlock)
herramientas_frame = customtkinter.CTkFrame(master=app, fg_color="transparent")
herramientas_frame.pack(pady=20)

# Cargar y redimensionar las imágenes de Nmap y Sherlock
nmap_logo_path = os.path.join(script_dir, "./img/NmapIcon.png")
nmap_img = Image.open(nmap_logo_path).resize((100, 100), Image.LANCZOS)
nmap_img_ctk = customtkinter.CTkImage(light_image=nmap_img, size=(100, 100))

sherlock_logo_path = os.path.join(script_dir, "./img/SherlockIcon.png")
sherlock_img = Image.open(sherlock_logo_path).resize((100, 100), Image.LANCZOS)
sherlock_img_ctk = customtkinter.CTkImage(light_image=sherlock_img, size=(100, 100))

# Cargar la imagen del icono de ayuda
questimg_path = os.path.abspath(os.path.join(script_dir, "./img/ayuda.png"))  
question_img = Image.open(questimg_path).resize((70, 70), Image.LANCZOS)
question_img_ctk = CTkImage(question_img, size=(30, 30))

# Agregar los logos y botones de Nmap y Sherlock
nmap_logo_label = customtkinter.CTkLabel(herramientas_frame, image=nmap_img_ctk, text="")
nmap_logo_label.grid(row=0, column=0, pady=10)

nmap_button = customtkinter.CTkButton(herramientas_frame, 
    text="Nmap",
    font=("Helvetica", 14), 
    border_width=0, 
    corner_radius=6,
    command=open_NmapGUI
)
nmap_button.grid(row=1, column=0, padx=70, pady=15)

questionNMap_label = customtkinter.CTkLabel(herramientas_frame, image=question_img_ctk, text="", fg_color="transparent", cursor="hand2")
questionNMap_label.grid(row=2, column=0, padx=70, pady=2)
questionNMap_label.bind("<Button-1>", lambda e: AboutNmap())

sherlock_logo_label = customtkinter.CTkLabel(herramientas_frame, image=sherlock_img_ctk, text="")
sherlock_logo_label.grid(row=0, column=1, pady=10)

sherlock_button = customtkinter.CTkButton(herramientas_frame, 
    text="Sherlock",
    font=("Helvetica", 14),  
    border_width=0, 
    corner_radius=6,
    command=open_SherlockGUI
)
sherlock_button.grid(row=1, column=1, padx=70)

questionSherlock_label = customtkinter.CTkLabel(herramientas_frame, image=question_img_ctk, text="", fg_color="transparent", cursor="hand2")
questionSherlock_label.grid(row=2, column=1, padx=70, pady=15)
questionSherlock_label.bind("<Button-1>", lambda e: AboutSherlock())

app.mainloop()