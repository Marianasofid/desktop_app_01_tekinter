from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera Noruega")

ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="red")

#Frame 1
frame_1 = Frame(ventana_principal)
frame_1.config(bg="white", width=900, height=130)
frame_1.place(x=0, y=200)

#Frame 2
frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=130, height=900)
frame_2.place(x=100, y=0)

#Frame 3
frame_3 = Frame(ventana_principal)
frame_3.config(bg="blue", width=900, height=50)
frame_3.place(x=0, y=240)

#Frame 4
frame_4 = Frame(ventana_principal)
frame_4.config(bg="blue", width=50, height=900)
frame_4.place(x=140, y=0)


#Final
ventana_principal.mainloop()

