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


frame_imagem = LabelFrame(window, width=380, height=400, text="Cyclone IV")
frame_selecao = LabelFrame(window, width=350, height=400, text="Configurações do Sistema")
frame_rodape = Frame(window, width=350, height=50)
frame_rodape.pack(fill=X, side=BOTTOM)

padding_x = 30
ipad_x = 15

Button(frame_rodape, text="Salvar Configuração").grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
Button(frame_rodape, text="Carregar Configuração").grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
Button(frame_rodape, text="Gerar", command = gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
Button(frame_rodape, text="Sair", command = get_prefixo).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)

image = ImageTk.PhotoImage(Image.open("assets/img.png"))
img = Label(frame_imagem, image = image)
img.place(relx=0.5, rely=0.5, anchor=CENTER)
frame_imagem.pack(fill=X, side=LEFT)

frame_selecao.pack(fill=X, side=LEFT)
Label(frame_selecao, text="Nome do Projeto:").place(anchor='nw')
Entry(frame_selecao, width=40, textvariable=nome_do_projeto).place(rely=0.06, anchor='nw')

Checkbutton(frame_selecao, text='CLOCK', onvalue=True, offvalue=False).place(relx=0.05, rely=0.2)
Checkbutton(frame_selecao, text='LED X 10', onvalue=True, offvalue=False).place(relx=0.05, rely=0.3)
Checkbutton(frame_selecao, text='Botão x 2', onvalue=True, offvalue=False).place(relx=0.05, rely=0.4)
Checkbutton(frame_selecao, text='VGA', onvalue=True, offvalue=False).place(relx=0.05, rely=0.5)
Checkbutton(frame_selecao, text='Arduino Header', onvalue=True, offvalue=False).place(relx=0.05, rely=0.6)


Checkbutton(frame_selecao, text='7-Segmentos X 6', onvalue=True, offvalue=False).place(relx=0.6, rely=0.2)
Checkbutton(frame_selecao, text='Switch X 10', onvalue=True, offvalue=False).place(relx=0.6, rely=0.3)
Checkbutton(frame_selecao, text='Acelerometro', onvalue=True, offvalue=False).place(relx=0.6, rely=0.4)
Checkbutton(frame_selecao, text='SDRAM, 64 MB', onvalue=True, offvalue=False).place(relx=0.6, rely=0.5)

Label(frame_selecao, text="Cabeçalho 2x20 GPIO").place(anchor ='sw', rely=0.8)
Label(frame_selecao, text="Prefixo:").place(anchor='sw', rely=0.95)
Entry(frame_selecao, width=20, textvariable = prefixo).place(anchor='sw', rely=0.95, relx=0.15)


window.resizable(False, False)
window.mainloop()
