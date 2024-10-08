from tkinter import *
import customtkinter
import os

class AboutNmap:
    instance = None  # Atributo de clase para almacenar la instancia actual

    def __init__(self):
        if AboutNmap.instance is not None:  # Si ya hay una instancia, no hacer nada
            return

        AboutNmap.instance = self  # Asigna la instancia actual

        self.window = customtkinter.CTk()
        self.window.title("About Nmap")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "../../img/NmapIcon.ico")
        self.window.iconbitmap(icon_path)
        self.window.minsize(800, 600)

        window_width = 800
        window_height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        section1 = customtkinter.CTkFrame(master=self.window, fg_color="transparent")
        section1.pack(pady=5)
        label1 = customtkinter.CTkLabel(master=section1, text="¿Qué es Nmap?", font=("Helvetica", 18, "bold"))
        label1.pack(pady=5)
        que_es_text = (
            "Es una herramienta de codigo abierto que se utiliza para escanear"
            "direcciones IP y puertos en una red y para detectar aplicaciones instaladas"
            "permite encontrar los dispositivos que se enjecutan en la red,"
            "descubir puertos y servicios abiertos, como también"
            "la detección de vulnerabilidades."
        )

        label = customtkinter.CTkLabel(master=section1, text=que_es_text, wraplength=750, font=("Helvetica", 14), justify=LEFT)
        label.pack(pady=10, fill="x")

        section2 = customtkinter.CTkFrame(master=self.window, fg_color="transparent")
        section2.pack(pady=5)
        label2 = customtkinter.CTkLabel(master=section2, text="¿Para qué sirve?", font=("Helvetica", 18, "bold"))
        label2.pack(pady=5)
        para_que_sirve_text = (
            "Tiene la capacidad de reconocer los dispositivos, incluidos servidores,"
            "enrutadores, conmutadores, dispositivos móviles, etc, en redes únicas o multiples."
            "ayuda a identificar servicios que se ejecutan en un sistema que incluye servidores web, servidores DNS y"
            "otras aplicaciones comunes. Nmap también puede detectar versiones de aplicaciones con una precisión" 
            "razonable para ayudar a detectar vulnerabilidades existentes."
        )
        label2 = customtkinter.CTkLabel(master=section2, text=para_que_sirve_text, wraplength=750, font=("Helvetica", 14), justify=LEFT)
        label2.pack(pady=10, fill="x")

        section3 = customtkinter.CTkFrame(master=self.window, fg_color="transparent")
        section3.pack(pady=5)
        label3 = customtkinter.CTkLabel(master=section3, text="¿Cómo funciona Nmap?", font=("Helvetica", 18, "bold"))
        label3.pack(pady=5)

        # Bind para cerrar la ventana y restablecer la instancia
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.mainloop()

    def on_close(self):
        AboutNmap.instance = None  # Reinicia la instancia al cerrar la ventana
        self.window.destroy()

if __name__ == "__main__":
    AboutNmap()
