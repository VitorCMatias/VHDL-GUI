from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime



window = Tk()
window.title("Gerador de Código")

window.geometry("730x450")
window.configure(bg = "#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()

def get_prefixo():
    print(prefixo.get())


def get_nome_do_projeto():
    return nome_do_projeto.get().upper()

def gerar_codigo():
    # f = open("demofile2.qpf", "w")
    # f.write("Now the file has more content!")
    # f.close()

    now = datetime.now()
    print(now.strftime("DATE = \"%H:%M:%S %B %d, %Y\""))
    print("QUARTUS_VERSION = \"16.0.0\"\n")
    print("# Revisions\n")
    print('PROJECT_REVISION = \"{}\"'.format(get_nome_do_projeto()))


img_frame = LabelFrame(window, width=380, height=400, text="Cyclone IV")
subframe2 = LabelFrame(window, width=350, height=400, text="Configurações do Sistema")
subframe3 = Frame(window, width=350, height=50)
subframe3.pack(fill=X, side=BOTTOM)

padding_x = 30
ipad_x = 15

Button(subframe3, text="Salvar Configuração").grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Carregar Configuração").grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Gerar", command = gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
Button(subframe3, text="Sair", command = get_prefixo).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)

image = ImageTk.PhotoImage(Image.open("assets/img.png"))
img = Label(img_frame, image = image)
img.place(relx=0.5, rely=0.5, anchor=CENTER)
img_frame.pack(fill=X, side=LEFT)

subframe2.pack(fill=X, side=LEFT)
Label(subframe2, text="Nome do Projeto:").place(anchor='nw')
Entry(subframe2, width=40, textvariable=nome_do_projeto).place(rely=0.06, anchor='nw')

Checkbutton(subframe2, text='CLOCK', onvalue=True, offvalue=False).place(relx=0.05, rely=0.2)
Checkbutton(subframe2, text='LED X 10', onvalue=True, offvalue=False).place(relx=0.05, rely=0.3)
Checkbutton(subframe2, text='Botão x 2', onvalue=True, offvalue=False).place(relx=0.05, rely=0.4)
Checkbutton(subframe2, text='VGA', onvalue=True, offvalue=False).place(relx=0.05, rely=0.5)
Checkbutton(subframe2, text='Arduino Header', onvalue=True, offvalue=False).place(relx=0.05, rely=0.6)


Checkbutton(subframe2, text='7-Segmentos X 6', onvalue=True, offvalue=False).place(relx=0.6, rely=0.2)
Checkbutton(subframe2, text='Switch X 10', onvalue=True, offvalue=False).place(relx=0.6, rely=0.3)
Checkbutton(subframe2, text='Acelerometro', onvalue=True, offvalue=False).place(relx=0.6, rely=0.4)
Checkbutton(subframe2, text='SDRAM, 64 MB', onvalue=True, offvalue=False).place(relx=0.6, rely=0.5)

Label(subframe2, text="Cabeçalho 2x20 GPIO").place(anchor ='sw',rely=0.8)
Label(subframe2, text="Prefixo:").place(anchor='sw', rely=0.95)
Entry(subframe2, width=20, textvariable = prefixo).place(anchor='sw', rely=0.95, relx=0.15)


window.resizable(False, False)
window.mainloop()
