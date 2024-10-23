from fpdf import FPDF
from tkinter import messagebox, filedialog

#Clase de generar PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resultados del escaneo de Nmap', ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0,'C')
    
    def add_result(self, result_text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, result_text)

def guardar_pdf(resultados):
    if not resultados.strip():
        messagebox.showwarning("Advertencia", "No hay resultados para guardar en el PDF.")
        return
    
    #Creación de ventana emergente de guardado del archivo
    archivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    #crear PDF
    if archivo:
        pdf = PDF()
        pdf.add_page()
        pdf.add_result(resultados)

        #Guardar PDF
        pdf.output(archivo)
        messagebox.showinfo("Información", f"El PDF se ha guardado en: {archivo}")