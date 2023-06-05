#Esta es una nueva actualizacion
from tkinter import*
from tkinter import ttk
from functools import partial
import random
from tkinter import messagebox
import time



#Inicio de otra ventana de inicio


root2 = Tk()
root2.title('TKINTER GAME REGISTRO')
root2.geometry("700x500")
root2.config(bg="#FFFFFF")

#texto en pantalla
titulo = ttk.Label(root2, text="Bienvenido a Matriz Aritmetrica", font="Arial")
titulo.place(x =220, y=40)

#texto en pantalla jugador 1
titulo1 = ttk.Label(root2,text="Jugador 1: ")
titulo1.place(x=220,y=100)
titulo2= ttk.Entry(root2, text="Jugador 1: ")
titulo2.place(x=220,y=120)


#texto en pantalla jugador 2
titulo3 = ttk.Label(root2, text="Jugador 2: ")
titulo3.place(x=220,y=190)
inputNombre2 =ttk.Entry(root2, text="Jugador 2: ")
inputNombre2.place(x=220, y=210)


def ingresarcredenciales():
    global nombre1
    nombre1 = titulo2.get()
    nombre1=ttk.Label( text=str(nombre1))
    nombre1.place(x=330, y=260)
   
    global nombre2
    nombre2 = inputNombre2.get()
    nombre2=ttk.Label( text=nombre2)
    nombre2.place(x=330, y=290)
    
    
boton = ttk.Button(text="ingrese: ", command=ingresarcredenciales)
boton.place(x=150+10+150,y=400)
ingrese=ttk.Entry()
    
    

inicio = 0
final = 0
detener = False

#Vaoy a probar algo nuevo
#Crear una ventana en tkinter
root = Tk()
root.title('TKINTER GAME')
root.geometry("800x700")
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

#Se hara una funcion el cual se ejecutara cuando el usuario le de click a un boton de la matriz.
def nuevo_click(i, j):
    global sumatoria #Utilizo la variable sumatoria en modalidad global.
    sumatoria = 0 #Reinicio la variable en 0
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
        
        
        
        #respuesta = input('Ingresa la respuesta \n')
       
        
    
    
    
    


    
    
     
    
    #btnLista[i-1][j].config(bg = "#FFFFFF", relief = "solid", fg = "blue")
    
    
        
def detenerTiempo():
    global tiempo
    global inicio
    global final
    global sumatoria
    final = time.time()
    tiempo = round(final-inicio, 0)
    
    print("Te has tardado " + str(tiempo))
    resultadoUsuario = entry.get()
    print(resultadoUsuario)
    print(sumatoria)
    if int(resultadoUsuario) == sumatoria:
        if tiempo > 25.0:
            messagebox.showinfo(message="Lo siento, se acabo tu tiempo te has tardado " + str(tiempo) + " segundos.", title="TIEMPO")
        else:
            messagebox.showinfo(message="Felicidades, la respuesta es correcta y te has tardado " + str(tiempo) + " segundos.", title="Felicidades!")
            
    else:
        messagebox.showinfo(message="Lo siento, el numero correcto era " + str(sumatoria), title="Incorrecto")
    
    generarMatriz()

#Crear un boton que diga, seleccion



    
    
    
    
    
    


print(matriz)


btnLista= []
ejemplo = [["x", "x"]]
def generarMatriz():
    posicionX =.2
    posicionY = .2
    for i in range(filas):
        btnLista.append([])
        for j in range(columnas):
            #Crear un label en la matriz
            #label2 = Label(root, text=matriz[i][j], font=("Arial", 20, "bold"), bg="#070D0F", fg="white")
            #label2.grid(row = i, column = j)
            #label2.place(relx=posicionX, rely=posicionY)
            #label2.config(bg = "#070D0F")
            
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

generarMatriz()

titulo = ttk.Label(root, text="Bienvenido a Matriz Aritmetrica", font="Arial")
titulo.place(x =10, y=30)
titulo1 = ttk.Label(root, text="Escriba su resultado")
titulo1.place(x =320, y=30)
    
# Crear caja de texto.
entry = ttk.Entry(root)
# Posicionarla en la ventana.
entry.place(x=370+70, y=30) 

#boton = ttk.Button(text="Creacion", command=generarMatriz)
#boton.place(x=5, y=5)

boton = ttk.Button(root, text="Comprobar", command=detenerTiempo)
boton.place(x=370+70+150, y=30)


root.mainloop()