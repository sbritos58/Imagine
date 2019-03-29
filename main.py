import kivy
kivy.require('1.9.0')
import re
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty,ObjectProperty,ListProperty
from kivy.uix.gridlayout import GridLayout
import sqlite3
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


Builder.load_string("""
#*********************************************** COMIENZO DE PANTALLA INICIO*******************************************************

<Inicio>:
    name:"Inicio"
#***********************************FLOATLAYOUR SIRVE PARA ESTRUCTURAR EL PROGRAMA INDEPENDIENTEMENTE*****************************
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
#*******************************AsyncImage nos permite poner una imagen con propiedades creadas por nosotros*******************************
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'logo.png'  


        Label:
            text:"[i][b][color=4286f4][u]Hoy podemos hacer la diferencia[/color][/b][/u][/i]"
#**********************************markup habilita poner codigos en el mismo texto como arriba*****************************************
            markup:True
            

        Button:
            text:"ENTRAR"
            pos_hint:{'center_x':.5,'y':.13}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
                root.manager.current = "ior"

#**********************************FIN DE PANTALLA DE INICIO Y COMIENZO DE INICIO DE SESION O LOGIN***********************************

<ior>:
    name:"ior"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'logo.png'


        Button:
            pos_hint:{'center_x':.5,'y':.23}
            size_hint:.4,.05
            text:"INICIAR SESIÓN"
            
#**************************************para cambiar color totalmente de un boton hay que ponerlo asi**************************
            background_normal: '' 
            background_color: 1, .3, .4, 1  
#***************************************************fin color de boton*********************************************************
            on_press:
                root.manager.transition.direction= "left"
                root.manager.transition.duration = .3
                root.manager.current = "IniciarSesion"

        Button:
            pos_hint:{'center_x':.5,'y':.13}
            size_hint:.4,.05
            
            text:"REGISTRARSE"
            background_normal: '' 
            background_color: 1, .3, .4, 1
            on_press:
                root.manager.transition.direction= "left"
                root.manager.transition.duration = .3
                root.manager.current = "Registro"

#******************************************FIN DE INICIO SESION Y COMIENZO DE INCIAR SESOPM*********************************************

<IniciarSesion>
    name:"ÏniciarSesion"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
            
        Label:
            pos_hint:{'center_x':.5,'y':.4}
            size:root.size
            text:"[i][b][color=4286f4][u]EMAIL[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:usuario_login
            hint_text:"EMAIL"
            pos_hint:{'center_x':.5,'y':.8}
            size_hint:.5,.06
            multiline:False
            write_tab: False
            multiline: False
            
        Label:
            pos_hint:{'center_x':.5,'y':.25}
            size:root.size
            text:"[i][b][color=4286f4][u]CONTRASEÑA[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:contrasena_login
            hint_text:"CONTRASEÑA"
            pos_hint:{'center_x':.5,'y':.65}
            size_hint:.5,.06
            multiline:False
#**********************************************write_tab false permite tabular de un input a otro***************************************
            write_tab:False
            password:True

        Label:
            pos_hint:{'center_x':.5,'y':.005}
            size:root.size
            text:"[i][b][color=4286f4][u][ref=Inicio]¿HAS OLVIDADO TU CONTRASEÑA?[/ref][/color][/b][/u][/i]"
            on_ref_press:root.manager.current = "ContrasenaOlvidada" 
            markup:True

        Button:
            text:"INICIAR SESION"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.validacionregistro()
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3

#******************************************FIN DE INICIO DE SESION INICIO DE REGISTRO******************************
<ContrasenaOlvidada>:
    name:"ContrasenaOlvidada"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
            
        Label:
            pos_hint:{'center_x':.5,'y':.4}
            size:root.size
            text:"[i][b][color=4286f4][u]INGRESE SU EMAIL[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:email
            hint_text:"INGRESE SU EMAIL"
            pos_hint:{'center_x':.5,'y':.8}
            size_hint:.5,.06
            multiline:False
            write_tab: False

        TextInput:
            id:contrasenaperdida
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.5,.06
            multiline:False
            readonly:True
            write_tab: False


        Button:
            pos_hint:{'center_x':.5,'y':.13}    
            size_hint:.4,.05
            text:"PEDIR CONTRASENA"
            background_normal: '' 
            background_color: 1, .3, .4, 1
            on_press:
                root.buscarcontrasena(email.text)
               # root.current.manager("IniciarSesion")

        

        

<Registro>:
    name:"Registro"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'empresa.png'


        Button:
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.4,.05
            text:"ORGANIZACIONES"
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            #---------------------------
            on_press:
                root.manager.transition.direction= "left"
                root.manager.transition.duration = .3
                root.manager.current = "Organizaciones"
            
    
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.2}
            size_hint:.3,.3
            source:'personal.png'

        Button:
            pos_hint:{'center_x':.5,'y':.13}    
            size_hint:.4,.05
            text:"PERSONAL"
            background_normal: '' 
            background_color: 1, .3, .4, 1
            on_press:
                root.manager.transition.direction= "left"
                root.manager.transition.duration = .3
                root.manager.current = "Personal" 
                   

#*************************************FIN DE REGISTRO Y COMIENZO DE PANTALLA ORGANIZACIONES************************************************

<Organizaciones>:
    name:"Organizaciones"       
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
            
        Label:
            pos_hint:{'center_x':.5,'y':.4}
            size:root.size
            text:"[i][b][color=4286f4][u]NOMBRE DE LA ORGANIZACIÓN[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:nombre_organizacion
            hint_text:"NOMBRE ORGANIZACION"
            pos_hint:{'center_x':.5,'y':.8}
            size_hint:.5,.06
            multiline:False
            write_tab: False
            multiline: False
            
        Label:
            pos_hint:{'center_x':.5,'y':.25}
            size:root.size
            text:"[i][b][color=4286f4][u]NOMBRE DEL USUARIO[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:usuario_organizacion
            hint_text:"NOMBRE DE USUARIO"
            pos_hint:{'center_x':.5,'y':.65}
            size_hint:.5,.06
            multiline:False
#**********************************************write_tab false permite tabular de un input a otro***************************************
            write_tab:False

        Label:
            pos_hint:{'center_x':.5,'y':.1}
            size:root.size
            text:"[i][b][color=4286f4][u]EMAIL[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:email_organizacion
            hint_text:"EMAIL"
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.5,.06
            multiline:False
            write_tab:False


        Label:
            pos_hint:{'center_x':.5,'y':-.05}
            size:root.size
            text:"[i][b][color=4286f4][u]NUMERO DE TELEFONO[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:telefono_organizacion
            hint_text:"TELEFONO"
            pos_hint:{'center_x':.5,'y':.35}
            size_hint:.5,.06
            multiline:False
            write_tab:False
            input_filter:"int"


        Label:
            pos_hint:{'center_x':.5,'y':-.2}
            size:root.size
            text:"[i][b][color=4286f4][u]CONTRASEÑA[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:contrasena_organizacion
            hint_text:"CONTRASEÑA"
            pos_hint:{'center_x':.5,'y':.2}
            size_hint:.5,.06
            multiline:False
            write_tab:False
            password:True


        Button:
            text:"REGISTRARME"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.guardar_nombre(nombre_organizacion.text,usuario_organizacion.text,email_organizacion.text,telefono_organizacion.text,contrasena_organizacion.text)
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
        
<Personal>:
    name:"Personal"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
            
        Label:
            pos_hint:{'center_x':.5,'y':.4}
            size:root.size
            text:"[i][b][color=4286f4][u]NOMBRE[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:nombre_usuario
            hint_text:"NOMBRE"
            pos_hint:{'center_x':.5,'y':.8}
            size_hint:.5,.06
            multiline:False
            write_tab: False
            multiline: False
            
        Label:
            pos_hint:{'center_x':.5,'y':.25}
            size:root.size
            text:"[i][b][color=4286f4][u]APELLIDO[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:apellido_usuario
            hint_text:"APELLIDO"
            pos_hint:{'center_x':.5,'y':.65}
            size_hint:.5,.06
            multiline:False
#**********************************************write_tab false permite tabular de un input a otro***************************************
            write_tab:False

        Label:
            pos_hint:{'center_x':.5,'y':.1}
            size:root.size
            text:"[i][b][color=4286f4][u]EMAIL[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:email_usuario
            hint_text:"EMAIL"
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.5,.06
            multiline:False
            write_tab:False


        Label:
            pos_hint:{'center_x':.5,'y':-.05}
            size:root.size
            text:"[i][b][color=4286f4][u]CONTRASEÑA[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:contrasena_usuario
            hint_text:"CONTRASEÑA"
            pos_hint:{'center_x':.5,'y':.35}
            size_hint:.5,.06
            multiline:False
            write_tab:False
            password:True


        Button:
            text:"REGISTRARME"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.guardar_nombre_usuario(nombre_usuario.text,apellido_usuario.text,email_usuario.text,contrasena_usuario.text)
                root.manager.transition.direction = "right"
                root.manager.transition.duration = .3


<RegistroExitoso>:
    name:"RegistroExitoso"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'logo.png'  


        Label:
            text:"[i][b][color=4286f4][u]GRACIAS POR REGISTRARTE EN[/color][/b][/u][/i]"
            markup:True
        Label:
            text:"[i][b][color=4286f4][u]IMAGINE[/color][/b][/u][/i]"
            pos_hint:{'center_x':.5,'y':-.1}
            markup:True

        Button:
            text:"INICIAR SESION"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
                root.manager.current = "IniciarSesion"


<DonatarioDonador>:
    name:"DonatarioDonador"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'logo.png'  

        Button:
            text:"BENEFICIARIO"
            pos_hint:{'center_x':.5,'y':.3}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
                root.manager.current = "Donatario"

        Button:
            text:"DONADOR"
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
                root.manager.current = "Donador"

<Donatario>:
    orientation:"vertical"
    name:"Donatario"
    ScreenManager:
        Screen:
            FloatLayout:
                canvas:
                    Color:
                        rgb:1,1,1
                    Rectangle:
                        size:self.size
                        pos:self.pos
                AsyncImage:
                    pos_hint:{'center_x':.5,'y':.6}
                    size_hint:.3,.3
                    source:'logo.png'

                ExampleRV:
                    pos_hint:{'center_x':.5,'y':.05}
                    size_hint:.4,.4
                    background_normal: '' 
                    background_color: 1, .3, .4, 1 



<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (0,0,0,1) if self.selected else (1, .3, .4, 1 )
        Rectangle:
            pos: self.pos
            size: self.size
        
                
<ExampleRV>:
    
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
        

<Donador>:
    name:"Donador"       
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
            
        Label:
            pos_hint:{'center_x':.5,'y':.4}
            size:root.size
            text:"[i][b][color=4286f4][u]PRODUCTO A DONAR[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:producto_productos
            hint_text:"PRODUCTO"
            pos_hint:{'center_x':.5,'y':.8}
            size_hint:.5,.06
            multiline:False
            write_tab: False
            multiline: False
            
        Label:
            pos_hint:{'center_x':.5,'y':.25}
            size:root.size
            text:"[i][b][color=4286f4][u]CANTIDAD[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:cantidad_productos
            hint_text:"CANTIDAD"
            pos_hint:{'center_x':.5,'y':.65}
            size_hint:.5,.06
            multiline:False
#**********************************************write_tab false permite tabular de un input a otro***************************************
            write_tab:False
            input_filter:"int"


        Label:
            pos_hint:{'center_x':.5,'y':.1}
            size:root.size
            text:"[i][b][color=4286f4][u]CIUDAD[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:ciudad_productos
            hint_text:"CIUDAD"
            pos_hint:{'center_x':.5,'y':.5}
            size_hint:.5,.06
            multiline:False
            write_tab:False


        Label:
            pos_hint:{'center_x':.5,'y':-.05}
            size:root.size
            text:"[i][b][color=4286f4][u]BARRIO[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:barrio_productos
            hint_text:"BARRIO"
            pos_hint:{'center_x':.5,'y':.35}
            size_hint:.5,.06
            multiline:False
            write_tab:False


        Label:
            pos_hint:{'center_x':.5,'y':-.2}
            size:root.size
            text:"[i][b][color=4286f4][u]DESTINO[/color][/b][/u][/i]"
            markup:True
            
        TextInput:
            id:destino_productos
            hint_text:"DESTINOS"
            pos_hint:{'center_x':.5,'y':.2}
            size_hint:.5,.06
            multiline:False
            write_tab:False


        Button:
            text:"DONAR"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.guardar_producto(producto_productos.text,cantidad_productos.text,ciudad_productos.text,barrio_productos.text,destino_productos.text)
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3

<DonacionExitosa>:
    name:"DonacionExitosa"
    FloatLayout:
        canvas:
            Color:
                rgb:1,1,1
            Rectangle:
                size:self.size
                pos:self.pos
        AsyncImage:
            pos_hint:{'center_x':.5,'y':.6}
            size_hint:.3,.3
            source:'logo.png'  


        Label:
            text:"[i][b][color=4286f4][u]GRACIAS POR AYUDAR A OTROS CON [/color][/b][/u][/i]"
            markup:True
        Label:
            text:"[i][b][color=4286f4][u]IMAGINE[/color][/b][/u][/i]"            
            pos_hint:{'center_x':.5,'y':-.1}
            markup:True

        Button:
            text:"HACER OTRA DONACION"
            pos_hint:{'center_x':.5,'y':.05}
            size_hint:.4,.05
            background_normal: '' 
            background_color: 1, .3, .4, 1  
            on_press:
                root.borrarproductos()
                root.manager.transition.direction = "left"
                root.manager.transition.duration = .3
                root.manager.current = "Donador"



<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'USUARIO O CONTRASEÑA INCORRECTA'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'TOQUE AQUI PARA VOLVER'
        on_press: pop.dismiss()
<AceptarDonacion>:
    id:aceptar
    size_hint: .4, .4
    auto_dismiss: False
    title: 'GRACIAS POR ACEPTAR DONACIÓN'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'SEGUIR'
        on_press: aceptar.dismiss()

<FaltanDatos>:
    id:FaltanDatos
    size_hint: .4, .4
    auto_dismiss: False
    title: 'EMAIL INCORRECTO'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'VOLVER'
        on_press: FaltanDatos.dismiss()

<EmailInvalido>:
    id:EmailInvalido
    size_hint: .4, .4
    auto_dismiss: False
    title: 'EMAIL YA UTLIIZADO'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'VOLVER'
        on_press: EmailInvalido.dismiss()

<ContrasenaInvalida>:
    id:ContrasenaInvalida
    size_hint: .4, .4
    auto_dismiss: False
    title: 'CONTRASEÑA INCORRECTA'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: '4 O MAS CARACTERES'
        on_press: ContrasenaInvalida.dismiss()    

<NoProductos>:
    id:NoProductos
    size_hint: .4, .4
    auto_dismiss: False
    title: 'NO INGRESASTE PRODUCTOS'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'VOLVER'
        on_press: NoProductos.dismiss()  


<Noemail>:
    id:Noemail
    size_hint: .4, .4
    auto_dismiss: False
    title: 'EMAIL INCORRECTO'
    Button:
        background_normal: '' 
        background_color: 1, .3, .4, 1 
        text: 'VOLVER'
        on_press: Noemail.dismiss()  

#*******************************************FIN DE ESTRUCTURA DE PROGRAMA****************************************************



""")
#*********************************************************Variables de organizaciones******************************
organizaciones= []
def agregarabaseorganizaciones():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.executemany("insert into organizacion values(null,?,?,?,?,?,null,null)",[organizaciones])
    print("conecto")
    cur.fetchall()
    con.commit()
    con.close()
#************************************base personal y datos personal******************************************
personal = []
def agregarabasepersonal():
    global personal
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.executemany("insert into particular values(null,?,?,?,?,null,null)",[personal])
    print("conecto")
    cur.fetchall()
    con.commit()
    con.close()
    personal=[]





productos=[]
cantidad=[]
def agregarbaseproductos():
    global productos
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.executemany("insert into producto values(null,?,?,?,?,?)",[productos])
    print("conecto")
    cur.fetchall()
    con.commit()
    con.close()
    productos=[]
producto=[]

def cargarproductosbase():
    global producto
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("select nombre from producto")
    print("se cargaron los productos")
    rows = cur.fetchall()
    for row in rows:
        for i in row:
            producto.append(str(i))
            print(producto)
    con.commit()
    con.close()
    print ("cargue estos datos")
    print (producto)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''
    

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols=2

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            aceptar=AceptarDonacion()
            aceptar.open()
            
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class ExampleRV(RecycleView):

    def __init__(self, **kwargs):
        global producto
        super(ExampleRV, self).__init__(**kwargs)
        cargarproductosbase()
        self.data = [{'text': str(x)} for x in producto]
        print(producto)
        
class Inicio(Screen):
#******************************************funcion para tomar datos de un textinput*****************************
#******************************************creo funcion con parametros que quiero obtener********************************
#******************************************    def mostrar(self,text):arahisaicarg**********************************************
#*************************************lo guardo en una variable text el dato puesto en textinput************************
#******************************************************self.text = text************************************************
#************************************************asi cambio algun id que yo quiera**************************************
#¨*********************************************self.ids["yogui"].text = text*******************************************
#********************************************aca cambio el hint del texto popr defecto************************************
#*****************************************self.ids["text"].hint_text = "hola nuevamente"************************************
    pass
        
class ior(Screen):
    pass

class SesionIniciada(Screen):
    pass

class Donatario(Screen):
    pass
class SimplePopup(Popup):
    pass
class AceptarDonacion(Popup):
    pass
class FaltanDatos(Popup):
    pass
class ContrasenaInvalida(Popup):
    pass
    
class IniciarSesion(Screen):

    
    def validacionregistro(self):
        usuario= self.ids["usuario_login"].text
        contrasena=self.ids["contrasena_login"].text
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        cur.execute("select * from organizacion where email = ? and contrasena = ?",(usuario,contrasena))
        hola = cur.fetchall()
        cur.execute("select * from particular where email = ? and contrasena = ?",(usuario,contrasena))
        chau = cur.fetchall()
        if hola or chau:
            self.manager.current = "DonatarioDonador"
        
                        
        else:
            pops=SimplePopup()
            pops.open()    
            self.ids["usuario_login"].text = ""
            self.ids["contrasena_login"].text=""

class EmailInvalido(Popup):
    pass
class Registro(Screen):
    pass
class NoProductos(Popup):
    pass

class Personal(Screen):
    global personal
    
    def guardar_nombre_usuario(self,nombre_usuario,apellido_usuario,email_usuario,contrasena_usuario):
              

        self.text = nombre_usuario
        self.text = apellido_usuario
        self.text = email_usuario   
        self.text = contrasena_usuario
        email = email_usuario

        if re.match(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",email):
            db = sqlite3.connect('base.db')
            c = db.cursor()
            c.execute('SELECT * from particular WHERE email = "%s"'%(email))  
            if c.fetchone() is not None:
                dat=EmailInvalido()
                dat.open()
                screen_manager.current="Personal"

            else:
                if len(contrasena_usuario) > 3:
                    screen_manager.current="RegistroExitoso"
                    personal.append(nombre_usuario)
                    personal.append(apellido_usuario)
                    personal.append(email_usuario)
                    personal.append(contrasena_usuario)
                    self.ids["nombre_usuario"].text=""
                    self.ids["apellido_usuario"].text=""
                    self.ids["email_usuario"].text=""
                    self.ids["contrasena_usuario"].text=""
                    print ( personal)
                    return agregarabasepersonal()
                else:
                    dat=ContrasenaInvalida()
                    dat.open()
                    screen_manager.current="Personal"
                
        else:
            dat = FaltanDatos()
            dat.open()
            screen_manager.current="Personal"
        
                        
class Organizaciones(Screen):
    global organizaciones

    def guardar_nombre(self,nombre_organizacion,usuario_organizacion,email_organizacion,telefono_organizacion,contrasena_organizacion):
        self.text = nombre_organizacion
        self.text = usuario_organizacion
        self.text = email_organizacion
        self.text = telefono_organizacion
        self.text = contrasena_organizacion

        email = email_organizacion

        if re.match(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",email):
            db = sqlite3.connect('base.db')
            c = db.cursor()
            c.execute('SELECT * from organizacion WHERE email = "%s"'%(email))  
            if c.fetchone() is not None:
                dat=EmailInvalido()
                dat.open()
                screen_manager.current="Organizaciones"

            else:
                if len(contrasena_organizacion) > 3:
                    screen_manager.current="RegistroExitoso"
                    organizaciones.append(nombre_organizacion)
                    organizaciones.append(usuario_organizacion)
                    organizaciones.append(email_organizacion)
                    organizaciones.append(telefono_organizacion)
                    organizaciones.append(contrasena_organizacion)
                    self.ids["nombre_organizacion"].text=""
                    self.ids["usuario_organizacion"].text=""
                    self.ids["email_organizacion"].text=""
                    self.ids["telefono_organizacion"].text=""
                    self.ids["contrasena_organizacion"].text=""
                    print (organizaciones)
                    return agregarabaseorganizaciones()
                else:
                    dat=ContrasenaInvalida()
                    dat.open()
                    screen_manager.current="Organizaciones"
                
        else:
            dat = FaltanDatos()
            dat.open()
            screen_manager.current="Organizaciones"        


class RegistroExitoso(Screen):
    pass

class InicioPerfil(Screen):
    pass
    
class DonatarioDonador(Screen):
    pass

class Donador(Screen):
    def guardar_producto(self, producto_productos,cantidad_productos,ciudad_productos,barrio_productos,destino_productos):
        self.text = producto_productos
        self.text = cantidad_productos
        self.text = ciudad_productos
        self.text = barrio_productos
        self.text = destino_productos
        productos1 = producto_productos
        if productos1 == "":
            dat = NoProductos()
            dat.open()
            screen_manager.current="Donador"
        else:   
            global productos
            screen_manager.current="DonacionExitosa"
            productos.append(producto_productos)
            productos.append(cantidad_productos)
            productos.append(ciudad_productos)
            productos.append(barrio_productos)
            productos.append(destino_productos)
            self.ids["producto_productos"].text=""
            self.ids["cantidad_productos"].text=""
            self.ids["ciudad_productos"].text=""
            self.ids["barrio_productos"].text=""
            self.ids["destino_productos"].text=""

            print(productos)

            return agregarbaseproductos()
class Noemail(Popup):
    pass
              
class DonacionExitosa(Screen):
    global productos
    def borrarproductos(self):
        global productos
        productos=[]
        return productos
screen_manager = ScreenManager()


class ContrasenaOlvidada(Screen):
    def buscarcontrasena(self,email):
        self.text = email
        email1 = email
        db = sqlite3.connect('base.db')
        c = db.cursor()
        c.execute('select * from organizacion where email="{}"'.format(email1))
        usuarios = c.fetchone()
        print(usuarios)
        if usuarios is not None:
            contrasena = usuarios[5]
            print (contrasena)
            self.ids["contrasenaperdida"].text=contrasena
            print(usuarios)
            db.commit()
            db.close()
        elif usuarios is None:
            c.execute('select * from particular where email="{}"'.format(email1))
            usuariosp = c.fetchone()
            print(usuarios)
            if usuariosp is not None:
                contrasena = usuariosp[4]
                print (contrasena)
                self.ids["contrasenaperdida"].text=contrasena
                print(usuariosp)
                db.commit()
                db.close()
            
            else:
                dat = Noemail()
                dat.open()
                self.ids["email"].text=""
                self.ids["contrasenaperdida"].text=""

#*********************El primer parametro pasado hace referencia a la clase mas arriba creada***********************************
#*********************el parametro name="       " hace referencia a la palabra demtro del builder*******************************

screen_manager.add_widget(Inicio(name="Inicio"))
screen_manager.add_widget(ior(name="ior"))
screen_manager.add_widget(IniciarSesion(name="IniciarSesion"))
screen_manager.add_widget(Registro(name="Registro"))
screen_manager.add_widget(Organizaciones(name="Organizaciones"))
screen_manager.add_widget(Personal(name="Personal"))
screen_manager.add_widget(RegistroExitoso(name="RegistroExitoso"))
screen_manager.add_widget(Donador(name="Donador"))
screen_manager.add_widget(Donatario(name="Donatario"))
screen_manager.add_widget(DonatarioDonador(name="DonatarioDonador"))
screen_manager.add_widget(DonacionExitosa(name="DonacionExitosa"))
screen_manager.add_widget(ContrasenaOlvidada(name="ContrasenaOlvidada"))




class MainApp(App):
    title = "IMAGINE"   
    def build(self):
        self.bind(on_start=self.post_build_init)
        return screen_manager

    def post_build_init(self,ev):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
#*************************************************************evento para el escape o boton retroceso de android************************************************
    def hook_keyboard(self, window, key, *largs):
        if key == 27:

            if(screen_manager.current=='Inicio'):
                App.get_running_app().stop()
            elif (screen_manager.current=='ior'):
                screen_manager.current='Inicio'
                screen_manager.transition.direction = "right"
                screen_manager.transition.duration = .1
            elif (screen_manager.current=="Organizaciones"):
                screen_manager.current="Registro"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="Personal"):
                screen_manager.current="Registro"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="IniciarSesion"):
                screen_manager.current="ior"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="RegistroExitoso"):
                screen_manager.current="IniciarSesion"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="Registro"):
                screen_manager.current="ior"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="Donador"):
                screen_manager.current="DonatarioDonador"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="DonatarioDonador"):
                screen_manager.current="IniciarSesion"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="Donatario"):
                screen_manager.current="DonatarioDonador"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="DonacionExitosa"):
                screen_manager.current="DonatarioDonador"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            elif (screen_manager.current=="ContrasenaOlvidada"):
                screen_manager.current="IniciarSesion"
                screen_manager.transition.duration = .1
                screen_manager.transition.direction = "right"
            return True 
  
imagine = MainApp()
imagine.run()