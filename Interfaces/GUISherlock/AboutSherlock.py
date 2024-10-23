from tkinter import *
import customtkinter
import os

class AboutSherlock:
    instance = None

    def __init__(self):
        if AboutSherlock.instance is not None:  # Si ya hay una instancia, no hacer nada
            return

        AboutSherlock.instance = self  # Asigna la instancia actual

        self.window = customtkinter.CTk()
        self.window.title("Sobre Sherlock")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "../../img/SherlockIcon.ico")
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
        label1 = customtkinter.CTkLabel(master=section1, text="¿Que es Sherlock?", font=("Helvetica", 18, "bold"))
        label1.pack(pady=5)
        que_es_text = (
        "Es una herramienta utilizada en la práctica "
        "de la seguridad informática, específicamente en " 
        "las pruebas de penetración (pentesting). " 
        "Se centra en la búsqueda de perfiles en redes "
        "sociales y otros servicios en línea. "
        )

        label = customtkinter.CTkLabel(master=section1, text=que_es_text, wraplength=750, font=("Helvetica", 14), justify=LEFT)
        label.pack(pady=10, fill="x")

        section2 = customtkinter.CTkFrame(master=self.window, fg_color="transparent")
        section2.pack(pady=5)
        label2 = customtkinter.CTkLabel(master=section1, text="¿Cual es su funcionalidad?", font=("Helvetica", 18, "bold"))
        label2.pack(pady=5)
        que_es_text = (
        "Sherlock puede buscar perfiles de usuario en una " 
        "amplia gama de redes sociales y servicios en " 
        "línea, incluyendo Facebook, Twitter, Instagram, " 
        "LinkedIn, entre otros.Permite a los pentesters " 
        "reunir información sobre un objetivo de manera " 
        "rápida y eficiente, lo que facilita el proceso " 
        "de reconocimiento. "
        )

        label2 = customtkinter.CTkLabel(master=section1, text=que_es_text, wraplength=750, font=("Helvetica", 14), justify=LEFT)
        label2.pack(pady=10, fill="x")

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

    def on_close(self):
            AboutSherlock.instance = None  # Reinicia la instancia al cerrar la ventana
            self.window.destroy()

if __name__ == "__main__":
    AboutSherlock()