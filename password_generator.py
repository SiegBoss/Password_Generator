#Generador de Contraseñas aleatorias / Random Password Generator

#importando las librerias necesarias / Importing the necessary libraries
from tkinter import *
from tkinter import messagebox
import random as rm
import os

global verify2
verify2 = ""

#Caracteres que se usaran para generar la contraseña / Characters that will be used to generate the password
lower_case = "abcdefghijklmnopqrstuvwxyz"
capital_letter = lower_case.upper()
symbols = "@#%$"
numbers = "0123456789"

#Funcion que genera la contraseña / Function that generates the password
def password(num):
    
    #Borra la contraseña anterior / Delete the previous password
    show_password.delete(0, END)
    password = ""  
    
    #Verifica que el numero de caracteres sea mayor a 12 y muestra una alerta / Verify that the number of characters is greater than 12 and display an alert
    if num < 12:
        messagebox.showinfo("Alvertencia" , "Es Recomendable Poner 12 Caracteres como Minimo para una Contraseña Segura")
    
    #Genera la contraseña aleatoria / Generates the random password
    for i in range(num):
        
        num_ran1 = rm.randint(1,4)
        
        if num_ran1 == 1:

            num_ran2 = rm.randint(0,25)
            password = password + lower_case[num_ran2]

        elif num_ran1 == 2:

            num_ran2  = rm.randint(0,25)
            password = password + capital_letter[num_ran2]

        elif num_ran1 == 3:

            num_ran3 = rm.randint(0,3)
            password= password + symbols[num_ran3]

        elif num_ran1 == 4:

            num_ran4 = rm.randint(0,9)
            password = password + numbers[num_ran4]
        
    #Guarda la contraseña en un archivo de texto si el usuario lo desea / Save the password in a text file if the user wishes
    if disable_save.get():
        with open(archive, "a", encoding="UTF-8") as archive_write:
            archive_write.write(f"Contraseña : {password}\n")

    #Muestra la contraseña en la interfaz / Show the password in the interface
    show_password.insert(0, password)
    
#Funcion que convierte el numero de caracteres a entero / Function that converts the number of characters to integer
def convert_integer():
    
    verify = entry_characters.get()
    
    #Verifica que el usuario ingresa un numero / Verify that the user enters a number
    if verify.isdigit():
        number = int(entry_characters.get())
        password(number)
        
    elif verify == "":
        messagebox.showinfo("Alvertencia" , "No Ingreso Ningun Numero")
    else:
        messagebox.showinfo("Alvertencia" , "Solo se pueden Ingresar Numeros")

#Funcion que actualiza el ancho del Entry / Function that updates the width of the Entry
def update_width(*args):
    show_password.config(width=len(sv.get()) + 10)

#Funcion que desactiva la opcion de guardar las contraseñas en un archivo de texto / Function that disables the option to save passwords in a text file
def disable():
    global verify2
    
    current_directory = os.getcwd()
    verify = name_txt.get()
    
    if verify == "":
        messagebox.showinfo("Alvertencia" , "Ingrese un Nombre para el Archivo de Texto")
        disable_save.set(0)
        
    elif verify == verify2 and disable_save.get():
        messagebox.showinfo("Alvertencia" ,"Se sobreescribira el Archivo de Texto Borrando las Contraseñas Anteriores")
        disable_save.set(0)
           
    elif disable_save.get():
        global archive
        archive = os.path.join(current_directory, name_txt.get() + ".txt")
        open(archive, "w", encoding="UTF-8")
    
    verify2 = verify

window = Tk()
disable_save = IntVar()
sv = StringVar()
sv.trace("w", update_width)

#nombre de la ventana / Name of the window
window.title("Password Generator")

#Titulo del programa / Title of the program
Label_0 = Label(window, text="Programa para Generar Contraselas Aleatorias", font=("Arial", 14))
Label_0.grid(row=0, column=0, padx=2, pady=2)

Label_empty= Label(window, text=" ")
Label_empty.grid(row=1, column=0, padx=2, pady=2)

#Ingresar el numero de caracteres / Enter the number of characters
Label_1 = Label(window, text="Ingrese el Numero de Caracteres", font=("Arial", 13))
Label_1.grid(row=2, column=0, padx=2, pady=2)
entry_characters = Entry(window, font=("Arial", 14))
entry_characters.grid(row=3, column=0, padx=1, pady=2) 

Label_empty_1= Label(window, text=" ")
Label_empty_1.grid(row=4, column=0, padx=2, pady=2)

#Titulo para guardar las contraseñas en un archivo de texto / Title to save passwords in a text file
Label_2 = Label(window, text="Guardar la Contraseña en un Archivo .txt", font=("Arial", 14))
Label_2.grid(row=5, column=0, padx=5, pady=5)

#Guardar las contraseñas en un archivo de texto / Save passwords in a text file
checkbutton_save_passwords = Checkbutton(window, font=("Arial", 10), text="Guardar las Contraseñas",  variable = disable_save, command = disable)
checkbutton_save_passwords.grid(row=7, column=0, padx=2, pady=2)

#nombre del archivo de texto / name of the text file
Label_3 = Label(window, text="Nombre del Archivo de Texto", font=("Arial", 13))
Label_3.grid(row=8, column=0, padx=5, pady=5)
name_txt = Entry(window, font=("Arial", 14))
name_txt.grid(row=9, column=0, padx=1, pady=2)

Label_empty_2= Label(window, text=" ")
Label_empty_2.grid(row=10, column=0, padx=2, pady=2)

#Boton para generar la contraseña / Button to generate the password
button_generate_password = Button(window, text="Generar Contraseña", width=19, height=1, font=("Arial", 13), command = lambda:convert_integer())
button_generate_password.grid(row=11, column=0, padx=2, pady=2)

#Mostrar la contraseña generada / Show the generated password
Label_4 = Label(window, text="Contraseña Generada", font=("Arial", 14))
Label_4.grid(row=12, column=0, padx=2, pady=2)
show_password = Entry(window, font=("Arial", 14), textvariable = sv)
show_password.config(justify="center")
show_password.grid(row=13, column=0, padx=1, pady=2)

Label_empty_2= Label(window, text=" ")
Label_empty_2.grid(row=14, column=0, padx=2, pady=2)

window.mainloop()