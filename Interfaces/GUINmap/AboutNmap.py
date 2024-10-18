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

         # Crear un CTkScrollableFrame para contenido desplazable
        scroll_frame = customtkinter.CTkScrollableFrame(master=self.window, width=780, height=580, fg_color="transparent")
        scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

        section1 = customtkinter.CTkFrame(master=scroll_frame, fg_color="transparent")
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

        section2 = customtkinter.CTkFrame(master=scroll_frame, fg_color="transparent")
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

        section3 = customtkinter.CTkFrame(master=scroll_frame, fg_color="transparent")
        section3.pack(pady=5)
        label3 = customtkinter.CTkLabel(master=section3, text="Comandos", font=("Helvetica", 18, "bold"))
        label3.pack(pady=5)
        comandos_text = (
            "Escaneo de ping: Escanea la lista de dispositivos en funcionamiento "
            "en un una subred determinada.\n\n"
            "> nmap -sp 192.168.1.1/24 \n\n"
            "Escanear un solo host: Escanea un solo host en busca de 1000 puertos conocidos "
            "estos puertos son los que utilizan servicios como SQL, SNTP, apache, entre otros.\n\n"
            "> nmap ' host ' \n\n"
            "Escaneo sigiloso: Se realiza enviando un paquete SYN y analizando las respuestas "
            "si se recibe SYN/ACK, significa que el puerto está abierto y puedes abrir una conexión TCP.\n\n"
            "> nmap -sS ' host ' \n\n"
            "Escaneo de versiones: Es una parte importante en las pruebas de penetración, ya que se puede encontrar "
            "una vulnerabilidad existente en la base de datos de Vulnerabilidades y Exploits Comunes (CVE). \n\n"
            "> nmap -sV ' host ' \n\n"
            "Escaneo de sistemas operativos: Proporciona información sobre el sistema operativo subyacente mediante "
            "huellas dactilares de TCP/IP. Nmap también intenta encontrar el tiempo de actividad del sistema "
            "durante una exploración del sistema operativo. \n\n"
            "> nmap -O ' host ' \n\n"
            "Escaneo de puertos \n\n"
            "El escaneo de puertos es una de las caracteristicas más fundamentales de Nmap. Puedes buscar puertos de "
            "varias maneras. \n\n"
            "• Usar el parámetro -p para buscar un solo puerto. \n\n"
            "> nmap -p 80 ' IP ' \n\n"
             "• Si se especifica el tipo de puertos, se puede buscar información sobre un tipo particular de conexión "
             "por ejemplo, una conexión TCP. \n\n"
             "> nmap -p  T:7777, 80 ' IP ' \n\n"
             "• Se puede escanear un rango de puertos separándolos con un guion. \n\n"
             "> nmap -p 76–973 ' IP ' \n\n"
             "• También se puede usar el indicador ' -top-ports ' para especificar los n puertos principales para escanear. \n\n"
             ">  nmap --top-ports 10 ' host ' \n\n"
            "Escaneo de puertos \n\n"
            "Si se desea escanear una gran lista de direcciones IP, puedes hacerlo importando un archivo con la lista "
            "de direcciones IP. \n\n"
            "> nmap -iL /input_ips.txt \n\n"
            "El comando anterior produce los resultados del escaneo de todos los dominios dados en el archivo ' input_ips.txt '. Además de "
            "simplemente escanear las direcciones IP, también puedes usar opciones y banderas adicionales. "

        )
        label3 = customtkinter.CTkLabel(master=section3, text=comandos_text, wraplength=750, font=("Helvetica", 14), justify=LEFT)
        label3.pack(pady=10, fill="x")

        # Bind para cerrar la ventana y restablecer la instancia
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.mainloop()

    def on_close(self):
        AboutNmap.instance = None  # Reinicia la instancia al cerrar la ventana
        self.window.destroy()

if __name__ == "__main__":
    AboutNmap()
