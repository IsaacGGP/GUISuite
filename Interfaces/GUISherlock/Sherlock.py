import subprocess
from tkinter import *
import customtkinter
import ctypes
import threading
import os
import psutil  # Importar psutil para gestionar los procesos
from fpdf import FPDF
import tkinter.messagebox as messagebox  # Importar messagebox para mostrar advertencias


class SherlockGUI:

    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        # Crear la ventana
        self.raiz = customtkinter.CTk()
        self.raiz.title("SherlockGUI")
        self.raiz.config(bg="black")
        self.raiz.resizable(0, 0)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "../../img/SherlockIcon.ico")
        self.raiz.iconbitmap(icon_path)

        # Configuración del tema
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Variable global para almacenar el nombre de usuario y el hilo de búsqueda
        self.nombre_usuario = ""
        self.hilo_busqueda = None
        self.proceso_sherlock = None

        # Primer frame y cuadro de texto
        frame1 = customtkinter.CTkFrame(self.raiz, fg_color="gray20", border_width=3, border_color="blue", corner_radius=10)
        frame1.pack(fill="x", padx=100, pady=(30, 10))
        label1 = customtkinter.CTkLabel(frame1, text="Identificador de Usuario", text_color="white", anchor="center")
        label1.pack(pady=(10, 0))

        # Cuadro de texto para ingresar el usuario
        self.cuadro_texto = customtkinter.CTkEntry(frame1, width=300, placeholder_text="Introduce el usuario")
        self.cuadro_texto.pack(pady=10)

        # Asociar el evento para validar el nombre de usuario (capturar la tecla presionada)
        self.cuadro_texto.bind("<Key>", self.validar_usuario)

        # Segundo frame para el resultado y cuadro de texto
        frame2 = customtkinter.CTkFrame(self.raiz, fg_color="gray20", border_width=3, border_color="blue", corner_radius=10)
        frame2.pack(fill="both", expand=True, padx=30, pady=(10, 30))
        label2 = customtkinter.CTkLabel(frame2, text="Resultado de la búsqueda", text_color="white")
        label2.pack(pady=(10, 0))
        self.cuadro_texto2 = customtkinter.CTkTextbox(frame2, width=500, height=200, state="normal")
        self.cuadro_texto2.pack(pady=10, padx=10, fill="both", expand=True)

        # Crear los botones
        frame_boton = customtkinter.CTkFrame(self.raiz, fg_color="black")
        frame_boton.pack(fill="x", padx=30, pady=(10, 30))

        # Botones con el mismo diseño original
        Scan = customtkinter.CTkButton(frame_boton, text="Buscar", font=("Helvetica", 12), command=self.buscar_cuentas, corner_radius=6)
        Scan.pack(anchor="center", padx=10)
        Cancelar = customtkinter.CTkButton(frame_boton, text="Cancelar", font=("Helvetica", 12), command=self.cancelar_busqueda, corner_radius=6)
        Cancelar.pack(anchor="center", padx=10, pady=(10, 0))
        Button = customtkinter.CTkButton(frame_boton, text="Generar PDF", font=("Helvetica", 12), command=self.generar_pdf, corner_radius=6)
        Button.pack(side="left", padx=10)
        Button2 = customtkinter.CTkButton(frame_boton, text="Limpiar", font=("Helvetica", 12), command=self.clear_entry, corner_radius=6)
        Button2.pack(side="right", anchor="e", padx=10)

        # Ruta al archivo sherlock.py (se busca en todo el sistema)
        self.ruta_a_sherlock = self.encontrar_ruta_sherlock()
        if self.ruta_a_sherlock is None:
            messagebox.showerror("Error", "No se encontró el archivo sherlock.py. Asegúrate de que esté en tu sistema.")
            self.raiz.quit()

        # Tamaño de la ventana
        width = 800
        height = 700

        # Centrar la ventana
        self.center_window(self.raiz, width, height)
        self.raiz.protocol("WM_DELETE_WINDOW", self.on_close) # Manejar el evento de cierre
        self.raiz.mainloop()
        
    def on_close(self):
        self.raiz.destroy()  # Cerramos la ventana de Sherlock
        self.parent.deiconify()  # Restauramos la ventana principal

    # Función para obtener las dimensiones de la pantalla
    def get_screen_resolution(self):
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    # Función para centrar la ventana en la pantalla
    def center_window(self, root, width, height):
        screen_width, screen_height = self.get_screen_resolution()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    # Función para buscar cuentas utilizando Sherlock como un subproceso
    def buscar_cuentas(self):
        self.nombre_usuario = self.cuadro_texto.get().strip()  # Eliminar espacios al principio y al final
        if not self.nombre_usuario:  # Verificar si el nombre de usuario está vacío
            messagebox.showwarning("Advertencia", "Por favor, introduce un nombre de usuario.")
            return

        # Mensaje inicial de búsqueda
        resultado = "Buscando cuentas, esto puede tardar, por favor espera..."
        self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
        self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
        self.cuadro_texto2.insert("end", resultado)
        self.cuadro_texto2.configure(state="disabled")  # Desactivar la edición

        def ejecutar_sherlock():
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            resultado_archivo = os.path.join(desktop_path, f"{self.nombre_usuario}.txt")
            comando = f"python {self.ruta_a_sherlock} {self.nombre_usuario} --output {resultado_archivo}"
            proceso_sherlock = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = proceso_sherlock.communicate()
            if stderr:
                resultado = "Error al ejecutar Sherlock:\n" + stderr.decode("utf-8")
            else:
                resultado = stdout.decode("utf-8")

            # Actualizar el cuadro de texto con el resultado
            self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
            self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
            self.cuadro_texto2.insert("end", resultado)  # Insertar el resultado
            self.cuadro_texto2.configure(state="disabled")  # Volver a desactivar la edición

        # Crear y guardar el hilo de búsqueda
        self.hilo_busqueda = threading.Thread(target=ejecutar_sherlock)
        self.hilo_busqueda.start()

    # Función para cancelar el proceso de búsqueda
    def cancelar_busqueda(self):
        if self.proceso_sherlock and self.proceso_sherlock.poll() is None:  # Si el proceso está corriendo
            proceso_psutil = psutil.Process(self.proceso_sherlock.pid)
            for proc in proceso_psutil.children(recursive=True):  # Terminar los procesos hijos
                proc.terminate()
            proceso_psutil.terminate()  # Terminar el proceso principal

            # Limpiar el cuadro de texto de salida
            self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
            self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa

            # Mostrar el mensaje de cancelación
            self.cuadro_texto2.insert("1.0", f"Has cancelado la búsqueda del usuario '{self.nombre_usuario}'.")
            self.cuadro_texto2.configure(state="disabled")  # Volver a desactivar la edición

    # Función para generar un PDF con el contenido del cuadro de texto
    def generar_pdf(self):
        if self.nombre_usuario:
            contenido = self.cuadro_texto2.get("1.0", "end-1c")  # Obtener el contenido del cuadro de texto
            if contenido.strip():  # Verificar si el contenido no está vacío
                try:
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.multi_cell(0, 10, contenido)
                    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                    archivo_pdf = os.path.join(desktop_path, f"{self.nombre_usuario}.pdf")
                    pdf.output(archivo_pdf)

                    # Actualizar la interfaz para mostrar el mensaje de éxito
                    resultado = f"PDF generado y guardado en el escritorio con el nombre {self.nombre_usuario}.pdf"
                    self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
                    self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
                    self.cuadro_texto2.insert("end", resultado)  # Insertar el mensaje
                    self.cuadro_texto2.configure(state="disabled")  # Desactivar la edición
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo generar el PDF: {str(e)}")
            else:
                self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
                self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
                self.cuadro_texto2.insert("end", "No hay datos para guardar en el PDF.")
                self.cuadro_texto2.configure(state="disabled")  # Desactivar la edición
        else:
            self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto
            self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
            self.cuadro_texto2.insert("end", "No se ha realizado una búsqueda, por favor realiza una búsqueda primero.")
            self.cuadro_texto2.configure(state="disabled")  # Desactivar la edición

    # Función para limpiar los cuadros de texto
    def clear_entry(self):
        self.cuadro_texto.delete(0, "end")  # Limpiar el cuadro de texto del usuario
        self.cuadro_texto2.configure(state="normal")  # Habilitar edición en el cuadro de texto de resultados
        self.cuadro_texto2.delete("1.0", "end")  # Limpiar cualquier salida previa
        self.cuadro_texto2.configure(state="disabled")  # Volver a desactivar la edición

    # Función que se llama cuando se presiona una tecla en el cuadro de texto
    def validar_usuario(self, event):
        if event.keysym == "space":  # Si se presiona la barra espaciadora
            # Mostrar una ventana emergente advirtiendo que no se pueden introducir espacios
            messagebox.showwarning("Advertencia", "El nombre de usuario no puede contener espacios.")
            return "break"  # Evita que el espacio se inserte en el cuadro de texto

    # Función para buscar la ruta de la carpeta Sherlock
    def encontrar_ruta_sherlock(self):
        for root, dirs, files in os.walk(os.path.expanduser("~")):
            if "sherlock.py" in files:
                return os.path.join(root, "sherlock.py")
        return None

# Para ejecutar la interfaz en modo normal
if __name__ == "__main__":
   SherlockGUI()