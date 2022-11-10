from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime



window = Tk()
window.title("Gerador de Código")

window.geometry("730x450")
window.configure(bg="#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()
check_clock = BooleanVar()

def get_prefixo():
    print(prefixo.get())


def get_nome_do_projeto():
    return nome_do_projeto.get().upper()

def gerar_arquivo_qpf():
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.qpf'.format(projeto)
    data = datetime.now()

    qpf = open(nome_arquivo, 'w')
    qpf.write(data.strftime('DATE = \"%H:%M:%S %B %d, %Y\"\n'))
    qpf.write('QUARTUS_VERSION = \"16.0.0\"\n')
    qpf.write('\n')
    qpf.write('# Revisions\n')
    qpf.write('\n')
    qpf.write('PROJECT_REVISION = \"{}\"\n'.format(get_nome_do_projeto()))

    qpf.close()


def gerar_arquivo_sdc():
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.sdc'.format(projeto)

    if check_clock.get() == True:
        f = open('auxiliar/com_clock.sdc', 'r')
        buffer = f.read()
        f.close()
    else:
        f = open('auxiliar/sem_clock.sdc', 'r')
        buffer = f.read()
        f.close()

    sdc = open(nome_arquivo, 'w')
    sdc.write(buffer)
    sdc.close()


def gerar_codigo():
    #gerar_arquivo_qpf()
    gerar_arquivo_sdc()


def gerar_botoes_rodape(frame, padding_x=40, ipad_x=10):
    Button(frame, text="Salvar Configuração").grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Carregar Configuração").grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Gerar", command=gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Sair", command=get_prefixo).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)


def gerar_rodape(largura, altura, background_color):
    frame_rodape = Frame(window, width=largura, height=altura, bg=background_color)
    frame_rodape.pack(fill=X, side=BOTTOM)
    gerar_botoes_rodape(frame_rodape)


frame_selecao = LabelFrame(window, width=350, height=400, text="Configurações do Sistema")

gerar_rodape(350, 50, "#f0f0f0")

frame_imagem = LabelFrame(window, width=380, height=400, text="Cyclone IV")
image = ImageTk.PhotoImage(Image.open("assets/img.png"))
Label(frame_imagem, image=image).place(relx=0.5, rely=0.5, anchor=CENTER)
frame_imagem.pack(fill=X, side=LEFT)

frame_selecao.pack(fill=X, side=LEFT)
Label(frame_selecao, text="Nome do Projeto:").place(anchor='nw')
Entry(frame_selecao, width=40, textvariable=nome_do_projeto).place(rely=0.06, anchor='nw')

Checkbutton(frame_selecao, text='CLOCK', onvalue=True, offvalue=False, variable=check_clock).place(relx=0.05, rely=0.2)
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
Entry(frame_selecao, width=20, textvariable=prefixo).place(anchor='sw', rely=0.95, relx=0.15)


window.resizable(False, False)
window.mainloop()
