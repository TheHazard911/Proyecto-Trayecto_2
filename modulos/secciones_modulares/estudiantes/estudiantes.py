import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from modulos.variables import variables as var
from modulos.secciones_modulares.estudiantes.sub_estudiantes.crear_estudiante import CrearEstudianteVentana
from modulos.secciones_modulares.estudiantes.sub_estudiantes.modificar_estudiante import ModificarEstudianteVentana
from modulos.secciones_modulares.estudiantes.sub_estudiantes.eliminar_estudiante import eliminar_estudiante
from modulos.secciones_modulares.estudiantes.sub_estudiantes.modificar_representante import ModificarRepresentanteVentana
import sqlite3
from PIL import ImageTk, Image


class EstudiantesVentana:
    def __init__(self, master):
        self.master = master
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
            
        self.frame_texto_blanco()
        self.texto_titulo()
        self.importar_img_ico()
        self.botones_seleccion_estudiantes()
        self.input_seleccion_estudiantes()
        self.imagen_de_usuario()
    
    def importar_img_ico(self):
        self.icono_user_original = Image.open("imagenes/usuario-estudiante.png")
        self.icono_user_ajustada = self.icono_user_original.resize((250, 250), Image.LANCZOS)
        self.img_icono_user = ImageTk.PhotoImage(self.icono_user_ajustada)
        
    def imagen_de_usuario(self):
        self.carga_imagen_estudiante = ctk.CTkLabel(master=self.master,
                                                    image=self.img_icono_user,
                                                    text="",
                                                    fg_color="#FFFFFF")
        self.carga_imagen_estudiante.place(relx=0.5,rely=0.70,anchor="center")
    
    def cargar_ventana_crear_estudiante(self):
        self.contenido_ventana_crear_estudiante = CrearEstudianteVentana(master=self.master)
        self.contenido_ventana_crear_estudiante.mostrar()

    
    def cargar_ventana_modificar_estudiante(self, cedula):
        self.contenido_ventana_modificar_estudiante = ModificarEstudianteVentana(self.master, cedula)
        self.contenido_ventana_modificar_estudiante.mostrar()
    
    
    def cargar_ventana_modificar_representante(self, cedula):
        self.contenido_ventana_modificar_representante = ModificarRepresentanteVentana(self.master, cedula)
        self.contenido_ventana_modificar_representante.mostrar()
    
    def frame_texto_blanco(self):
        self.frame_fondo_blanco = ctk.CTkFrame(master=self.master,
                                               width=1000,
                                               height=350,
                                               fg_color="white",
                                               corner_radius=20
                                                )
        self.frame_fondo_blanco.place(relx=0.5,rely=0.7,anchor="center")
        
        
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Informacion de Estudiantes",
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
        
    # botones de estudiantes
    def botones_seleccion_estudiantes(self):
        self.texto_Datos_del_estudiante = ctk.CTkLabel(master=self.master,
                                           text="Ingrese La Cedula",
                                           text_color=var.text_black,
                                           font=var.Andika_small
                                           )
        self.texto_Datos_del_estudiante.place(relx=0.15, rely=0.24, anchor="center")
        
        self.boton_crear_estudiante = self.crear_botones(texto="Registrar Estudiante",
                                                        comando=lambda: self.cargar_ventana_crear_estudiante(),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.150,
                                                        posicion_y=0.15
                                                       )
        self.boton_ver_resultados = self.crear_botones(texto="Buscar Estudiante",
                                                        comando=self.consulta,
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.35,
                                                        posicion_y=0.30
                                                       )
    # input de estudiantes
    def input_seleccion_estudiantes(self):
        validacion_numeros = self.master.register(self.solo_numeros)
        self.input_buscar_estudiantes = ctk.CTkEntry(master=self.master,
                                            width=200,
                                            height=40,
                                            text_color=var.text_black,
                                            font=var.Andika_small_ultra,
                                            validate="key",
                                            validatecommand=(validacion_numeros,'%S')
                                            )
        self.input_buscar_estudiantes.place(relx=0.080, rely=0.30,anchor="w")
    
    
    # texto estudiantes
    def texto_seleccion_estudiantes(self):
        # variables: nombres Apellidos Cedula Edad fecha 
        self.texto_Datos_del_estudiante = self.crear_texto(texto="Datos Del Estudiante",
                                                        posicion_x=0.2,
                                                        posicion_y=0.50,
                                                        fuente=var.Amaranth_medium_small
                                                       )
        self.texto_nombres = self.crear_texto(texto="Nombres",
                                                        posicion_x=0.12,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_apellidos = self.crear_texto(texto="Apellidos",
                                                        posicion_x=0.28,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_cedula = self.crear_texto(texto="Cedula",
                                                        posicion_x=0.42,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_edad = self.crear_texto(texto="Genero",
                                                        posicion_x=0.52,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_fecha = self.crear_texto(texto="Fecha De Nacimiento",
                                                        posicion_x=0.67,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_acciones = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.84,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.boton_modificar_estudiante = self.crear_boton_simple(texto="Editar",
                                                        comando=lambda: self.cargar_ventana_modificar_estudiante(self.input_buscar_estudiantes.get()),
                                                        color_boton=var.button_transparent,
                                                        color_text=var.text_blue,
                                                        posicion_x=0.81,
                                                        posicion_y=0.64
                                                       )
        self.boton_eliminar_estudiante = self.crear_boton_simple(texto="Borrar",
                                                        comando=lambda: self.eliminar_usuario_funcion(),
                                                        color_boton=var.button_transparent,
                                                        color_text=var.text_blue,
                                                        posicion_x=0.87,
                                                        posicion_y=0.64
                                                       )
        
    def variables_seleccion_estudiantes(self):
        cedula = self.input_buscar_estudiantes.get()
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, cedula, fecha_nacimiento, genero FROM Estudiante WHERE cedula = {cedula}")
        info = c.fetchall()
        
        for element in info:
          nombres = f"{element[0]} {element[1]}"
          apellidos = f"{element[2]} {element[3]}"
          cedula = element[4]
          fecha_nacimiento = element[5]
          genero = element[6]

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
      
        # datos # nombre Apellido Cedula Edad 
        lista_datos = (
            # identificador="123",
            nombres,
            apellidos,
            cedula,
            genero,
            fecha_nacimiento
        )
        # self.var_id = self.crear_texto(texto=f"{identificador}",
        #                                                 posicion_x=0.085,
        #                                                 posicion_y=0.68,
        #                                                 fuente=var.Amaranth_small
        #                                                )
        self.var_nombres = self.crear_texto(texto=lista_datos[0],
                                                        posicion_x=0.12,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_apellidos = self.crear_texto(texto=lista_datos[1],
                                                        posicion_x=0.28,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_cedula = self.crear_texto(texto=f"V{lista_datos[2]}",
                                                        posicion_x=0.42,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_edad = self.crear_texto(texto=lista_datos[3],
                                                        posicion_x=0.52,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_fecha = self.crear_texto(texto=lista_datos[4],
                                                        posicion_x=0.67,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        # Llamada a la función con valores específicos

    def variables_seleccion_representantes(self):
        cedula = self.input_buscar_estudiantes.get()
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT R.primer_nombre, R.segundo_nombre, R.primer_apellido, R.segundo_apellido, R.cedula, R.correo, R.telefono, R.direccion FROM Estudiante as E INNER JOIN Representante as R ON R.id_representante = E.id_representante WHERE E.cedula = {cedula};")
        info = c.fetchall()
        # print(info)
        
        for element in info:
          nombres = f"{element[0]} {element[1]}"
          apellidos = f"{element[2]} {element[3]}"
          cedula = element[4]
          correo = element[5]
          telefono = element[6]
          direccion = element[7]

        # print(nombres, apellidos, cedula, correo, telefono, direccion)

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
      
        # datos # nombre Apellido Cedula Edad 
        lista_datos_representante = (
            # identificador="123",
            nombres,
            apellidos,
            cedula,
            correo,
            direccion
        )
        # self.var_id = self.crear_texto(texto=f"{identificador}",
        #                                                 posicion_x=0.085,
        #                                                 posicion_y=0.68,
        #                                                 fuente=var.Amaranth_small
        #                                                )
        self.texto_Datos_del_estudiante = self.crear_texto(texto="Datos Del Representante",
                                                        posicion_x=0.2,
                                                        posicion_y=0.76,
                                                        fuente=var.Amaranth_medium_small
                                                       )
        self.texto_nombres = self.crear_texto(texto="Nombres",
                                                        posicion_x=0.14,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_apellidos = self.crear_texto(texto="Apellidos",
                                                        posicion_x=0.31,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_cedula = self.crear_texto(texto="Cedula",
                                                        posicion_x=0.44,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_edad = self.crear_texto(texto="Correo Electronico",
                                                        posicion_x=0.61,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_fecha = self.crear_texto(texto="Direccion",
                                                        posicion_x=0.77,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_acciones = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.88,
                                                        posicion_y=0.82,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.boton_modificar_representante = self.crear_boton_simple(texto="Editar",
                                                        color_boton=var.button_transparent,
                                                        color_text=var.text_blue,
                                                        comando=lambda: self.cargar_ventana_modificar_representante(cedula),
                                                        posicion_x=0.88,
                                                        posicion_y=0.89
                                                       )
        
        # variables seleccion representantes
        self.var_nombres = self.crear_texto(texto=lista_datos_representante[0],
                                                        posicion_x=0.14,
                                                        posicion_y=0.89,
                                                        fuente=var.Amaranth_small                                          
                                                       )
        self.var_apellidos = self.crear_texto(texto=lista_datos_representante[1],
                                                        posicion_x=0.31,
                                                        posicion_y=0.89,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_cedula = self.crear_texto(texto=f"V{lista_datos_representante[2]}",
                                                        posicion_x=0.44,
                                                        posicion_y=0.89,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_edad = self.crear_texto(texto=lista_datos_representante[3],
                                                        posicion_x=0.61,
                                                        posicion_y=0.89,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_fecha = self.crear_texto(texto=lista_datos_representante[4],
                                                        posicion_x=0.77,
                                                        posicion_y=0.89,
                                                        fuente=var.Amaranth_small             
                                                       )

    
    # Metodos  de creacion generales
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.master,
                                            text=texto,
                                            text_color=var.text_black,
                                            font=fuente,
                                            fg_color="white",
                                            compound="center",
                                            justify="center"
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="center")

        
    #Metodo para crear botones
    def crear_botones(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=130,
                             height=40,
                             font=var.Andika_small_ultra,
                             fg_color=color_boton,
                             hover_color=var.hover_button_blue,
                             corner_radius=5,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y,anchor="center")
    
    def crear_boton_simple(self, texto,color_text, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=20,
                             height=20,
                             font=var.Andika_small_ultra,
                             fg_color=color_boton,
                             text_color=color_text,
                             hover_color=var.hover_button_transparent,
                             corner_radius=5,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y,anchor="center")
        
        
    # logica de consulta 
    
    def consulta(self):
        self.frame_texto_blanco()
        cedula = self.input_buscar_estudiantes.get()
        if cedula:
            try:
                cedula = int(cedula)
        # Resto de tu código aquí
            except ValueError:
                texto_emergente = "No se encuentra una cedula registrada"
                CTkMessagebox(title="Error", message=texto_emergente,font=("calibri",16),icon="cancel")
        # cedula = int(cedula)
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute("SELECT cedula FROM Estudiante")
        info = c.fetchall()

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        
        lista_cedulas = []
        
        for element in info:
          lista_cedulas.append(element[0])

        if cedula in lista_cedulas:
            self.texto_seleccion_estudiantes()
            self.variables_seleccion_estudiantes()
            self.variables_seleccion_representantes() 
        else:
            texto_emergente = "No se encuentra una cedula registrada"
            CTkMessagebox(title="Error", message=texto_emergente,font=("calibri",16),icon="cancel")
            self.imagen_de_usuario()
    
    def solo_numeros(self, char):
        return char.isdigit() # solo numeros
    
    def eliminar_usuario_funcion(self):
        eliminar_estudiante(self.input_buscar_estudiantes.get())
        self.frame_texto_blanco()
        self.imagen_de_usuario()