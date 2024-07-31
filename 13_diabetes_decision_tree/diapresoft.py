import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
    
##################################################################
##################################################################

class VentanaM1(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Configurar la segunda ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Cargar la imagen de fondo2
        self.imagen_fondo1 = tk.PhotoImage(file="1.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo1
        self.label_fondo1 = tk.Label(self, image=self.imagen_fondo1)
        self.label_fondo1.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Variable para almacenar el estado de la opción seleccionada
        self.H3_21 = tk.IntVar()
        self.C64_21 = tk.IntVar()
        self.C49_8_21 = tk.IntVar()
        self.C68D_21 = tk.IntVar()

        # Checkbox Sí/No H3_21
        self.checkbox_siH3_21 = tk.Checkbutton(self, text="Sí", variable=self.H3_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siH3_21.place(relx=0.45, rely=0.39, anchor=tk.CENTER)

        self.checkbox_noH3_21 = tk.Checkbutton(self, text="No", variable=self.H3_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noH3_21.place(relx=0.55, rely=0.39, anchor=tk.CENTER)

        # Checkbox Sí/No C64_21
        self.checkbox_siC64_21 = tk.Checkbutton(self, text="Sí", variable=self.C64_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC64_21.place(relx=0.45, rely=0.495, anchor=tk.CENTER)

        self.checkbox_noC64_21 = tk.Checkbutton(self, text="No", variable=self.C64_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC64_21.place(relx=0.55, rely=0.495, anchor=tk.CENTER)

        # Checkbox Sí/No C49_8_21
        self.checkbox_siC49_8_21 = tk.Checkbutton(self, text="Sí", variable=self.C49_8_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC49_8_21.place(relx=0.45, rely=0.59, anchor=tk.CENTER)

        self.checkbox_noC49_8_21 = tk.Checkbutton(self, text="No", variable=self.C49_8_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC49_8_21.place(relx=0.55, rely=0.59, anchor=tk.CENTER)

        # Checkbox Sí/No C68D_21
        self.checkbox_siC68D_21 = tk.Checkbutton(self, text="Sí", variable=self.C68D_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC68D_21.place(relx=0.45, rely=0.685, anchor=tk.CENTER)

        self.checkbox_noC68D_21 = tk.Checkbutton(self, text="No", variable=self.C68D_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC68D_21.place(relx=0.55, rely=0.685, anchor=tk.CENTER)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="", font=('Helvetica', 18), bg='#59c2d5')
        self.resultado_label.place(relx=0.5, rely=0.825, anchor=tk.CENTER)

        # Botón para enviar
        self.boton_enviar = tk.Button(self, text="Diagnosticar", command=self.enviar_valor,
                                       width=20, height=2, font=('Helvetica', 14, "bold"),
                                       bg='#32CD32', fg='black')
        self.boton_enviar.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # Botón para regresar a menu
        self.boton_menu = tk.Button(self, text="← Menú", command=self.regresar_menu, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_menu.place(relx=0.2, rely=.9, anchor=tk.CENTER)

    @staticmethod
    def decision_tree_model_1(C68D_21, C49_8_21, C64_21, H3_21):
        if C68D_21 <= 1.50:
            if C64_21 <= 1.50:
                if C49_8_21 <= 1.50:
                    return 2
                else:
                    return 2
            else:
                if H3_21 <= 1.50:
                    if C49_8_21 <= 1.50:
                        return 1
                    else:
                        return 1
                else:
                    return 1
        else:
            if H3_21 <= 1.50:
                if C49_8_21 <= 1.50:
                    if C64_21 <= 1.50:
                        return 2
                    else:
                        return 2
                else:
                    if C64_21 <= 1.50:
                        return 2
                    else:
                        return 2
            else:
                if C49_8_21 <= 1.50:
                    if C64_21 <= 1.50:
                        return 2
                    else:
                        return 2
                else:
                    if C64_21 <= 1.50:
                        return 2
                    else:
                        return 2

    def enviar_valor(self):
        # Obtener el valor seleccionado
        H3_21 = self.H3_21.get()
        C64_21 = self.C64_21.get()
        C49_8_21 = self.C49_8_21.get()
        C68D_21 = self.C68D_21.get()

        # Llamar a la función de decisión y obtener el resultado
        resultado = self.decision_tree_model_1(C68D_21, C49_8_21, C64_21, H3_21)
        if resultado == 1:
            resultadom1 = "Positivo"
        else:
            resultadom1 = "Negativo"

        # Actualizar el texto en el widget de etiqueta con el resultado
        self.resultado_label.config(text="{}".format(resultadom1), font=('Helvetica', 18), bg='#FF5757')
        
    def regresar_menu(self):
        self.destroy()  # Cerrar la ventana secundaria

##################################################################
##################################################################
    
class VentanaM2(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Configurar la segunda ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Cargar la imagen de fondo2
        self.imagen_fondo2 = tk.PhotoImage(file="2.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo2
        self.label_fondo2 = tk.Label(self, image=self.imagen_fondo2)
        self.label_fondo2.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Variable para almacenar el estado de la opción seleccionada
        self.H9_21 = tk.IntVar()
        self.C64_21 = tk.IntVar()
        self.C49_8_21 = tk.IntVar()
        self.C68D_21 = tk.IntVar()

        # Checkbox Sí/No H9_21
        self.checkbox_siH9_21 = tk.Checkbutton(self, text="Sí", variable=self.H9_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siH9_21.place(relx=0.45, rely=0.42, anchor=tk.CENTER)

        self.checkbox_noH9_21 = tk.Checkbutton(self, text="No", variable=self.H9_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noH9_21.place(relx=0.55, rely=0.42, anchor=tk.CENTER)

        # Checkbox Sí/No C64_21
        self.checkbox_siC64_21 = tk.Checkbutton(self, text="Sí", variable=self.C64_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC64_21.place(relx=0.45, rely=0.515, anchor=tk.CENTER)

        self.checkbox_noC64_21 = tk.Checkbutton(self, text="No", variable=self.C64_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC64_21.place(relx=0.55, rely=0.515, anchor=tk.CENTER)

        # Checkbox Sí/No C49_8_21
        self.checkbox_siC49_8_21 = tk.Checkbutton(self, text="Sí", variable=self.C49_8_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC49_8_21.place(relx=0.45, rely=0.61, anchor=tk.CENTER)

        self.checkbox_noC49_8_21 = tk.Checkbutton(self, text="No", variable=self.C49_8_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC49_8_21.place(relx=0.55, rely=0.61, anchor=tk.CENTER)

        # Checkbox Sí/No C68D_21
        self.checkbox_siC68D_21 = tk.Checkbutton(self, text="Sí", variable=self.C68D_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC68D_21.place(relx=0.45, rely=0.71, anchor=tk.CENTER)

        self.checkbox_noC68D_21 = tk.Checkbutton(self, text="No", variable=self.C68D_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC68D_21.place(relx=0.55, rely=0.71, anchor=tk.CENTER)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="", font=('Helvetica', 18), bg='#59c2d5')
        self.resultado_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        # Botón para enviar
        self.boton_enviar = tk.Button(self, text="Diagnosticar", command=self.enviar_valor,
                                       width=20, height=2, font=('Helvetica', 14, "bold"),
                                       bg='#32CD32', fg='black')
        self.boton_enviar.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # Botón para regresar a menu
        self.boton_menu = tk.Button(self, text="← Menú", command=self.regresar_menu, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_menu.place(relx=0.2, rely=.9, anchor=tk.CENTER)

    @staticmethod
    def decision_tree_model_2(C68D_21, C49_8_21, C64_21, H9_21):
        if C68D_21 <= 1.50:
            if C64_21 <= 1.50:
                if H9_21 <= 1.50:
                    return 1
                else:
                    if C49_8_21 <= 1.50:
                        return 2
                    else:
                        return 2
            else:
                if H9_21 <= 1.50:
                    return 1
                else:
                    if C49_8_21 <= 1.50:
                        return 1
                    else:
                        return 1
        else:
            if C64_21 <= 1.50:
                if C49_8_21 <= 1.50:
                    if H9_21 <= 1.50:
                        return 2
                    else:
                        return 2
                else:
                    if H9_21 <= 1.50:
                        return 2
                    else:
                        return 2
            else:
                if H9_21 <= 1.50:
                    if C49_8_21 <= 1.50:
                        return 2
                    else:
                        return 2
                else:
                    if C49_8_21 <= 1.50:
                        return 2
                    else:
                        return 2
                
    def enviar_valor(self):
        # Obtener el valor seleccionado
        H9_21 = self.H9_21.get()
        C64_21 = self.C64_21.get()
        C49_8_21 = self.C49_8_21.get()
        C68D_21 = self.C68D_21.get()

        # Llamar a la función de decisión y obtener el resultado
        resultado = self.decision_tree_model_2(C68D_21, C49_8_21, C64_21, H9_21)
        if resultado == 1:
            resultadom1 = "Positivo"
        else:
            resultadom1 = "Negativo"

        # Actualizar el texto en el widget de etiqueta con el resultado
        self.resultado_label.config(text="{}".format(resultadom1), font=('Helvetica', 18), bg='#FF5757')
        
    def regresar_menu(self):
        self.destroy()  # Cerrar la ventana secundaria

##################################################################
##################################################################

class VentanaM3(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Configurar la segunda ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Cargar la imagen de fondo2
        self.imagen_fondo3 = tk.PhotoImage(file="3.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo3
        self.label_fondo3 = tk.Label(self, image=self.imagen_fondo3)
        self.label_fondo3.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Variable para almacenar el estado de la opción seleccionada
        self.C64_21 = tk.IntVar()
        self.C49_8_21 = tk.IntVar()
        self.C68D_21 = tk.IntVar()

        # Checkbox Sí/No C64_21
        self.checkbox_siC64_21 = tk.Checkbutton(self, text="Sí", variable=self.C64_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC64_21.place(relx=0.45, rely=0.445, anchor=tk.CENTER)

        self.checkbox_noC64_21 = tk.Checkbutton(self, text="No", variable=self.C64_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC64_21.place(relx=0.55, rely=0.445, anchor=tk.CENTER)

        # Checkbox Sí/No C49_8_21
        self.checkbox_siC49_8_21 = tk.Checkbutton(self, text="Sí", variable=self.C49_8_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC49_8_21.place(relx=0.45, rely=0.54, anchor=tk.CENTER)

        self.checkbox_noC49_8_21 = tk.Checkbutton(self, text="No", variable=self.C49_8_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC49_8_21.place(relx=0.55, rely=0.54, anchor=tk.CENTER)

        # Checkbox Sí/No C68D_21
        self.checkbox_siC68D_21 = tk.Checkbutton(self, text="Sí", variable=self.C68D_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC68D_21.place(relx=0.45, rely=0.64, anchor=tk.CENTER)

        self.checkbox_noC68D_21 = tk.Checkbutton(self, text="No", variable=self.C68D_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC68D_21.place(relx=0.55, rely=0.64, anchor=tk.CENTER)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="", font=('Helvetica', 18), bg='#59c2d5')
        self.resultado_label.place(relx=0.5, rely=0.78, anchor=tk.CENTER)

        # Botón para enviar
        self.boton_enviar = tk.Button(self, text="Diagnosticar", command=self.enviar_valor,
                                       width=20, height=2, font=('Helvetica', 14, "bold"),
                                       bg='#32CD32', fg='black')
        self.boton_enviar.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # Botón para regresar a menu
        self.boton_menu = tk.Button(self, text="← Menú", command=self.regresar_menu, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_menu.place(relx=0.2, rely=.9, anchor=tk.CENTER)

    @staticmethod
    def decision_tree_model_3(C68D_21, C49_8_21, C64_21):
        if C68D_21 <= 1.50:
            if C64_21 <= 1.50:
                if C49_8_21 <= 1.50:
                    return 2
                else:
                    return 2
            else:
                if C49_8_21 <= 1.50:
                    return 1
                else:
                    return 1
        else:
            if C64_21 <= 1.50:
                if C49_8_21 <= 1.50:
                    return 2
                else:
                    return 2
            else:
                if C49_8_21 <= 1.50:
                    return 2
                else:
                    return 2
                
    def enviar_valor(self):
        # Obtener el valor seleccionado
        C64_21 = self.C64_21.get()
        C49_8_21 = self.C49_8_21.get()
        C68D_21 = self.C68D_21.get()

        # Llamar a la función de decisión y obtener el resultado
        resultado = self.decision_tree_model_3(C68D_21, C49_8_21, C64_21)
        if resultado == 1:
            resultadom1 = "Positivo"
        else:
            resultadom1 = "Negativo"

        # Actualizar el texto en el widget de etiqueta con el resultado
        self.resultado_label.config(text="{}".format(resultadom1), font=('Helvetica', 18), bg='#FF5757')
        
    def regresar_menu(self):
        self.destroy()  # Cerrar la ventana secundaria

##################################################################
##################################################################

class VentanaM4(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Configurar la segunda ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Cargar la imagen de fondo4
        self.imagen_fondo4 = tk.PhotoImage(file="4.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo4
        self.label_fondo4 = tk.Label(self, image=self.imagen_fondo4)
        self.label_fondo4.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Variable para almacenar el estado de la opción seleccionada
        self.C64_21 = tk.IntVar()
        self.C49_8_21 = tk.IntVar()
        self.C68D_21 = tk.IntVar()

        # Checkbox Sí/No C64_21
        self.checkbox_siC64_21 = tk.Checkbutton(self, text="Sí", variable=self.C64_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC64_21.place(relx=0.45, rely=0.49, anchor=tk.CENTER)

        self.checkbox_noC64_21 = tk.Checkbutton(self, text="No", variable=self.C64_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC64_21.place(relx=0.55, rely=0.49, anchor=tk.CENTER)

        # Checkbox Sí/No C49_8_21
        self.checkbox_siC49_8_21 = tk.Checkbutton(self, text="Sí", variable=self.C49_8_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC49_8_21.place(relx=0.45, rely=0.59, anchor=tk.CENTER)

        self.checkbox_noC49_8_21 = tk.Checkbutton(self, text="No", variable=self.C49_8_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC49_8_21.place(relx=0.55, rely=0.59, anchor=tk.CENTER)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="", font=('Helvetica', 18), bg='#59c2d5')
        self.resultado_label.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

        # Botón para enviar
        self.boton_enviar = tk.Button(self, text="Diagnosticar", command=self.enviar_valor,
                                       width=20, height=2, font=('Helvetica', 14, "bold"),
                                       bg='#32CD32', fg='black')
        self.boton_enviar.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # Botón para regresar a menu
        self.boton_menu = tk.Button(self, text="← Menú", command=self.regresar_menu, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_menu.place(relx=0.2, rely=.9, anchor=tk.CENTER)

    @staticmethod
    def decision_tree_model_4(C64_21, C49_8_21):
        if C64_21 <= 1.50:
            if C49_8_21 <= 1.50:
                return 2
            else:
                return 2
        else:
            if C49_8_21 <= 1.50:
                return 2
            else:
                return 2
                
    def enviar_valor(self):
        # Obtener el valor seleccionado
        C64_21 = self.C64_21.get()
        C49_8_21 = self.C49_8_21.get()

        # Llamar a la función de decisión y obtener el resultado
        resultado = self.decision_tree_model_4(C64_21, C49_8_21)
        if resultado == 1:
            resultadom1 = "Positivo"
        else:
            resultadom1 = "Negativo"

        # Actualizar el texto en el widget de etiqueta con el resultado
        self.resultado_label.config(text="{}".format(resultadom1), font=('Helvetica', 18), bg='#FF5757')
        
    def regresar_menu(self):
        self.destroy()  # Cerrar la ventana secundaria

##################################################################
##################################################################

class VentanaM5(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Configurar la segunda ventana en pantalla completa
        self.attributes('-fullscreen', True)

        # Cargar la imagen de fondo5
        self.imagen_fondo5 = tk.PhotoImage(file="5.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo5
        self.label_fondo5 = tk.Label(self, image=self.imagen_fondo5)
        self.label_fondo5.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Variable para almacenar el estado de la opción seleccionada
        self.H3_21 = tk.IntVar()
        self.H9_21 = tk.IntVar()
        self.C64_21 = tk.IntVar()
        self.C49_8_21 = tk.IntVar()
        self.C68D_21 = tk.IntVar()

        # Checkbox Sí/No H3_21
        self.checkbox_siH3_21 = tk.Checkbutton(self, text="Sí", variable=self.H3_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siH3_21.place(relx=0.45, rely=0.29, anchor=tk.CENTER)

        self.checkbox_noH3_21 = tk.Checkbutton(self, text="No", variable=self.H3_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noH3_21.place(relx=0.55, rely=0.29, anchor=tk.CENTER)

        # Checkbox Sí/No H9_21
        self.checkbox_siH9_21 = tk.Checkbutton(self, text="Sí", variable=self.H9_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siH9_21.place(relx=0.45, rely=0.44, anchor=tk.CENTER)

        self.checkbox_noH9_21 = tk.Checkbutton(self, text="No", variable=self.H9_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noH9_21.place(relx=0.55, rely=0.44, anchor=tk.CENTER)

        # Checkbox Sí/No C64_21
        self.checkbox_siC64_21 = tk.Checkbutton(self, text="Sí", variable=self.C64_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC64_21.place(relx=0.45, rely=0.54, anchor=tk.CENTER)

        self.checkbox_noC64_21 = tk.Checkbutton(self, text="No", variable=self.C64_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC64_21.place(relx=0.55, rely=0.54, anchor=tk.CENTER)

        # Checkbox Sí/No C49_8_21
        self.checkbox_siC49_8_21 = tk.Checkbutton(self, text="Sí", variable=self.C49_8_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC49_8_21.place(relx=0.45, rely=0.635, anchor=tk.CENTER)

        self.checkbox_noC49_8_21 = tk.Checkbutton(self, text="No", variable=self.C49_8_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC49_8_21.place(relx=0.55, rely=0.635, anchor=tk.CENTER)

        # Checkbox Sí/No C68D_21
        self.checkbox_siC68D_21 = tk.Checkbutton(self, text="Sí", variable=self.C68D_21, onvalue=1, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_siC68D_21.place(relx=0.45, rely=0.735, anchor=tk.CENTER)

        self.checkbox_noC68D_21 = tk.Checkbutton(self, text="No", variable=self.C68D_21, onvalue=2, offvalue=0, font=('Helvetica', 16), bg='#59c2d5')
        self.checkbox_noC68D_21.place(relx=0.55, rely=0.735, anchor=tk.CENTER)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(self, text="", font=('Helvetica', 18), bg='#59c2d5')
        self.resultado_label.place(relx=0.5, rely=0.87, anchor=tk.CENTER)

        # Botón para enviar
        self.boton_enviar = tk.Button(self, text="Diagnosticar", command=self.enviar_valor,
                                       width=20, height=2, font=('Helvetica', 14, "bold"),
                                       bg='#32CD32', fg='black')
        self.boton_enviar.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # Botón para regresar a menu
        self.boton_menu = tk.Button(self, text="← Menú", command=self.regresar_menu, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_menu.place(relx=0.2, rely=.9, anchor=tk.CENTER)

    @staticmethod
    def decision_tree_model_5(C68D_21, C64_21, H3_21, C49_8_21, H9_21):
        if C68D_21 <= 1.50:
            if C64_21 <= 1.50:
                return 2
            else:
                if H3_21 <= 1.50:
                    if C49_8_21 <= 1.50:
                        if H9_21 <= 1.50:
                            return 1
                        else:
                            return 1
                    else:
                        return 1
                else:
                    if H9_21 <= 1.50:
                        return 1
                    else:
                        return 1
        else:
            if H3_21 <= 1.50:
                if H9_21 <= 1.50:
                    if C49_8_21 <= 1.50:
                        if C64_21 <= 1.50:
                            return 2
                        else:
                            return 2
                    else:
                        if C64_21 <= 1.50:
                            return 2
                        else:
                            return 1
                else:
                    if C49_8_21 <= 1.50:
                        if C64_21 <= 1.50:
                            return 2
                        else:
                            return 2
                    else:
                        if C64_21 <= 1.50:
                            return 2
                        else:
                            return 2
            else:
                if C49_8_21 <= 1.50:
                    if C64_21 <= 1.50:
                        if H9_21 <= 1.50:
                            return 2
                        else:
                            return 2
                    else:
                        if H9_21 <= 1.50:
                            return 2
                        else:
                            return 2
                else:
                    if C64_21 <= 1.50:
                        if H9_21 <= 1.50:
                            return 2
                        else:
                            return 2
                    else:
                        if H9_21 <= 1.50:
                            return 2
                        else:
                            return 2

                
    def enviar_valor(self):
        # Obtener el valor seleccionado
        H3_21 = self.H3_21.get()
        H9_21 = self.H9_21.get()
        C64_21 = self.C64_21.get()
        C49_8_21 = self.C49_8_21.get()
        C68D_21 = self.C68D_21.get()

        # Llamar a la función de decisión y obtener el resultado
        resultado = self.decision_tree_model_5(C68D_21, C64_21, H3_21, C49_8_21, H9_21)
        if resultado == 1:
            resultadom1 = "Positivo"
        else:
            resultadom1 = "Negativo"

        # Actualizar el texto en el widget de etiqueta con el resultado
        self.resultado_label.config(text="{}".format(resultadom1), font=('Helvetica', 18), bg='#FF5757')
        
    def regresar_menu(self):
        self.destroy()  # Cerrar la ventana secundaria

##################################################################
##################################################################

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.title("DIAPRESOFT")
        self.attributes('-fullscreen', True)  # Pantalla completa

        # Cargar la imagen de fondo
        self.imagen_fondo = tk.PhotoImage(file="fondo.png")

        # Crear un widget de etiqueta para mostrar la imagen de fondo
        self.label_fondo = tk.Label(self, image=self.imagen_fondo)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Llenar toda la ventana

        # Botones para modelos 
        modelos = ['I', 'II', 'III', 'IV', 'V']
        for i, modelo in enumerate(modelos):
            if modelo == 'I':
                comando = self.mostrar_ventanam1
            elif modelo == "II":
                comando = self.mostrar_ventanam2
            elif modelo == "III":
                comando = self.mostrar_ventanam3
            elif modelo == "IV":
                comando = self.mostrar_ventanam4
            elif modelo == "V":
                comando = self.mostrar_ventanam5
            else:
                comando = lambda m=modelo: self.mostrar_modelo(m)
            boton_modelo = tk.Button(self, text=f"Modelo {modelo}", 
                                     command=comando,
                                     width=20, height=2, font=('Helvetica', 14, 'bold'), 
                                     bg="#0CC0DF", fg='black')
            boton_modelo.place(relx=0.8, rely=0.3 + i * 0.1, anchor=tk.CENTER)

        # Botón para salir
        self.boton_salir = tk.Button(self, text="Salir", command=self.confirmar_salir, 
                                     width=20, height=2, font=('Helvetica', 14, "bold"), 
                                     bg='#FF5757', fg='black')
        self.boton_salir.place(relx=0.8, rely=0.9, anchor=tk.CENTER)
        
    def mostrar_modelo(self, modelo):
        messagebox.showinfo(f"Modelo {modelo}", f"Seleccionaste el modelo {modelo}")

    def mostrar_ventanam1(self):
        ventanaM1 = VentanaM1()

    def mostrar_ventanam2(self):
        ventanaM2 = VentanaM2()

    def mostrar_ventanam3(self):
        ventanaM3 = VentanaM3()

    def mostrar_ventanam4(self):
        ventanaM4 = VentanaM4()

    def mostrar_ventanam5(self):
        ventanaM5 = VentanaM5()

    def confirmar_salir(self):
        respuesta = messagebox.askokcancel("Confirmar salida", "¿Estás seguro de que quieres salir?")
        if respuesta:
            self.destroy()  # Cerrar la ventana de la aplicación

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
