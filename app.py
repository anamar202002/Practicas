from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL


class aplicacion(Tk):
    def __init__(self):
        
        super().__init__()  
        

    def inicializar_gui(self):
        
        self.title('Programa') #Título de la ventana
        self.state("zoomed")
        f_menu=Frame(self,bg="pink")
        f_menu.grid(row=0, column=0, columnspan=2)
        f_tabla=Frame(self, bg="blue")
        f_tabla.grid(row=1,column=0,  padx=10, pady=10, ipady=60, ipadx=60)
        f_scrolly=Frame(self, bg="red")
        f_scrolly.grid(row=1, column=1, rowspan=2)
        f_scrollx=Frame(self, bg="red")
        f_scrollx.grid(row=2, column=0)
        #self.geometry('350x350') #tamaño de la ventada
        
        #botones iniciales para la carga de los documentos
        

 
  

def main():
     app = aplicacion()
     app.inicializar_gui()     
     app.mainloop()
   
    
    

if __name__ == '__main__':
    main()