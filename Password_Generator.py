# Generador de Contraseñas aleatorias / Random Password Generator

# Importando las librerias necesarias / Importing the necessary libraries
from tkinter import *
from tkinter import messagebox
import random as rm
import os

# Variables Globales / Global Variables
lower_case = "abcdefghijklmnopqrstuvwxyz"
capital_letter = lower_case.upper()
symbols = "@#%$"
numbers = "0123456789"

# Funcion que genera la contraseña / Function that generates the password
def password(num):
    
    # Borra la contraseña anterior / Delete the previous password
    show_password.delete(0, END)
    password = ""

    # Verifica que el numero de caracteres sea mayor a 12 si no lo es muestra una advertencia pero aun asi genera la contraseña
    # Verify that the number of characters is greater than 12 if it is not, it shows a warning but still generates the password
    if num < 12:
        
        messagebox.showinfo(
            "Alvertencia",
            "Es Recomendable Poner 12 Caracteres como Minimo para una Contraseña Segura",
        )

    # Genera la contraseña aleatoria / Generates the random password
    for i in range(num):
        
        num_ran1 = rm.randint(1, 4)

        if num_ran1 == 1:
            password = password + lower_case[rm.randint(0, 25)]

        elif num_ran1 == 2:
            password = password + capital_letter[rm.randint(0, 25)]

        elif num_ran1 == 3:
            password = password + symbols[rm.randint(0, 3)]

        elif num_ran1 == 4:
            password = password + numbers[rm.randint(0, 9)]

    # Guarda la contraseña en un archivo de texto si el usuario lo desea / Save the password in a text file if the user wishes
    if enable_save.get():
        
        with open(archive, "a", encoding="UTF-8") as archive_write:
            archive_write.write(f"Contraseña : {password}\n")

    # Muestra la contraseña en el Entry / Show the password in the Entry
    show_password.insert(0, password)

# Funcion que convierte el numero de caracteres a entero / Function that converts the number of characters to integer
def convert_integer():
    
    # Verifica que el usuario ingresa un numero / Verify that the user enters a number
    if entry_characters.get().isdigit():
        
        # Convierte el numero de caracteres a entero / Converts the number of characters to integer
        number = int(entry_characters.get())
        password(number)

    # Verifica que el usuario no ingrese nada / Verify that the user does not enter anything
    elif entry_characters.get() == "":
        
        messagebox.showinfo("Alvertencia", "No Ingreso Ningun Numero")
        
    # Verifica que el usuario ingrese un numero / Verify that the user enters a number
    else:
        messagebox.showinfo("Alvertencia", "Solo se pueden Ingresar Numeros")

# Funcion que actualiza el ancho del Entry / Function that updates the width of the Entry
def update_width(*args):
    
    length = len(sv.get())
    new_length = length + 10
    show_password.config(width=new_length)

# Funcion para el guardado de las contraseñas en un archivo de texto / Function for saving passwords in a text file
def enable():
    
    # Alvertencia | Warning
    messagebox.showinfo(
        "Alvertencia",
        "Verifique que el Nombre del Archivo no se repita con otro Archivo de Texto por que se sobreescribira",
    )

    global archive
    
    # Obtiene el directorio actual / Get the current directory
    current_directory = os.getcwd()
    
    verify = name_txt.get()

    # Verifica que el usuario ingrese un nombre para el archivo de texto / Verify that the user enters a name for the text file
    if verify == "":
        
        messagebox.showinfo("Alvertencia", "Ingrese un Nombre para el Archivo de Texto")
        enable_save.set(0)

    elif enable_save.get():
        
        archive = os.path.join(current_directory, name_txt.get() + ".txt")
        open(archive, "w", encoding="UTF-8")


# Interfaz Grafica / Graphic Interface
window = Tk()
enable_save = IntVar()
sv = StringVar()
sv.trace("w", update_width)

# Nombre de la ventana / Name of the window
window.title("Password Generator")
window.configure(background="#3D405B")

# Titulo del programa / Title of the program
Label_0 = Label(
    window,
    text="Programa para Generar Contraselas Aleatorias",
    background="#3D405B",
    font=("Arial", 16),
    fg="#81B29A",
)
Label_0.grid(row=0, column=0, padx=2, pady=2)

# Espacio en blanco / Blank space
Label_empty = Label(window, text=" ", background="#3D405B")
Label_empty.grid(row=1, column=0, padx=2, pady=2)

# Ingresar el numero de caracteres / Enter the number of characters
Label_1 = Label(
    window,
    text="Ingrese el Numero de Caracteres",
    background="#3D405B",
    font=("Arial, 14"),
    fg="#F4F1DE",
)
Label_1.grid(row=2, column=0, padx=2, pady=2)

# Entry para ingresar el numero de caracteres / Entry to enter the number of characters
entry_characters = Entry(
    window, background="#F4F1DE", bd=4, relief="ridge", font=("Arial, 14"), fg="#3D405B"
)
entry_characters.grid(row=3, column=0, padx=1, pady=2)

# Espacio en blanco / Blank space
Label_empty_1 = Label(window, text=" ", background="#3D405B")
Label_empty_1.grid(row=4, column=0, padx=2, pady=2)

# Titulo para guardar las contraseñas en un archivo de texto / Title to save passwords in a text file
Label_2 = Label(
    window,
    text="Guardar la Contraseña en un Archivo .txt",
    background="#3D405B",
    font=("Arial", 14),
    fg="#F4F1DE",
)
Label_2.grid(row=5, column=0, padx=5, pady=5)

# Guardar las contraseñas en un archivo de texto / Save passwords in a text file
checkbutton_save_passwords = Checkbutton(
    window,
    font=("Arial", 10),
    fg="#F4F1DE",
    background="#3D405B",
    text="Guardar las Contraseñas",
    variable=enable_save,
    command=lambda: enable(),
)
checkbutton_save_passwords.grid(row=7, column=0, padx=2, pady=2)

# nombre del archivo de texto / name of the text file
Label_3 = Label(
    window,
    text="Nombre del Archivo de Texto",
    background="#3D405B",
    font=("Arial", 13),
    fg="#F4F1DE",
)
Label_3.grid(row=8, column=0, padx=5, pady=5)

# Entry para ingresar el nombre del archivo de texto / Entry to enter the name of the text file
name_txt = Entry(
    window, background="#F4F1DE", bd=4, relief="ridge", font=("Arial, 14"), fg="#3D405B"
)
name_txt.grid(row=9, column=0, padx=1, pady=2)

# Espacio en blanco / Blank space
Label_empty_2 = Label(window, text=" ", background="#3D405B")
Label_empty_2.grid(row=10, column=0, padx=2, pady=2)

# Boton para generar la contraseña / Button to generate the password
button_generate_password = Button(
    window,
    text="Generar Contraseña",
    width=19,
    height=1,
    background="#E07A5F",
    font=("Arial", 13),
    fg="#F4F1DE",
    command=lambda: convert_integer(),
)
button_generate_password.grid(row=11, column=0, padx=2, pady=2)

# Mostrar la contraseña generada / Show the generated password
Label_4 = Label(
    window,
    text="Contraseña Generada",
    background="#3D405B",
    font=("Arial", 14),
    fg="#F4F1DE",
)
Label_4.grid(row=12, column=0, padx=2, pady=2)

# Entry para mostrar la contraseña generada / Entry to show the generated password
show_password = Entry(
    window, background="#F4F1DE", font=("Arial", 14), fg="#3D405B", textvariable=sv
)
show_password.config(justify="center")
show_password.grid(row=13, column=0, padx=1, pady=2)

# Espacio en blanco / Blank space
Label_empty_2 = Label(window, text=" ", background="#3D405B")
Label_empty_2.grid(row=14, column=0, padx=2, pady=2)

# mainloop de la ventana / mainloop of the window
window.mainloop()
