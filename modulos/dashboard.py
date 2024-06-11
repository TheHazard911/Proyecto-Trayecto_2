import tkinter as tk
import customtkinter as ctk
import datetime
import time
import variables as var
from PIL import ImageTk, Image

class Dashboard:
    def __init__(self):
        # definicion de apariencia
        self.configurar_apariencia()
        # creacion de ventana
        self.crear_ventana_principal()
        # imagenes e iconos
        self.importar_img_ico()
        #datetime
        self.datetime()
        # cuadro principal
        self.area_principal_funcion()
        self.panel_izquierdo()
        self.elementos_panel_izquierdo()
        self.panel_superior()
        self.elementos_panel_superior()
    
    
    # configurar apariencia
    def configurar_apariencia(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

    
    # metodo para crear la ventana principal
    def crear_ventana_principal(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Login")
        self.app.resizable(0,0)
        self.app.update_idletasks()

    
    # importando imagenes e iconos
    def importar_img_ico(self):
        # importardo imagen
        self.icono_menu_png = Image.open("imagenes/icono_menu.png")
        self.icono_usuario_png = Image.open("imagenes/login-usuario-blanco.png")  
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.icono_menu_ajustada = self.icono_menu_png.resize((79, 68), Image.LANCZOS)
        self.icono_usuario_ajustada = self.icono_usuario_png.resize((40, 40), Image.LANCZOS)
        # asignando a la variable que va a ser usada
        self.img_menu = ImageTk.PhotoImage(self.icono_menu_ajustada)
        self.img_usuario = ImageTk.PhotoImage(self.icono_usuario_ajustada)
    
    
    # incorporacion de frames y widgets
    def panel_izquierdo(self):
        self.panel_izquierdo = ctk.CTkFrame(master=self.app,
                                    width=196,
                                    height=720,
                                    fg_color=var.bg_gray,
                                    corner_radius=0)

        #------------------posicionamiento----------------------------------#
        self.panel_izquierdo.grid(row=0,column=0)
    
    
    def elementos_panel_izquierdo(self):
        # icono de menu
        self.icono_menu = ctk.CTkLabel(master=self.panel_izquierdo,
                                image=self.img_menu,
                                text="",
                                )
        # texto de menu
        self.texto_menu = ctk.CTkLabel(master=self.panel_izquierdo,
                                    text="Menu",
                                    font=var.Amaranth_medium_large,
                                    text_color=var.text_white)
        
        # botones del menu
        self.boton_inicio = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Inicio",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_grados = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Grados",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_personal = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Personal",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_estudiantes = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Estudiantes",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_perfil = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Perfil",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_salir = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Salir",
                                        width=160,
                                        font=var.Amaranth_small,
                                        fg_color=var.buttons_color,
                                        hover_color=var.hover_buttons_color,
                                        corner_radius=30,
                                        command=self.kill
                                        )
        
        #------------------posicionamiento------------------------------------
        self.icono_menu.place(relx=0.25, rely=0.01, anchor="n")
        self.texto_menu.place(relx=0.7,rely=0.030,anchor="n",)
        self.boton_inicio.place(relx=0.5,rely=0.31,anchor="center")
        self.boton_grados.place(relx=0.5,rely=0.37,anchor="center")
        self.boton_personal.place(relx=0.5,rely=0.43,anchor="center")
        self.boton_estudiantes.place(relx=0.5,rely=0.49,anchor="center")
        self.boton_perfil.place(relx=0.5,rely=0.55,anchor="center")
        self.boton_salir.place(relx=0.5,rely=0.91,anchor="s")
    
    
    #-------------------------funciones de botones-----------------------
    def panel_superior(self):
        self.panel_superior = ctk.CTkFrame(master=self.app,
                                    width=1084,
                                    height=80,
                                    fg_color=var.bg_blue,
                                    corner_radius=0)
        #------------------posicionamiento----------------------------------#
        self.panel_superior.grid(row=0,column=1,sticky="N")
    
    
    def elementos_panel_superior(self):
        self.icono_usuario = ctk.CTkLabel(master=self.panel_superior,
                                image=self.img_usuario,
                                text="",
                                )
        self.texto_usuario = ctk.CTkLabel(master=self.panel_superior,
                                text=f"Bienvenido {"Cargo"} - {"Usuario"}",
                                text_color=var.text_white,
                                font=var.Amaranth_small
                                )
        self.Hora_fecha = ctk.CTkLabel(master=self.panel_superior,
                                    text=f"Fecha actual: {self.fecha_actual} - Ingreso: {self.hora_actual}",
                                    text_color=var.text_white,
                                    font=var.Amaranth_small
                                    )
        #           posicionamiento
        self.icono_usuario.place(relx=0.02, rely=0.5, anchor="w")
        self.texto_usuario.place(relx=0.06, rely=0.55, anchor="w")
        self.Hora_fecha.place(relx=0.98,rely=0.5, anchor="e")
    
    
    def area_principal_funcion(self):
        self.area_contenido = ctk.CTkFrame(master=self.app,
                                    fg_color="green",#-------------------------
                                    width=1084,
                                    height=640,
                                    corner_radius=0)
        #------------------posicionamiento----------------------------------#
        self.area_contenido.grid(column=1,row=0, sticky="s")
    
    
    def datetime(self):
        self.ahora = datetime.datetime.now()
        self.fecha_actual = self.ahora.strftime("%d/%m/%y")
        self.hora_actual = self.ahora.strftime("%I:%M%p")

    
    #iniciar la ventana
    def run(self):
        self.app.mainloop()
    
    
    def kill(self):
        self.app.destroy()


# Crear y ejecutar aplicación
app = Dashboard()
app.run()