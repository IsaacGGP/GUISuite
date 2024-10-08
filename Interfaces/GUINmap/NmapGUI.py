from tkinter import *
from tkinter import messagebox
import customtkinter
import subprocess
import os
from .GeneratePDF import guardar_pdf

class NmapGUI:

    def __init__(self, parent):
        self.parent = parent
        # Inicializar una lista para almacenar el historial de resultados
        self.scan_history = []
        self.setup_ui()

    def setup_ui(self):
        #Color de tema
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.app = customtkinter.CTk()
        self.app.title("Nmap")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "../../img/NmapIcon.ico")
        self.app.iconbitmap(icon_path)
        self.app.minsize(900, 600)

        window_width = 900
        window_height = 600
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        #Frame principal
        main_frame = customtkinter.CTkFrame(master=self.app, fg_color="transparent")
        main_frame.pack(padx=20, pady=20)

        # Frame para los campos de entrada
        input_frame = customtkinter.CTkFrame(master=main_frame, fg_color="transparent")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        # Sub-Frame para "Target"
        target_frame = customtkinter.CTkFrame(master=input_frame, fg_color="transparent")
        target_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        Target_label = customtkinter.CTkLabel(target_frame, text="Objetivo:", font=("helvetica", 14))
        Target_label.grid(row=0, column=0, sticky="e", pady=5, padx=5)
        self.target_var = StringVar()
        self.target_entry = customtkinter.CTkEntry(target_frame, width=300, textvariable=self.target_var)
        self.target_entry.grid(row=0, column=1, pady=5, padx=5)
        self.target_entry.bind("<KeyRelease>", self.update_command)

        # Sub-Frame para "Perfil"
        profile_frame = customtkinter.CTkFrame(master=input_frame, fg_color="transparent")
        profile_frame.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        profile_label = customtkinter.CTkLabel(profile_frame, text="Perfil:", font=("helvetica", 14))
        profile_label.grid(row=0, column=2, sticky="e", pady=10, padx=5)

        profiles = ["Escaneo básico", "Escaneo rápido", "Escaneo profundo", "Escaneo de vulnerabilidades", "Escaneo de ping", "Detección de firewall e IPS", "Escaneo UDP", "Escaneo personalizado"]
        self.profile_var = customtkinter.StringVar(value=profiles[0])

        # Crear el menú desplegable para perfiles
        profile_menu = customtkinter.CTkOptionMenu(profile_frame, variable=self.profile_var, values=profiles, command=self.update_command ,width=300)
        profile_menu.grid(row=0, column=3, padx=5, pady=5)

        # Sub-Frame para Command
        command_frame = customtkinter.CTkFrame(input_frame, fg_color="transparent")
        command_frame.grid(row=2, column=0, columnspan=2, pady=5)

        command_label = customtkinter.CTkLabel(command_frame, text="Comando:", font=("helvetica", 14))
        command_label.grid(row=1, column=0, sticky="e", pady=10)
        self.command_entry = customtkinter.CTkEntry(command_frame, width=450)
        self.command_entry.grid(row=1, column=1, columnspan=3, pady=5, padx=5)

        # Frame para los botones
        button_frame = customtkinter.CTkFrame(master=main_frame, fg_color="transparent")
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        #Botones
        Scan = customtkinter.CTkButton(button_frame, 
            text="Escanear",
            font=("Helvetica", 12),
            corner_radius=6,
            command=self.execute_scan)
        Scan.grid(row=2, column=1, pady=5, padx=15)

        Cancel = customtkinter.CTkButton(button_frame, 
            text="Cancelar",
            font=("Helvetica", 12),
            corner_radius=6,
            command=self.cancel_scan)
        Cancel.grid(row=2, column=2, pady=5, padx=15)
    
        PrintPDF = customtkinter.CTkButton(button_frame, 
            text="Generar PDF",
            font=("Helvetica", 12),
            corner_radius=6,
            command=self.generate_pdf)
        PrintPDF.grid(row=2, column=3, pady=5, padx=15)

        # Frame para los resultados
        result_frame = customtkinter.CTkFrame(master=main_frame, fg_color="transparent")
        result_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Botones para cambiar entre "Output" e "Historial"
        options_frame = customtkinter.CTkFrame(master=result_frame, fg_color="transparent")
        options_frame.grid(row=0, column=0, pady=5, sticky="w")

        output_button = customtkinter.CTkButton(options_frame, 
            text="Salida",
            font=("Helvetica", 12), 
            border_width=0, 
            corner_radius=6, 
            fg_color="transparent",
            command=self.show_output)
        output_button.grid(row=0, column=0, padx=5)

        history_button = customtkinter.CTkButton(options_frame, 
        text="Historial",
        font=("Helvetica", 12),  
        border_width=0, 
        corner_radius=6, 
        fg_color="transparent",
        command=self.show_history)
        history_button.grid(row=0, column=1, padx=5)

        self.result_text = customtkinter.CTkTextbox(result_frame, width=700, height=350)
        self.result_text.grid(row=1, column=0, padx=15, pady=8, sticky='nsew')

        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(1, weight=1)

        self.update_command()
        
        self.app.protocol("WM_DELETE_WINDOW", self.on_close)

        self.app.mainloop()

    def on_close(self):
        self.app.destroy()
        self.parent.deiconify()

    # Función para obtener el comando según el perfil seleccionado
    def get_command(self,profile, target):
        commands = {
            "Escaneo básico": f"nmap {target}",
            "Escaneo rápido": f"nmap -T4 -F {target}",
            "Escaneo profundo": f"nmap -T4 -A {target}",
            "Escaneo de vulnerabilidades": f"nmap --script vuln {target}",
            "Escaneo de ping": f"nmap -sn {target}",
            "Detección de firewall e IPS": f"nmap -sA {target}",
            "Escaneo UDP": f"nmap -sU {target}",
            "Escaneo personalizado": ""  # Deja el campo de comando para que el usuario lo complete
        }
        return commands.get(profile, "")
    
    def generate_pdf(self):
            guardar_pdf(self.result_text.get("1.0", customtkinter.END))

    # Función para actualizar el campo de comando
    def update_command(self, event=None):
        target = self.target_entry.get()
        profile = self.profile_var.get()
        command = self.get_command(profile, target)
        self.command_entry.delete(0, customtkinter.END)
        self.command_entry.insert(0, command)

    # Función para actualizar el TextBox
    def update_textbox(self, text):
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, customtkinter.END)
        self.result_text.insert(customtkinter.END, text)
        self.result_text.configure(state="disabled")

    # Función para ejecutar el escaneo
    def execute_scan(self):
        target = self.target_entry.get()
        profile = self.profile_var.get()

        if not target:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un objetivo.")
            return
        
        command = self.command_entry.get()  # Obtén el comando actual

        # Ejecutar el comando y mostrar el resultado
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            self.update_textbox(result)  # Mostrar el resultado del escaneo
            # Añadir el resultado al historial
            self.scan_history.append(result)
        except subprocess.CalledProcessError as e:
            error_message = f"Error al ejecutar Nmap: {e}"
            self.update_textbox(error_message)
            messagebox.showerror("Error", error_message)
    
    def cancel_scan(self):
        if self.scan_process:
            self.scan_process.terminate()
            self.scan_process = None
            self.update_textbox("Escaneo cancelado.")
    
    def show_output(self):
        # Mostrar el resultado del escaneo actual
        if self.scan_history:
            self.update_textbox(self.scan_history[-1])  # Mostrar el último resultado del historial

    def show_history(self):
        # Mostrar todo el historial
        history_text = "\n".join(self.scan_history) if self.scan_history else "No hay historial disponible."
        self.update_textbox(history_text)

    # Función para actualizar los colores de los botones según el tema
    def update_button_colors(self):
        theme = customtkinter.get_appearance_mode()
        if theme == "dark":
            text_color = "white"
            hover_color = "#333"
        else:
            text_color = "black"
            hover_color = "#f0f0f0"
        
        for button in [self.output_button, self.history_button]:
            button.configure(text_color=text_color, hover_color=hover_color)

if __name__ == "__main__":
      NmapGUI()