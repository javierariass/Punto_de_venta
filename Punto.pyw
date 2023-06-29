from tkinter import *;
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox as mBox
from tkinter import Menu


#Definicion de las variables globales
productos = []
vproductos = []
vsproductos = []
ventas = []
tarifaT = 0.0
name = []
cantM = []
preciM = []
code = []
aname = [""]
cantD = []
resto = []
nresto = []
password = '123'
value = 0
vname = []
vcode = []
vcant = []
vpreci = []
totald = 0.0
totalm = 0.0

#Establecer direccion de la base de datos
text = ('datos')

#Definicion de las funciones
def calcular():
    nombre = []
    posibilidad = True
    devolver.set(-(tarifaT - efectivo.get()))
    for f  in productos:
        arreglo = f.split("$")
        nombre.append(arreglo[0])
    if(tarifaT > efectivo.get()):
        posibilidad = False
        messagebox.showwarning("Advertencia", "La tarifa es insuficiente para comprar los producos.\nPor favor vuelva a comprobar")
    if posibilidad == True:
        for d in range(len(ventas)):
            for g in range(len(nombre)):
                s = nombre[g]
                if name[d] == s:
                    aname[0] = name[d]
                    acodigo.set(code[g])
                    aprecio.set(float(preciM[g]))
                    acantidad.set(-(int(cantM[d])))
                    actualizar_cantidad()
                    consultar
    if posibilidad == True:
        agrega()
        acumulacion()
    aname[0] = ""
    
def Monton():
    monto.set(tarifaT)

def clean():
    for s in range(len(ventas)):
        f = ventas[0]
        ventas.remove(f)
    for s in range(len(resto)):
        f = resto[0]
        d = nresto[0]
        resto.remove(f)
        nresto.remove(d)
        if resto == "":
            break
    
    aname[0] = ""
    monto.set(0)
    efectivo.set(0)
    devolver.set(0)
    consultar()
    
def agregar():
    try:
        t = producto.get()
        a = cantidad.get()
        e = precio.get()
        c = codigo.get()
        repetido = False

        for elemento in productos:
            if t in elemento:
                messagebox.showwarning("Advertencia", "El producto ya existe")
                repetido = True
        if t == "":
            messagebox.showwarning("Advertencia", "Nombre del producto no valido")
        elif a <= 0 or a ==  "":
            messagebox.showwarning("Advertencia", "La cantidad no es valida")
        elif e  <=  0 or e == "":
             messagebox.showwarning("Advertencia", "El precio no es valido")
        else:
            if repetido == False:
                productos.append(t + "$" + c  + "$" + str(a) + "$" + str(e))
                copiar()
                messagebox.showinfo("Hecho","EL producto fue agregado")
                producto.set("")
                cantidad.set(0)
                precio.set(0)
    except:
        messagebox.showwarning("Advertencia", "Introduzca un numero valido")

def registro():
    nombre = []
    posibilidad = True
    encontre = False
    pase = False
    a = producto1.get()
    b = cantidad1.get()
    global resto, nresto
    tot = len(resto)

    if nresto != "" and resto != "":
        for s in range(len(nresto)):
            f = nresto[s]
            if a == f:
                resto[s] += b
                encontre = True
                i = s
                break
    if encontre == False:
        nresto.append(a)
        resto.append(b)
        i = tot
    if a ==  "":
        messagebox.showwarning("Advertencia", "Nombre del producto no valido")
    else:
        ventas.append(a + "$" + str(b))
    for f  in productos:
        arreglo = f.split("$")
        nombre.append(arreglo[0])
    for d in range(len(ventas)):
        for g in range(len(nombre)):
            s = nombre[g]
            if a == s:
                if int(cantD[g])  < resto[i]:
                    posibilidad = False
                   
         
    if posibilidad == True:
        copiar()
        cantidad.set(1)
        
    elif posibilidad == False:
        messagebox.showwarning("Advertencia", "No tienes suficientes existencias para vender de " + nresto[i])
        ventas.remove(a + "$" + str(b))
        resto[i] = resto[i] - b


def copiar():
    base = open(text, 'w')
    productos.sort()
    for elemento in productos:
        base.write(elemento + "\n")
    cargar()
    consultar()
    base.close()

def copiador():
    balances = open("Balance","w")
    vproductos.sort()
    for elemento in vproductos:
        balances.write(elemento + "\n")
    reload()
    acumulacion()
    balances.close()

def copy():
    total = open("Balancem", "w")
    vsproductos.sort()
    for elemento in vsproductos:
        total.write(elemento + '\n')
    load()
    acumulacion()
    total.close()

def eliminar():
    eliminado = eliminate.get()
    removido = False
    for elemento in productos:
        arreglo = elemento.split("$")
        if eliminate.get() == arreglo[0]:
            respuesta = messagebox.askyesno("Eliminacion", "Seguro que desea eliminar el producto:\n" + eliminado)

            if respuesta:
                productos.remove(elemento)
                removido = True
                copiar()
                respuesta = ""

            if removido == True:
                messagebox.showinfo("Eliminado", "Fue eliminado el producto: " + eliminado)
    consultar()
    
def actualizar_codigo():
    encontrado = False
    if aname[0] == "":
        aname[0]  = variable.get()
        actualizar = aname[0]
    def sumar():
        try:
            actualizado = False
            t = arreglo[0]
            c = acodigo.get()
            a = int(arreglo[2]) 
            e = arreglo[3]

            if  a <= 0:
                 a = 0
                 copiar()
                 messagebox.showinfo("Alerta", "El producto se ha quedado sin existencias")
                 productos.remove(elemento)
                 productos.append(t  + "$" +  c  +  "$"  +  str(a)  +  "$"  +  str(e))
                 actualizado = True
                 copiar()
                 acantidad.set(0)
                 aprecio.set(0)
                 
            else:
                productos.remove(elemento)
                productos.append(t + "$" + str(c) + "$" + str(a) + "$" + str(e))
                actualizado = True
                acantidad.set(0)
                aprecio.set(0)
           
        except:
            messagebox.showwarning("Advertencia", "Introduce un numero valido")

    for elemento in productos:
        arreglo = elemento.split("$")
        if  aname[0] == arreglo[0]:
            encontrado = True
            sumar()
            break
        
    if encontrado == False:
        messagebox.showinfo("!!!Alerta!!!", "Ya no existe el producto: " + actualizar)
    aname[0] = ""
    consultar()

def actualizar_cantidad():
    encontrado = False
    if aname[0] == "":
        aname[0]  = variable.get()
        actualizar = aname[0]

    def sumar():
        try:
            actualizado = False
            t = arreglo[0]
            c = arreglo[1]
            a = int(arreglo[2]) + acantidad.get()
            e = arreglo[3]

            if  a <= 0:
                 a = 0
                 copiar()
                 messagebox.showinfo("Alerta", "El producto se ha quedado sin existencias")
                 productos.remove(elemento)
                 productos.append(t  + "$" +  c  +  "$"  +  str(a)  +  "$"  +  str(e))
                 actualizado = True
                 copiar()
                 acantidad.set(0)
                 aprecio.set(0)
                 
            else:
                productos.remove(elemento)
                productos.append(t + "$" + str(c) + "$" + str(a) + "$" + str(e))
                actualizado = True
                acantidad.set(0)
                aprecio.set(0)
           
        except:
            messagebox.showwarning("Advertencia", "Introduce un numero valido")
    for elemento in productos:
        arreglo = elemento.split("$")
        if  aname[0] == arreglo[0]:
            encontrado = True
            sumar()
            break
        
    if encontrado == False:
        messagebox.showinfo("!!!Alerta!!!", "Ya no existe el producto: " + actualizar)
    aname[0] = ""
    consultar()

def actualizar_precio():   
    encontrado = False
    if aname[0] == "":
        aname[0]  = variable.get()
        actualizar = aname[0]

    def sumar():
        try:
            actualizado = False
            t = arreglo[0]
            c = arreglo[1]
            a = int(arreglo[2])
            e = aprecio.get()

            if  e <= 0:                
                 messagebox.showwarning("Alerta", "El precio no es valido")
                                
            else:
                productos.remove(elemento)
                productos.append(t + "$" + str(c) + "$" + str(a) + "$" + str(e))
                actualizado = True
                acantidad.set(0)
                aprecio.set(0)
           
        except:
            messagebox.showwarning("Advertencia", "Introduce un numero valido")

    for elemento in productos:
        arreglo = elemento.split("$")
        if  aname[0] == arreglo[0]:
            encontrado = True
            sumar()
            break
        
    if encontrado == False:
        messagebox.showinfo("!!!Alerta!!!", "Ya no existe el producto: " + actualizar)
    aname[0] = ""
    consultar()

   
def consultar():
    
    a = Text(tab2,width = 40, height = 20)
    barra1 = Scrollbar(tab2, command = a.yview)
    ventas.sort()
    elemental = []
    r = Text(tab1, width = 55, height = 15)
    barra2 = Scrollbar(tab1, command = r.yview)
    productos.sort()
    elementos = []
    pre = []
    can = []
    cant = []
    cod = []
    codt =[]
    prec = []
    tarifa = 0.0
    cantm = 0
    precim = 0.0
    arreglos = []
    cane = []

    if productos == []:
        elementos.append("")
    r.insert(INSERT," Producto       Codigo       Cantidad          Precio\n")
    r.insert(INSERT,"-------------------------------------------------------\n")

    for elemento in productos:
        arreglo = elemento.split("$")
        pre.append(arreglo[3])
        cod.append(arreglo[1])
        cane.append(arreglo[2])
        elementos.append(arreglo[0])
        
        r.insert(INSERT, " " + arreglo[0]  +  "          \t\t"   +  arreglo[1]  +  "\t \t"  +  arreglo[2]  +   "\t\t"  + arreglo[3] +  "\n" )
        r.insert(INSERT,"-------------------------------------------------------\n")

    if ventas == []:
        elemental.append("")
    a.insert(INSERT," Producto      Cantidad          Precio\n")
    a.insert(INSERT,"----------------------------------------\n")

    for element in ventas:
        arreglos = element.split("$")
        elemental.append(arreglos[0])
        cant.append(arreglos[1])
        for s in range (len(elementos)):
            if arreglos[0] == elementos[s]:
                f = s
        a.insert(INSERT, " " + arreglos[0]  +  "\t\t"   +  arreglos[1]  +  "\t \t"  +  pre[f] +  "\n" )
        a.insert(INSERT,"---------------------------------------\n")
        prec.append(pre[f])
        codt.append(cod[f])
        tarifa = tarifa + (float(arreglos[1]) * float( pre[f]))

    global name, cantM, preciM, code, cantD,tarifaT, vname, vcode, vcant, vpreci
    name = elemental
    vname = elemental
    cantM = cant
    vcant = cant
    vpreci = prec
    vcode = codt
    preciM = pre
    code = cod
    cantD = cane
    tarifaT = tarifa
    
    pro = Label(tab1, text = "Producto:", font = 12).place(x = 700, y = 50)

    prod1 = ttk.Combobox(tab2,width = 25, font = 12, textvariable = producto1)
    prod1['values'] = elementos
    prod1.place(x = 120, y = 50, height = 30)
    prod1.current(0)
    
    actu = Label(tab1, text = "Producto:", font = 12).place(x = 700, y = 50)
    actualiza = ttk.Combobox(tab1,state = 'readonly',width = 25, font = 12, textvariable = variable)
    actualiza['values'] = elementos
    actualiza.place(x = 790, y = 50, height = 30)
    actualiza.current(0)

    delet = Label(tab1, text = "Producto:", font = 12).place(x = 510 , y = 450)
    elimina = ttk.Combobox(tab1,state = 'readonly',width = 25, font = 12, textvariable = eliminate)
    elimina['values'] = elementos
    elimina.place(x = 600, y = 450,height = 30)
    elimina.current(0)

    a.place( x = 30, y = 180)
    barra1.place(x = 355, y = 180, height = 328, width = 22)
    a.config(yscrollcommand = barra1.set)
    a.config(state = DISABLED)
    r.place( x = 30, y = 400)
    barra2.place(x = 480, y = 400, height = 250, width = 20)
    r.config(yscrollcommand = barra2.set)
    r.config(state = DISABLED)
    
def abrir():
    base = open(text, 'a')
    balances = open("Balance","a")
    total = open("Balancem","a")
    base.close()
    balances.close()
    total.close()

        
def reload():
    balances = open('Balance', 'r')
    linea = balances.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            vproductos.append(linea)
            linea = balances.readline()
        balances.close()

def load():
    total = open("Balancem","r")
    linea = total.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea [:-1]
            vsproductos.append(linea)
            linea = total.readline()
        total.close()
        
def cargar ():
    base = open(text, 'r')
    linea = base.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            productos.append(linea)
            linea = base.readline()
        base.close()      

def acumulacion ():
    vproductos.sort()
    elementos = []
    s = Text(tab3,width = 50, height = 35)
    f = Text(tab3,width = 50, height = 35)
    s.insert(INSERT," Producto         Codigo    Cantidad     Precio\n")
    s.insert(INSERT,"--------------------------------------------------\n")

    for elemento in vproductos:
        arreglo = elemento.split("$")
        s.insert(INSERT, " " + arreglo[0]  +  "            \t\t"   +  arreglo[1]  +  "\t       "  +  arreglo[2]  +   "\t         "  + arreglo[3] +  "\n" )
        s.insert(INSERT,"--------------------------------------------------\n")
    f.insert(INSERT," Producto         Codigo    Cantidad     Precio\n")
    f.insert(INSERT,"--------------------------------------------------\n")
    for elementos in vsproductos:
        arreglos = elementos.split("$")
        f.insert(INSERT, " " + arreglos[0]  +  "            \t\t"   +  arreglos[1]  +  "\t       "  +  arreglos[2]  +   "\t         "  + arreglos[3] +  "\n" )
        f.insert(INSERT,"--------------------------------------------------\n")
    s.place( x = 30, y = 50)
    f.place( x = 650, y = 50)
    s.config(state = DISABLED)
    f.config(state = DISABLED)
    sa = Label(tab3, text = "Ventas del Dia", font = 12).place(x = 150, y = 20)
    fa = Label(tab3, text = "Ventas Totales", font = 12).place(x = 790, y = 20)
    Button_cerrar_dia = Button(tab3, text = "Cerrar dia", font = 12,width = 15,command = vaciar).place(x =450, y = 300)
    tot1 = Label(tab3, text = "Total:", font = 12).place(x = 100, y = 630)
    atot1 = Entry(tab3, state = DISABLED, textvariable = diario,font = 12).place(x = 170, y = 632)
    tot2 = Label(tab3, text = "Total:", font = 12).place(x = 660, y = 630)
    atot2 = Entry(tab3, state = DISABLED, textvariable = mensual,font = 12).place(x = 730, y = 632)
    
def agrega():
    nombres = []
    cantidad = []
    precio = []
    codigo = []
    h = 0
    ventat = []
    encontre = False
    global totald
    totald = 0
    
    if vproductos == []:
        if len(name) == 1:
            nombres = vname
            cantidad = vcant
            codigo = vcode
            precio = vpreci
            vproductos.append(nombres[0] + "$" + codigo[0] + "$" + str(cantidad[0]) + "$" + str(precio[0]))

        else:
            nombres.append(vname[0])
            precio.append(vpreci[0])
            codigo.append(vcode[0])

            for s in range(len(vname)):
                if s + 1 < len(vname) and vname[s]  != vname[s+1]:
                    if vpreci[s] != vpreci[s+1]:
                        nombres.append(vname[s+1])
                        precio.append(vpreci[s+1])
                        codigo.append(vcode[s+1])

            for s in range(len(nombres)):
                cantidad.append(0)

            for s in range(len(nombres)):
                g = nombres[s]
                c = precio[s]
                for a  in range(len(vname)):
                    d = vname[a]
                    v = precio[s]
                    if d == g and c == v:
                        cantidad[s] +=  int(vcant[a])
            for elemento in vproductos:
                f = vproducto[0]
                vproducto.remove(f)
            for s in range(len(nombres)):
                vproductos.append(nombres[s] + "$" + codigo[s] + "$" + str(cantidad[s]) + "$" + str(precio[s]))

    else:
        for elemento in vproductos:
            arreglo = elemento.split("$")
            nombres.append(arreglo[0])
            codigo.append(arreglo[1])
            cantidad.append(arreglo[2])
            precio.append(arreglo[3])
        for s in range(len(nombres)):
            g = nombres[s]
            c = precio[s]
            for a  in range(len(vname)):
                d = vname[a]
                v = vpreci[a]
                if d == g and v == c:
                    cantidad[s] = str(int(cantidad[s])  +  int(vcant[a]))
        for s in range(len(vname)):
            for d in range(len(nombres)):
                if nombres[d] == vname[h]:
                    if precio[d] == vpreci[h]:
                        encontre = True
            if encontre == True:
                h += 1
                encontre = False
            else:
                nombres.append(vname[h])
                cantidad.append(vcant[h])
                precio.append(vpreci[h])
                codigo.append(vcode[h])
                h += 1
                        
        for s in range(len(vproductos)):
            d = vproductos[0]
            vproductos.remove(d)
        for s in range(len(nombres)):
            vproductos.append(nombres[s] + "$" + codigo[s] + "$" + str(cantidad[s]) + "$" + str(precio[s]))
            
    totales()
    copiador()
    acumulacion()

def vaciar():
    nombres = []
    cantidad = []
    precio = []
    codigo = []
    encontre = False
    h = 0
    global vname,vcode,vpreci,vcant
    vname = []
    vcode = []
    vpreci = []
    vcant = []
    if vname == []:
            for element in vproductos:
                arreglo1 = element.split("$")
                vname.append(arreglo1[0])
                vcode.append(arreglo1[1])
                vcant.append(arreglo1[2])
                vpreci.append(arreglo1[3])
    respuesta = messagebox.askyesno("Advertencia", "Esta seguro q desea cerrar el dia.")
    if respuesta:
        if vsproductos == []:
            for elemento in vproductos:
                vsproductos.append(elemento)
        else:                  
            for elementos in vsproductos:
                arreglo = elementos.split("$")
                nombres.append(arreglo[0])
                codigo.append(arreglo[1])
                cantidad.append(arreglo[2])
                precio.append(arreglo[3])
            for s in range(len(nombres)):
                g = nombres[s]
                c = precio[s]
                for a  in range(len(vname)):
                    d = vname[a]
                    v = vpreci[a]
                    if d == g and v == c:
                        cantidad[s] = str(int(cantidad[s])  +  int(vcant[a]))
            for d in range(len(vname)):
                for s in range(len(nombres)):
                    if nombres[s] == vname[h]:
                        if vpreci[h] == precio[s]:
                            encontre = True
                        
                if encontre == True:
                    h += 1
                    encontre = False
                else:
                    nombres.append(vname[h])
                    cantidad.append(vcant[h])
                    precio.append(vpreci[h])
                    codigo.append(vcode[h])
                    
            for s in range(len(vsproductos)):
                d = vsproductos[0]
                vsproductos.remove(d)
            for s in range(len(nombres)):
                vsproductos.append(nombres[s] + "$" + codigo[s] + "$" + str(cantidad[s]) + "$" + str(precio[s]))
        for s in range(len(vproductos)):
            f = vproductos[0]
            vproductos.remove(f)
            
    copy()
    copiador()
    totales()
    acumulacion()

def totales():
    nombres = []
    cantidad = []
    precio = []
    codigo = []
    nombres1 = []
    cantidad1 = []
    precio1 = []
    codigo1 = []
    global totald,totalm
    totald = 0.0
    totalm = 0.0
    for elemento in vproductos:
            arreglo = elemento.split("$")
            nombres.append(arreglo[0])
            codigo.append(arreglo[1])
            cantidad.append(arreglo[2])
            precio.append(arreglo[3])
    for elementos in vsproductos:
            arreglos = elementos.split("$")
            nombres1.append(arreglos[0])
            codigo1.append(arreglos[1])
            cantidad1.append(arreglos[2])
            precio1.append(arreglos[3])

    for s in range(len(nombres)):
        totald += float(cantidad[s]) * float(precio[s])
        diario.set(totald)
        
    for s in range(len(nombres1)):
        totalm += float(cantidad1[s]) * float(precio1[s])
        mensual.set(totalm)

def comparar_password():
    a = contra.get()
    global value
    if a == password:
        value = 1
    else:
        value = 0
    if value == 1:
        ven.destroy()
    else:
        messagebox.showwarning("Advertencia", "ContraseÃ±a incorrecta")
        
def version():
    mBox.showinfo('Acerca de', 'Nombre: Inventario\nVersion: 2.0d\nFecha de desarrollo: 16-2-2021\nDesarrollo y programacion: Javier Arias Sotolongo\nColaboradores: Joan Manuel Sandianes')

def actua():
    mBox.showinfo("Detalles de la actualizacion", "Mejoras\n-AÃ±adida pestaÃ±a de Cuadre.")

#Definicion de contraseÃ±a
ven = Tk()
ven.title("Password")
ven.geometry('250x150')
ven.resizable(0,0)
contra = StringVar()
pa = Label(ven, text = "Enter password",font = 12).place(x = 50, y = 20)
pas = Entry(ven, textvariable= contra,font = 12)
pas.config(show = "*")
pas.place(x = 15, y = 60)
Button_introducir = Button(ven,text = 'Introducir', command = comparar_password,font = 12).place(x = 69, y = 95)
ven.mainloop()

#Definicion cuerpo princpipal del programal
ventana = Tk()
pestaÃ±as = ttk.Notebook(ventana)
tab2 = ttk.Frame(pestaÃ±as)
tab1 = ttk.Frame(pestaÃ±as)
tab3 = ttk.Frame(pestaÃ±as)
pestaÃ±as.add(tab2, text = "Ventas")
pestaÃ±as.add(tab1, text = "Inventario")
pestaÃ±as.add(tab3, text = "Cuadre")
pestaÃ±as.pack(expand = 1, fill = "both")

#Definicion de variables de la funcion agregar
producto  =  StringVar()
codigo = StringVar("")
cantidad = IntVar()
precio = DoubleVar()
precio.set(0)

#Definicion de variables de la funcion actualizar
variable = StringVar()
acodigo = StringVar()
aprecio = DoubleVar()
aprecio.set(0)
acantidad = IntVar()

#Definicion de la variable de la funcion eliminar
eliminate = StringVar()

#Definicion de las variables de la pestaÃ±a ventas
producto1 = StringVar()
cantidad1 = IntVar()
cantidad1.set(1)
monto = DoubleVar()
monto.set(0)
efectivo = DoubleVar()
efectivo.set(0)
devolver = DoubleVar()
devolver.set(0)

#Definicion de variables pestaÃ±a cuadre
diario = DoubleVar()
mensual = DoubleVar()

#Llamada a funciones de uso
if value == 1:
    abrir()
    cargar()
ðø           |    €H   X           4       ‰             ‰                                          Q$³   €       |    €H   X           4       Ÿ            Ÿ                                         "v          x    €H   X           4       ÿ            ‰                                          Ž¬öJ  €      €    €P   `           <       ÿ            ©                                          ‘XŽ         t    €H   T           4       ÿ            ©                                          b›Ÿ
  €      `    €0   @                 ÿ                             õÓ#  à      \    €0   <                  ÿ                             m½á  @      ¼    ˜|   Œ      0                     L      ÿ               ÿ           ­          !                      ©#¤µßé¬      gDX«         È    ˜ˆ   ˜      0                     X      ÿ               ÿ          $ ÿ         ©#¤µßé¬í                      ©#¤µßé¬          \DÕ­	  Ð      È    ˆˆ   ˜      0                     X       ÿ                ÿ           $ ÿ         ©#¤µßé¬í                      ©#¤µßé¬          ‹u'«
         t    €H   T           4       ÿ                ÿ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
