from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
from datetime import datetime



window = Tk()
window.title("Gerador de Código")

window.geometry("730x480")
window.configure(bg="#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()

check_clock = BooleanVar()
check_SDRAM = BooleanVar()
check_segmentos = BooleanVar()
check_switch = BooleanVar()
check_LED = BooleanVar()
check_button = BooleanVar()
check_VGA = BooleanVar()
check_GPIO = BooleanVar()
check_LCD = BooleanVar()



def get_diretorio_arquivos():
    diretorio = askdirectory()
    print(diretorio)
    return diretorio


def get_prefixo():
    print(prefixo.get())


def get_nome_do_projeto():
    return nome_do_projeto.get().upper()

def gerar_arquivo_qpf(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.qpf'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo
    data = datetime.now()

    qpf = open(nome_arquivo, 'w')
    qpf.write(data.strftime('DATE = \"%H:%M:%S %B %d, %Y\"\n'))
    qpf.write('QUARTUS_VERSION = \"16.0.0\"\n')
    qpf.write('\n')
    qpf.write('# Revisions\n')
    qpf.write('\n')
    qpf.write('PROJECT_REVISION = \"{}\"\n'.format(get_nome_do_projeto()))

    qpf.close()


def gerar_arquivo_qsf(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.qsf'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo
    data = datetime.now()

    if check_SDRAM.get() == True:
        with open('auxiliar/SDRAM_qsf.txt', 'r') as f:
            SDRAM_buffer = f.read()

    if check_segmentos.get() == True:
        with open('auxiliar/SEG7_qsf.txt', 'r') as f:
            SEG7_buffer = f.read()

    if check_VGA.get():
        with open('auxiliar/VGA_qsf.txt', 'r') as f:
            VGA_buffer = f.read()

    if check_LCD.get():
        with open('auxiliar/Arduino_qsf.txt', 'r') as f:
            Arduino_buffer = f.read()



    with open(nome_arquivo, 'w') as qsf:
        qsf.write('#============================================================\n'
                  '# Build by Terasic System Builder\n'
                  '#============================================================\n\n')

        qsf.write('set_global_assignment -name FAMILY "MAX 10 FPGA"\n')
        qsf.write('set_global_assignment -name DEVICE 10M50DAF484C7G\n')
        qsf.write('set_global_assignment -name TOP_LEVEL_ENTITY "{}"\n'.format(projeto))
        qsf.write('set_global_assignment -name LAST_QUARTUS_VERSION "16.0.0"\n')
        qsf.write('set_global_assignment -name PROJECT_CREATION_TIME_DATE "{}"\n'.format(data.strftime('%H:%M:%S %B %d,%Y')))
        qsf.write('set_global_assignment -name DEVICE_FILTER_PACKAGE FBGA\n')
        qsf.write('set_global_assignment -name ORIGINAL_QUARTUS_VERSION "16.0.0"\n')
        qsf.write('set_global_assignment -name DEVICE_FILTER_PIN_COUNT 484\n')
        qsf.write('set_global_assignment -name DEVICE_FILTER_SPEED_GRADE 7\n')
        qsf.write('set_global_assignment -name SDC_FILE {}.SDC\n'.format(projeto))

        if check_clock.get():
            qsf.write('\n#============================================================\n'
                      '# CLOCK\n'
                      '#============================================================\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to ADC_CLK_10\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to MAX10_CLK1_50\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to MAX10_CLK2_50\n')
            qsf.write('set_location_assignment PIN_N5 -to ADC_CLK_10\n')
            qsf.write('set_location_assignment PIN_P11 -to MAX10_CLK1_50\n')
            qsf.write('set_location_assignment PIN_N14 -to MAX10_CLK2_50\n')

        if check_SDRAM.get():
            qsf.write(SDRAM_buffer)
            qsf.write('\n')

        if check_segmentos.get():
            qsf.write(SEG7_buffer)
            qsf.write('\n')

        if check_button.get():
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3 V Schmitt Trigger" -to KEY[0]\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3 V Schmitt Trigger" -to KEY[1]\n')
            qsf.write('set_location_assignment PIN_B8 -to KEY[0]\n')
            qsf.write('set_location_assignment PIN_B8 -to KEY[1]\n')

        if check_LED.get():
            qsf.write('\n#============================================================\n'
                      '# LED\n'
                      '#============================================================\n\n')
            for i in range(0, 10):
                qsf.write('set_instance_assignment -name IO_STANDARD "3.3 V Schmitt Trigger" -to KEY[{}]\n'.format(i))

            qsf.write('set_location_assignment PIN_A8 -to LEDR[0]\n')
            qsf.write('set_location_assignment PIN_A9 -to LEDR[1]\n')
            qsf.write('set_location_assignment PIN_A10 -to LEDR[2]\n')
            qsf.write('set_location_assignment PIN_B10 -to LEDR[3]\n')
            qsf.write('set_location_assignment PIN_D13 -to LEDR[4]\n')
            qsf.write('set_location_assignment PIN_C13 -to LEDR[5]\n')
            qsf.write('set_location_assignment PIN_E14 -to LEDR[6]\n')
            qsf.write('set_location_assignment PIN_D14 -to LEDR[7]\n')
            qsf.write('set_location_assignment PIN_A11 -to LEDR[8]\n')
            qsf.write('set_location_assignment PIN_B11 -to LEDR[9]\n')

        if check_switch.get():
            qsf.write('\n#============================================================\n'
                      '# SW\n'
                      '#============================================================\n')

            for i in range(0, 10):
                qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to SW[{}]\n'.format(i))

            qsf.write('set_location_assignment PIN_C10 -to SW[0]\n')
            qsf.write('set_location_assignment PIN_C11 -to SW[1]\n')
            qsf.write('set_location_assignment PIN_D12 -to SW[2]\n')
            qsf.write('set_location_assignment PIN_C12 -to SW[3]\n')
            qsf.write('set_location_assignment PIN_A12 -to SW[4]\n')
            qsf.write('set_location_assignment PIN_B12 -to SW[5]\n')
            qsf.write('set_location_assignment PIN_A13 -to SW[6]\n')
            qsf.write('set_location_assignment PIN_A14 -to SW[7]\n')
            qsf.write('set_location_assignment PIN_B14 -to SW[8]\n')
            qsf.write('set_location_assignment PIN_F15 -to SW[9]\n')
            qsf.write('\n')

        if check_VGA.get():
            qsf.write(VGA_buffer)
            qsf.write('\n')

        if check_GPIO.get():
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_CS_N\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_INT[1]\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_INT[2]\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_SCLK\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_SDI\n')
            qsf.write('set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GSENSOR_SDO\n')
            qsf.write('set_location_assignment PIN_AB16 -to GSENSOR_CS_N\n')
            qsf.write('set_location_assignment PIN_Y14 -to GSENSOR_INT[1]\n')
            qsf.write('set_location_assignment PIN_Y13 -to GSENSOR_INT[2]\n')
            qsf.write('set_location_assignment PIN_AB15 -to GSENSOR_SCLK\n')
            qsf.write('set_location_assignment PIN_V11 -to GSENSOR_SDI\n')
            qsf.write('set_location_assignment PIN_V12 -to GSENSOR_SDO\n')

        if check_LCD.get():
            qsf.write(Arduino_buffer)

        qsf.write('\n#============================================================\n'
              '# End of pin assignments by Terasic System Builder'
              '\n#============================================================\n\n')


def criar_selecao(label, varialvel, coluna, posicao):
    espacamento = 13

    if coluna == 1:
        Checkbutton(frame_selecao, text=label, onvalue=True, offvalue=False, variable=varialvel).place(relx=0.05, rely=posicao/espacamento)
    elif coluna == 2:
        Checkbutton(frame_selecao, text=label, onvalue=True, offvalue=False, variable=varialvel).place(relx=0.6, rely=posicao/espacamento)
    else:
        print('Só há duas colunas')


def gerar_arquivo_v(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.v'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    v = open(nome_arquivo, 'w')
    v.write('module {}(\n'.format(projeto))

    if check_clock.get():
        v.write('\t//////////// CLOCK ////////////\n')
        v.write('\tinput\t\t\t\t\tADC_CLK_10,\n\tinput\t\t\t\t\tMAX10_CLK1_50,\n\tinput\t\t\t\t\tMAX10_CLK2_50\n')
    if check_SDRAM.get():
        v.write('\n\t//////////// SDRAM ////////////\n')
        v.write('\toutput\t\t[12:0]\t\tDRAM_ADDR,\n')
        v.write('\toutput\t\t [1:0]\t\tDRAM_BA,\n')
        v.write('\toutput\t\t      \t\tDRAM_CAS_N,\n')
        v.write('\toutput\t\t      \t\tDRAM_CKE,\n')
        v.write('\toutput\t\t      \t\tDRAM_CLK,\n')
        v.write('\toutput\t\t      \t\tDRAM_CS_N,\n')
        v.write('\tinput\t\t[15:0]\t\tDRAM_DQ,\n')
        v.write('\toutput\t\t      \t\tDRAM_LDQM,\n')
        v.write('\toutput\t\t      \t\tDRAM_RAS_N,\n')
        v.write('\toutput\t\t      \t\tDRAM_UDQM,\n')
        v.write('\toutput\t\t      \t\tDRAM_WE_N,\n')

    if check_segmentos.get():
        v.write('\n\t//////////// SEG7 ////////////\n')
        v.write('\toutput\t\t [7:0]\t\tHEX0,\n')
        v.write('\toutput\t\t [7:0]\t\tHEX1,\n')
        v.write('\toutput\t\t [7:0]\t\tHEX2,\n')
        v.write('\toutput\t\t [7:0]\t\tHEX3,\n')
        v.write('\toutput\t\t [7:0]\t\tHEX4,\n')
        v.write('\toutput\t\t [7:0]\t\tHEX5,\n')

    if check_switch.get():
        v.write('\n\t//////////// KEY ////////////\n')
        v.write('\tinput\t\t [1:0]\t\tinput,\n')

    if check_LED.get():
        v.write('\n\t//////////// LED ////////////\n')
        v.write('\toutput\t\t [9:0]\t\tLEDR,\n')

    if check_VGA.get():
        v.write('\n\t//////////// VGA ////////////\n')
        v.write('\toutput\t\t [3:0]\t\tVGA_B,\n')
        v.write('\toutput\t\t [3:0]\t\tVGA_G,\n')
        v.write('\toutput\t\t      \t\tVGA_HS,\n')
        v.write('\toutput\t\t [3:0]\t\tVGA_R,\n')
        v.write('\toutput\t\t      \t\tVGA_VS,\n')

    if check_GPIO.get():
        v.write('\n\t//////////// Accelerometer ////////////\n')
        v.write('\toutput\t\t      \t\tGSENSOR_CS_N,\n')
        v.write('\tinput\t\t [2:1]\t\tGSENSOR_INT,\n')
        v.write('\toutput\t\t      \t\tGSENSOR_SCLK,\n')
        v.write('\tinout\t\t      \t\tGSENSOR_SDI,\n')
        v.write('\tinout\t\t      \t\tGSENSOR_SDO,\n')

    if check_LCD.get():
        v.write('\n\t//////////// Arduino ////////////\n')
        v.write('\tinout\t\t [15:0]\t\tARDUINO_IO,\n')
        v.write('\tinout\t\t      \t\tARDUINO_RESET_N,\n')



    v.write(');\n')
    v.write('\n')
    v.write('//=======================================================\n//  REG/WIRE declarations\n//=======================================================\n')
    v.write('\n\n\n\n')
    v.write('//=======================================================\n//  Structural coding\n//=======================================================\n')
    v.write('\n\n\n\n')
    v.write('endmodule\n')
    v.close()


def gerar_arquivo_sdc(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo='{}.sdc'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

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
    diretorio = get_diretorio_arquivos()

    gerar_arquivo_qpf(diretorio)
    gerar_arquivo_qsf(diretorio)
    gerar_arquivo_sdc(diretorio)
    gerar_arquivo_v(diretorio)


def gerar_botoes_rodape(frame, padding_x=40, ipad_x=10):
    Button(frame, text="Salvar Configuração", command=get_diretorio_arquivos).grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Carregar Configuração").grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Gerar", command=gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Sair", command=window.destroy).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)


def gerar_rodape(largura, altura, background_color):
    frame_rodape = Frame(window, width=largura, height=altura, bg=background_color)
    frame_rodape.pack(fill=X, side=BOTTOM)
    gerar_botoes_rodape(frame_rodape)


frame_selecao = LabelFrame(window, width=350, height=410, text="Configurações do Sistema")

gerar_rodape(350, 50, "#f0f0f0")

frame_imagem = LabelFrame(window, width=380, height=410, text="Cyclone IV")
image = ImageTk.PhotoImage(Image.open("assets/img.png"))
Label(frame_imagem, image=image).place(relx=0.5, rely=0.5, anchor=CENTER)
frame_imagem.pack(fill=X, side=LEFT)

frame_selecao.pack(fill=X, side=LEFT)
Label(frame_selecao, text="Nome do Projeto:").place(relx=0.05, anchor='nw')
Entry(frame_selecao, width=40, textvariable=nome_do_projeto).place(relx=0.05, rely=0.06, anchor='nw')

criar_selecao('CLOCK', check_clock, 1, 2)
criar_selecao('LED 8X5', check_LED, 1, 3)
criar_selecao('Botão x12', check_button, 1, 4)
criar_selecao('VGA', check_VGA, 1, 5)
criar_selecao('LCD', check_LCD, 1, 6)
criar_selecao('SDRAM 512Mbit', check_SDRAM, 1, 7)
criar_selecao('Conector Micro SD', check_SDRAM, 1, 8)
criar_selecao('Serial RS232', check_SDRAM, 1, 9)
criar_selecao('Sensor de temperatura I²C', check_SDRAM, 1, 10)
criar_selecao('10/100 Ethernet PHY', check_SDRAM, 1, 11)

criar_selecao('7-Segmentos X 2', check_segmentos, 2, 2)
criar_selecao('Chave X4', check_switch, 2, 3)
criar_selecao('Conector 2x GPIO', check_GPIO, 2, 4)
criar_selecao('SDRAM, 64 MB', check_SDRAM, 2, 5)
criar_selecao('SA e SB', check_SDRAM, 2, 6)
criar_selecao('DAC', check_SDRAM, 2, 7)
criar_selecao('ADC', check_SDRAM, 2, 8)
criar_selecao('LED RGB', check_SDRAM, 2, 9)
criar_selecao('FLASH 64Mbit', check_SDRAM, 2, 10)
criar_selecao('PMOD x2', check_SDRAM, 2, 11)



#Label(frame_selecao, text="Conector 2x GPIO").place(anchor ='sw', rely=0.8)
#Label(frame_selecao, text="Prefixo:").place(anchor='sw', rely=0.95)
#Entry(frame_selecao, width=20, textvariable=prefixo).place(anchor='sw', rely=0.95, relx=0.15)


window.resizable(False, False)
window.mainloop()
