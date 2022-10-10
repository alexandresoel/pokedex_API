from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#cores
co0 = '#444466' #pretas
co1 = '#feffff' #branco
co2 = '#6f9fbd' #azul
co3 = '#38576b' #valor
co4 = '#403d3d' #letra
co5 = '#ef5350' #vermelha

#criando uma janela
janela = Tk()
janela.title('RotomDex')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


#labelnome

pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

#labeltipo

pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

#labelid

pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

#imagem do poke
imagem_pokemon = Image.open('images/pikachu.png')
imagem_pokemon = imagem_pokemon.resize((238,238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=co1, fg=co0)
pok_imagem.place(x=60, y=50)
##"official-artwork":{"front_default":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png"}

pok_tipo.lift()

#STATUS
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)
pok_hp = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)
pok_atk = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atk.place(x=15, y=360)
pok_def = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_def.place(x=15, y=360)
pok_stk = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_stk.place(x=15, y=360)
pok_sdf = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_sdf.place(x=15, y=360)
pok_spe = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_spe.place(x=15, y=360)

janela.mainloop()

