# Importar tkinter
import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz gráfica con tkinter")
ventana.geometry("400x400")
ventana.iconbitmap("f1_logo.ico") # Cambiar el ícono de la ventana

# Crear variables para almacenar los datos del usuario
nombre = tk.StringVar()
curp = tk.StringVar()
rfc = tk.StringVar()
sexo = tk.StringVar()
boletos = [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]

# Crear función para validar y mostrar los datos del usuario
def validar():
    # Obtener los valores de las variables
    n = nombre.get()
    c = curp.get()
    r = rfc.get()
    s = sexo.get()
    b = [boletos[0].get(), boletos[1].get(), boletos[2].get()]
    
    # Validar que los campos no estén vacíos
    if n and c and r and s:
        # Mostrar los datos del usuario en una etiqueta
        resultado.config(text=f"Nombre: {n}\nCURP: {c}\nRFC: {r}\nSexo: {s}\nBoletos: {b}")
    else:
        # Mostrar un mensaje de error en una etiqueta
        resultado.config(text="Debes llenar todos los campos")

# Crear etiquetas para solicitar los datos del usuario
etiqueta_nombre = tk.Label(ventana, text="Nombre completo:")
etiqueta_curp = tk.Label(ventana, text="CURP:")
etiqueta_rfc = tk.Label(ventana, text="RFC:")
etiqueta_sexo = tk.Label(ventana, text="Sexo:")
etiqueta_boletos = tk.Label(ventana, text="Boletos:")

# Crear campos de texto para ingresar los datos del usuario
entrada_nombre = tk.Entry(ventana, textvariable=nombre)
entrada_curp = tk.Entry(ventana, textvariable=curp)
entrada_rfc = tk.Entry(ventana, textvariable=rfc)

# Crear botones de radio para seleccionar el sexo del usuario
radio_femenino = tk.Radiobutton(ventana, text="Femenino", variable=sexo, value="Femenino")
radio_masculino = tk.Radiobutton(ventana, text="Masculino", variable=sexo, value="Masculino")

# Crear casillas de verificación para seleccionar los boletos del usuario
check_boleto1 = tk.Checkbutton(ventana, text="Boleto 1", variable=boletos[0])
check_boleto2 = tk.Checkbutton(ventana, text="Boleto 2", variable=boletos[1])
check_boleto3 = tk.Checkbutton(ventana, text="Boleto 3", variable=boletos[2])

# Crear un botón para validar y mostrar los datos del usuario
boton_validar = tk.Button(ventana, text="Validar", command=validar)

# Crear una etiqueta para mostrar el resultado o el error
resultado = tk.Label(ventana)

# Crear una imagen y colocarla en la ventana
imagen = tk.PhotoImage(file="imagen.png")
etiqueta_imagen = tk.Label(ventana, image=imagen)

# Colocar los widgets en la ventana usando grid()
etiqueta_nombre.grid(row=0, column=0)
entrada_nombre.grid(row=0, column=1)
etiqueta_curp.grid(row=1, column=0)
entrada_curp.grid(row=1, column=1)
etiqueta_rfc.grid(row=2, column=0)
entrada_rfc.grid(row=2, column=1)
etiqueta_sexo.grid(row=3, column=0)
radio_femenino.grid(row=3, column=1)
radio_masculino.grid(row=4, column=1)
etiqueta_boletos.grid(row=5, column=0)
check_boleto1.grid(row=5, column=1)
check_boleto2.grid(row=6, column=1)
check_boleto3.grid(row=7, column=1)
boton_validar.grid(row=8, column=0, columnspan=2)
resultado.grid(row=9, column=0, columnspan=2)
etiqueta_imagen.grid(row=10, column=0, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()