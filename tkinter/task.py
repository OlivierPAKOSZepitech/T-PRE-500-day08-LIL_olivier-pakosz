from tkinter import *
from PIL import Image, ImageTk 



fenetre = Tk()
fenetre.config(width= 800, height=600)
label = Label(fenetre, text = "Hello WORLD")
label.pack()

entree = Entry(fenetre, width=50)
entree.pack()

def cliquer_bouton():
    entree_text = entree.get()
    label.config(text= f"Texte saisi: {entree_text.upper()}")

boutoninput = Button(fenetre, text= "Ecrivez quelque chose ici", command= cliquer_bouton)
boutoninput.pack()

#image = Image.open('tkinter/photoPAKOSZ.jpg')
#image = image.resize((800, 800), Image.ADAPTIVE)
#photo = ImageTk.PhotoImage(image)

#canvas = Canvas(fenetre, width=image.size[0], height=image.size[1], background= "red")
#canvas.pack()
#canvas.create_image(0, 0, anchor=NW, image=photo)

canvas2 = Canvas(fenetre, width= 600, height=800, background="white")
ligne1 = canvas2.create_line(400 , 700, 300, 600, fill= "purple", width=5)
ligne2 = canvas2.create_line(200, 700, 300, 600, fill= "orange", width=5 )
ligne3 = canvas2.create_line(300, 600, 300, 200, fill= "green", width=5)
ligne4 = canvas2.create_line(400 , 400     ,300, 300, fill="red", width=5  )
ligne5 = canvas2.create_line(200,   400 , 300, 300, fill="blue", width=5)
tete = canvas2.create_oval(400, 200, 200, 50, fill= "lightgreen")
canvas2.pack()


def mouvement_bras():
    bras = canvas2.coords(ligne2)
    if bras[1] == 700:
        canvas2.move(ligne1, 0, -100)
        canvas2.move(ligne2, 0, -100)
    else: 
        canvas2.move(ligne1, 0, 100)
        canvas2.move(ligne2, 0, 100)

    canvas2.after(500, mouvement_bras)

mouvement_bras()
fenetre.mainloop()
