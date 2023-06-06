#esta es una nueva actualizacion
from tkinter import*
from tkinter import ttk
from functools import partial
import random
from tkinter import messagebox
import time

#evaluar turnos
turno=True


puntosjugador1 =0
puntosjugador2=0

nombre1=" "
nombre2=" "



root2 = Tk()
root2.title('TKINTER game')
root2.geometry("500x500")
root2.config(bg="#FFFFFF")

def selection_changed(event):
    global filas
    global columnas
    selection = combo.get()
    filas = int(selection)
    columnas = int(selection)
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )
    generarMatriz()
combo = ttk.Combobox(root2)
combo = ttk.Combobox(
    state="readonly",
    values=["3", "4", "5", "6", "7", "8"]
)
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=450)

#conteo de puntos jugador 2
Labelpunteos1=ttk.Label(root2, text= "0")
Labelpunteos1.place(x=220, y=280)

#mostrar en pantalla siguiente jugador
labelturn=ttk.Label(root2,text="0")
labelturn.place(x=220, y=400)


#conteo de puntos jugador 1
Labelpunteos3=ttk.Label(root2, text= "0")
Labelpunteos3.place(x=220, y=350)

#Cuantos turnos desea para cada usuario
Labelpunteos2=ttk.Label(root2, text= "Ingrese el numero de los turnos")
Labelpunteos2.place(x=220, y=250)





#texto en pantalla
titulo = ttk.Label(text="Bienvenido a Matriz Aritmetrica", font="Arial")
titulo.place(x =120, y=40)

#texto en pantalla jugador 1
titulo1 = ttk.Label(text="Jugador 1: ")
titulo1.place(x=220,y=100)
titulo2= ttk.Entry(root2, text="Jugador 1: ")
titulo2.place(x=220,y=120)


#texto en pantalla jugador 2
titulo3 = ttk.Label(text="Jugador 2: ")
titulo3.place(x=220,y=190)
titulo4 =ttk.Entry(root2, text="Jugador 2: ")
titulo4.place(x=220, y=210)
titulop =ttk.Entry(root2, text="Turnos")
titulop.place(x=220, y=410)
Tpermitidos = 0

def ingresarcredenciales():
    global nombre1
    nombre1=titulo2.get()
    labelnombre1=ttk.Label(text=str(nombre1))
    labelnombre1.place(x=330, y=250)
   
   
    global nombre2
    nombre2=titulo4.get()
    labelnombre2=ttk.Label(text=str(nombre2))
    labelnombre2.place(x=330, y=280)
    
    global Tpermitidos
    turnoss = titulop.get()
    print("Necesitan " + str(turnoss))
    Tpermitidos = 2 * turnoss
    
    
   
    
    
boton = ttk.Button(text="ingrese: ", command=ingresarcredenciales)
boton.place(x=150+10+150,y=400)
ingrese=ttk.Entry()




inicio = 0
final = 0
detener = False

#Voy a probar algo nuevo
#Crear una ventana en tkinter
root = Tk()
root.title('TKINTER GAME')
root.geometry("700x500")
root.config(bg="#FFFFFF")

filas = 8 #El numero de filas que deseo en la matriz
columnas = 8 # el numero de columnas que deseo en la matriz


#Crear una matriz con numeros aleatorios de 3 columnas y 3 filas
matriz = [[random.randint(0,11) for x in range(columnas)] for y in range(filas)] #Se crea una matriz con numeros aleatoreos con las columnas y filas que deseo.
#label = Label(root, text = "Hola mundo " )
#label.grid(row = 1, column = 0)
#label.config(bg = "#070D0F")

#crear una matriz vacia
anulados=[]#Aqui ire guardando las posiciones de los botones que ya fueron utilizados
sumatoria = 0 #Guardaré la sumatoria de los numeros vecinos
multiplicador = 0
#Se hara una funcion el cual se ejecutara cuando el usuario le de click a un boton de la matriz.
def nuevo_click(i, j):
    global sumatoria #Utilizo la variable sumatoria en modalidad global.
    sumatoria = 0 #Reinicio la variable en 0
    global multiplicador 
    multiplicador = matriz[i][j]
    print(str(i) + " " + str(j))
    #Ahora comprobare si la posición que se envió ya existe en la matriz anulados.
    if [i, j] in anulados: #S
        print('Existe en la matriz')
        messagebox.showinfo(message="No puedes seleccionar este numero", title="Incorrecto")#Envio un mensaje de error para notificar al usuario que ya existe. 
    else:
        #De lo contrario comenzará a mostrar todos los numeros vecinos

        btnLista[i][j].config(bg = "#FFFFFF", relief = "solid", fg = "red")#El numero central se pintara de color rojo.
        
        if i +1 >= filas: #Comprueba si se puede para la parte de abajo. 
            print("No se puede abajo")
        else:
            print(columnas)
            print(j)
            #Si se puede abajo, pintara de azul
            btnLista[i+1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es AC" + str(matriz[i+1][j]))
            sumatoria = sumatoria + matriz[i+1][j]#Sumatoria seria igual a su valor + el valor de esa posicion
            print("LA SUMATORIA ES " + str(sumatoria))
            if j+1 >= columnas:#Verificara si se puede abajo a la derecha.
                print("No se puede abajo derecha")
            else:  
                #En caso que si se pueda, lo pintara de azul
                btnLista[i+1][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue") 
                print("El numero es AD" + str(matriz[i+1][j+1]))
                sumatoria = sumatoria + matriz[i+1][j+1] #Sumatoria seria igual a su valor + el valor de esa posicion
                print("LA SUMATORIA ES " + str(sumatoria))
            
            if j-1 < 0:#Comprobara si se puede abajo izquierda
                print("No se puede abajo izquierda")
            else: 
                #En caso que si se pueda, lo pintara de azul
                btnLista[i+1][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es AI" + str(matriz[i+1][j-1]))
                sumatoria = sumatoria + matriz[i+1][j-1]#Sumatoria seria igual a su valor + el valor de esa posicion
                print("LA SUMATORIA ES " + str(sumatoria))
        
        if i -1 < 0:#Ahora se comprobara si se puede hacia arriba.
            print("No se puede arriba")
        else:
            print(filas)
            print(i)
            btnLista[i-1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es " + str(matriz[i-1][j]))
            sumatoria = sumatoria + matriz[i-1][j]
            print("LA SUMATORIA ES " + str(sumatoria))
            if j+1 >= columnas:
                print("No se puede arriba derecha")
            else:  
                btnLista[i-1][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es " + str(matriz[i-1][j+1]))
                sumatoria = sumatoria + matriz[i-1][j+1]
                print("LA SUMATORIA ES " + str(sumatoria))
            
            if j-1 < 0:
                print("No se puede arriba izquierda")
            else: 
                btnLista[i-1][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
                print("El numero es " + str(matriz[i-1][j-1]))
                sumatoria = sumatoria + matriz[i-1][j-1]
                print("LA SUMATORIA ES " + str(sumatoria))
                
        
                
        if j <= 0:
            print("No se puede a la izquierda")      
        else:
            btnLista[i][j-1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es izquierda" + str(matriz[i][j-1]))
            sumatoria = sumatoria + matriz[i][j-1]
            print("LA SUMATORIA ES " + str(sumatoria))
        
        print(columnas )
        print(j)
        if j+1 >= columnas:
            print("No se puede a la derecha")
        else:
            btnLista[i][j+1].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
            print("El numero es derecha" + str(matriz[i][j+1]))
            sumatoria = sumatoria + matriz[i][j+1]
            print("LA SUMATORIA ES " + str(sumatoria))

        print("CONSULTAS")
        
        print(anulados)
        print("LA SUMATORIA ES " + str(sumatoria))
        
        anulados.append([i,j])
        
        print(anulados)

        global detener
        global inicio
        inicio = time.time()
        print(inicio)
    
        
        #proceso de tiempo limitado del jugador 
def detenerTiempo():
    global tiempo
    global inicio
    global final
    global sumatoria
    global puntosjugador1
    global puntosjugador2
    global multiplicador
    
    final = time.time()
    tiempo = round(final-inicio, 0)
    
    print("Te has tardado " + str(tiempo))
    resultadoUsuario = entry.get()
    print(resultadoUsuario)
    print(sumatoria)
    
    
    if int(resultadoUsuario) == sumatoria * multiplicador:
        if tiempo > 25.0:
            messagebox.showinfo(message="Lo siento, se acabo tu tiempo te has tardado " + str(tiempo) + " segundos.", title="TIEMPO")
        else:
            messagebox.showinfo(message="Felicidades, la respuesta es correcta y te has tardado " + str(tiempo) + " segundos.", title="Felicidades!")
            
            
            if turno == True:
               
                puntosjugador2 = puntosjugador2 + 3
                messagebox.showinfo(message= "el jugador " + nombre2 + " lleva " + str (puntosjugador2) + " puntos\n" + "turno de: " + nombre1 )
                #print("el jugador " + nombre2 + " lleva: " + str (puntosjugador2) + " puntos")
                Labelpunteos1.config(text= str(puntosjugador2))
                labelturn.config(text= "turno de " + nombre1)
                
            else:
                puntosjugador1 = puntosjugador1 + 3
                messagebox.showinfo(message= "el jugador " + nombre1 + " lleva " + str (puntosjugador1) + " puntos\n" + "turno de: " + nombre2)
                Labelpunteos2.config(text= str(puntosjugador1))
                labelturn.config(text="turno de " + nombre2)
              
            
    else:
      
        if turno == True:
            messagebox.showinfo(message="Lo siento, la respuesta es incorrecta y te has tardado " + str(tiempo) + " segundos.\n Lleva " + str (puntosjugador2) + "\nLe corresponde turno a: " + str(nombre1), title="TIEMPO")
             
        else:
            messagebox.showinfo(message="Lo siento, la respuesta es incorrecta y te has tardado " + str(tiempo) + " segundos.\n" + "lleva "+ str (puntosjugador1) + "\nLe corresponde turno a: "+ str(nombre2), title="TIEMPO")
       
    
    generarMatriz()
    global Tpermitidos
    print("FALTAN ---- " + str(Tpermitidos))
    
    
#boton de seleccion
print(matriz)


btnLista= []
ejemplo = [["x", "x"]]
def generarMatriz():
    global turno
    
    if turno:
        print("turno del jugador 1 ")
        turno=False
           
    else:
        print("turno del jugador 2 ")
        turno=True
        
    posicionX =.2
    posicionY = .2
    for i in range(filas):
        btnLista.append([])
        for j in range(columnas):
   
            if [i, j] in anulados:
                print('Existe en la matriz')
                
                btnLista[i].append(Button(root, text = "x", command=partial(nuevo_click, i,j) ))
                btnLista[i][j].config(bg = "#FFFFFF", relief = "solid", fg = "black")
                
                btnLista[i][j].place(relx = 0.1 *j, rely = 0.1 + 0.1*i, relwidth = 0.1, relheight = 0.1)
                #messagebox.showinfo(message="No puedes seleccionar este numero", title="Incorrecto")
            else:
                btnLista[i].append(Button(root, text = matriz[i][j], command=partial(nuevo_click, i,j) ))
                btnLista[i][j].config(bg = "#FFFFFF", relief = "solid", fg = "white")
                btnLista[i][j].place(relx = 0.1 *j, rely = 0.1 + 0.1*i, relwidth = 0.1, relheight = 0.1)
            
            posicionX+=0.1
        posicionY+=0.1
        posicionX = .2



titulo = ttk.Label(root, text="Bienvenido a Matriz Aritmetrica", font="Arial")
titulo.place(x =10, y=10)
titulo1 = ttk.Label(root, text="Escriba su resultado")
titulo1.place(x =320, y=30)
    

entry = ttk.Entry(root)

# Posicionarla en la ventana.
entry.place(x=370+70, y=30) 


boton = ttk.Button(root, text="Comprobar", command=detenerTiempo)
boton.place(x=370+70+150, y=30)


root.mainloop()
