import os
from tkinter import Tk, Label, Button, messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL, Frame
import tkinter as tk
from PyPDF2 import PdfFileMerger
from PIL import ImageTk, Image, ImageSequence
import keyboard




class aplicacion(Tk):
    pdfs =[]
    
    i=1
    def __init__(self):
        
        super().__init__()  
       
    def inicializar_gui(self):
        
        self.title('Selector')
        self.geometry('180x400+1100+0')
        
        Button(self, text='Seleccione el archivo de pdf', command=self.seleccionar_archivo_pdf).grid(padx=5, pady=5)
        Button(self, text='Continuar', command=self.union).grid(padx=5, pady=5)
        Button(self, text='De 1 tiff a pdf', command=self.tiff).grid(padx=5, pady=5)
        Button(self, text='De png a pdf', command=self.seleccionar_archivo_png).grid(padx=5, pady=5)
        Button(self, text='Separador tiff', command=self.separador_tiff).grid(padx=5, pady=5)
        Button(self, text='Obtener portada .pdfs', command=self.portada).grid(padx=5, pady=5)
        
        
        id=tk.Entry(self, width=25)
        id.grid(padx=5, pady=5)
        aplicacion.num=0
        
        Button(self, text='PNG UN (1) PDF ', command=lambda:[self.unir_png_pdf(int(id.get()))]).grid(padx=5, pady=5) #TIFF
        Button(self, text='De varios png a varios pdf', command=lambda:[self.varios_png_varios_pdf(int(id.get()))]).grid(padx=5, pady=5) #TIFF
        Button(self, text='Dividir pdf', command=lambda:[self.clearFrame(self), self.dividir_pdf()]).grid(padx=5, pady=5)


    def seleccionar_archivo_pdf(self):
        archivo = filedialog.askopenfilename(title='Abrir archivo...', filetypes=[("Archivos PDF", "*.pdf")])
        aplicacion.pdfs.append(archivo)
        Label(self,text=os.path.basename(archivo)).grid(row=aplicacion.i, column=3)
        aplicacion.i+=1
        return

    def seleccionar_archivo_png(self):

        from PIL import Image

        archivos=[]
        archivo = filedialog.askopenfilename(multiple=True, filetypes=[("Archivos png", "*.png")])
        print(archivo)

        i=0        
        for file in archivo:
            img = Image.open(file)
            im_1 = img.convert('RGB')
            print(file)
            if i == 0:
                im=im_1
            else:
                archivos.append(im_1)
            i+=1
        
        self.salida = filedialog.asksaveasfilename(title='Guardar pdf unido...', defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
        im.save(self.salida, save_all=True, append_images=archivos)
        print("Finalizó")
        

    def tiff(self):
        archivos=[]
        archivo = filedialog.askopenfilename(title='Abrir archivo...')
        img = Image.open(archivo)
        for i, page in enumerate(ImageSequence.Iterator(img)):
            img1=page.convert('RGB')
            if i == 0:
                im=img1
            else:
                archivos.append(img1)
            #page.save("page%d.png" % i)

        self.salida = filedialog.asksaveasfilename(title='Guardar pdf unido...', defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
        im.save(self.salida, save_all=True, append_images=archivos)
        print("Finalizó")
        
        #img.close()
    
    
    def union (self):

        self.salida = filedialog.asksaveasfilename(title='Guardar pdf unido...', defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])
        if not self.salida.endswith('.pdf'):
            self.salida += '.pdf'
        self.salida=str(self.salida)
        fs = PdfFileMerger()

        for pdf in aplicacion.pdfs:
            fs.append(open(pdf, 'rb'))

        with open(self.salida, 'wb') as fout:
            fs.write(fout)
        print("Finalizó la unión")

    def separador_tiff(self):
        self.iconify()
        self.geometry('10x10')
        archivo = filedialog.askopenfilename(title='Abrir archivo...')
        img = Image.open(archivo)
        self.salida = filedialog.asksaveasfilename(title='Guardar png...', defaultextension='.png', filetypes=[('PDF', '*.png')])
        print(os.path.dirname(self.salida))
        for i, page in enumerate(ImageSequence.Iterator(img)):
            s=str(os.path.dirname(self.salida)+"\\"+"%d.png" % i)
            page.save(s)

        img.close()
        print("Finalizó los png")
        self.geometry('180x300+1100+0')
        self.deiconify()
        

    def unir_png_pdf(self, cont:int):
        cont+=aplicacion.num
        print(aplicacion.num, cont)
        self.iconify()
        self.geometry('10x10')
        cont=cont
        archivo = filedialog.askopenfilenames(multiple=True, filetypes=[("Archivos png", "*.png")])

        print("entró")
        archivos=[]
        print(archivo)
        i=0        
        for file in archivo:
            img = Image.open(file)
            im_1 = img.convert('RGB')
            if i == 0:
                im=im_1
            else:
                archivos.append(im_1)
            i+=1
        
        s=str(os.path.dirname(archivo[0])+"\\"+"%d.pdf" % cont)
        im.save(s, save_all=True, append_images=archivos)
        for file in archivo:
            os.remove(file)
        
        aplicacion.num+=1
        print(aplicacion.num, cont)
        print("Finalizó los png", cont)
        self.geometry('180x300+1100+0')
        self.deiconify()
    
    def varios_png_varios_pdf(self, cont:int):
        cont+=aplicacion.num
        print(aplicacion.num, cont)
        archivo = filedialog.askopenfilenames(multiple=True, filetypes=[("Archivos png", "*.png")])
        archivos=[]
        
        for file in archivo:
            img = Image.open(file)
            im_1 = img.convert('RGB')
            archivos.append(im_1)
            
        
        for a in archivos:
            s=str(os.path.dirname(archivo[0])+"\\"+"%d.pdf" % cont)
            a.save(s)
            cont+=1
            aplicacion.num+=1
        for file in archivo:
                os.remove(file)
        
        print(aplicacion.num, cont)
        print("Finalizó", cont)

    def archivos(self, dir, ext):
        i=0
        for root,dirs,files in os.walk(dir):
            for names in files:
                if names.endswith(ext):
                    i+=1
                    print(os.path.join(root, names))
        return i        
    
    def portada(self):
        import aspose.words as aw
        archivo = filedialog.askopenfilenames(filetypes=[("Archivos pdf", "*.pdf")])
        print(archivo)

        doc = aw.Document(archivo[0])

        extractedPage = doc.extract_pages(1, 1)
        extractedPage.save(f"Output_{1}.jpg")

    def dividir_pdf(self):
        inicio=tk.Entry(self, width=25)
        inicio.grid(padx=5, pady=5)
        fin=tk.Entry(self, width=25)
        fin.grid(padx=5, pady=5)
        Label(self, text="Nombre del archivo").grid(padx=5, pady=5)
        salida=tk.Entry(self, width=25)
        salida.grid(padx=5, pady=5)
       
        self.archivo = filedialog.askopenfilenames(filetypes=[("Archivos pdf", "*.pdf")])

        Button(self, text='Dividir', command=lambda:[self.split_pdf(int(inicio.get()), int(fin.get()), salida.get())]).grid(padx=5, pady=5)      
        Button(self, text="Atras", command=lambda:[self.clearFrame(self),self.inicializar_gui()]).grid()
    
    
    def split_pdf(self, page_num_inicio, page_num_fin, salida):
        import PyPDF2
        page_num_inicio-=1
        s=str(os.path.dirname(self.archivo[0])+"\\"+salida+".pdf")
        pdf_reader = PyPDF2.PdfFileReader(open(self.archivo[0], "rb"))
        pdf_writer = PyPDF2.PdfFileWriter()

        for page in range(page_num_inicio, page_num_fin):
            pdf_writer.addPage(pdf_reader.getPage(page))
        
        with open(s, 'wb') as file:
            pdf_writer.write(file)
        print("finalizó")

    def clearFrame(self, frame:Frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()

def main():
     app = aplicacion()
     app.inicializar_gui()
     
     app.mainloop()
   
    
    

if __name__ == '__main__':
    main()

