from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from datetime import datetime
import json
import arquivo

window = Tk()
window.title("Gerador de Código")

window.geometry("730x480")
window.configure(bg="#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()

check_clock = BooleanVar()
check_SDRAM_64 = BooleanVar()
check_segmentos = BooleanVar()
check_chave = BooleanVar()
check_LED = BooleanVar()
check_button = BooleanVar()
check_VGA = BooleanVar()
check_GPIO = BooleanVar()
check_LCD = BooleanVar()
check_Ethernet = BooleanVar()
check_I2C = BooleanVar()
check_RS232 = BooleanVar()
check_micro_SD = BooleanVar()
check_SDRAM_512 = BooleanVar()
check_PMOD = BooleanVar()
check_flash_64 = BooleanVar()
check_LED_RGB = BooleanVar()
check_ADC = BooleanVar()
check_DAC = BooleanVar()
check_SA_SB = BooleanVar()
check_ext_clock = BooleanVar()

def get_diretorio_arquivos():
    diretorio = askdirectory()
    print(diretorio)
    return diretorio


def get_prefixo():
    print(prefixo.get())


def get_arquivo(tipo):
    tipo_do_arquivo = (('text files', tipo), ('All files', '*.*'))
    nome_do_arquivo = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=tipo_do_arquivo)

    return nome_do_arquivo


def gerar_caixa_de_dialogo(titulo, mensagem):
    showinfo(title=titulo, message=mensagem)


def get_nome_do_projeto():
    return nome_do_projeto.get().upper()


def gerar_arquivo_qpf(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.qpf'.format(projeto)
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
    nome_arquivo = '{}.qsf'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo
    data = datetime.now()

    if check_clock.get():
        f = open('auxiliar/qsf/CLOCK.aux', 'r')
        clock_buffer = f.read()
        f.close()

    if check_ext_clock.get():
        f = open('auxiliar/qsf/EXT_CLOCK.aux', 'r')
        ext_clock_buffer = f.read()
        f.close()

    if check_chave.get():
        f = open('auxiliar/qsf/SW.aux', 'r')
        chave_buffer = f.read()
        f.close()

    if check_button.get():  #KEY
        f = open('auxiliar/qsf/KEY.aux', 'r')
        button_buffer = f.read()
        f.close()

    if check_segmentos.get():
        f = open('auxiliar/qsf/DISPLAY.aux', 'r')
        segmentos_buffer = f.read()
        f.close()

    if check_LED.get():
        f = open('auxiliar/qsf/LED_MX.aux', 'r')
        led_buffer = f.read()
        f.close()

    if check_LED_RGB.get():
        f = open('auxiliar/qsf/LED_RGB.aux', 'r')
        led_rgb_buffer = f.read()
        f.close()

    if check_I2C.get():
        f = open('auxiliar/qsf/TEMP_SENS.aux', 'r')
        i2c_buffer = f.read()
        f.close()

    if check_LCD.get():
        f = open('auxiliar/qsf/LCD.aux', 'r')
        lcd_buffer = f.read()
        f.close()

    if check_VGA.get():
        f = open('auxiliar/qsf/VGA.aux', 'r')
        vga_buffer = f.read()
        f.close()
    # if check_UART.get():
    #     pass

    # if check_USB.get():
    #     pass

    if check_ADC.get():
        f = open('auxiliar/qsf/ADC.aux', 'r')
        adc_buffer = f.read()
        f.close()

    if check_DAC.get():
        f = open('auxiliar/qsf/DAC.aux', 'r')
        dac_buffer = f.read()
        f.close()

    if check_micro_SD.get():
        f = open('auxiliar/qsf/SD_CARD.aux', 'r')
        micro_sd_buffer = f.read()
        f.close()

    if check_SDRAM_64.get():
        f = open('auxiliar/qsf/SDRAM.aux', 'r')
        sdram_64_buffer = f.read()
        f.close()

    if check_Ethernet.get():
        f = open('auxiliar/qsf/ETHERNET.aux', 'r')
        ethernet_buffer = f.read()
        f.close()

    if check_PMOD.get():
        f = open('auxiliar/qsf/PMOD.aux', 'r')
        pmod_buffer = f.read()
        f.close()

    if check_GPIO.get():
        f = open('auxiliar/qsf/GPIO.aux', 'r')
        gpio_buffer = f.read()
        f.close()

    if check_SA_SB.get():
        f = open('auxiliar/qsf/EXPANSION_KEY.aux', 'r')
        sa_sb_buffer = f.read()
        f.close()

    with open(nome_arquivo, 'w') as qsf:
        qsf.write('#============================================================\n'
                  '# Build by Terasic System Builder\n'
                  '#============================================================\n\n')
        qsf.write('set_global_assignment -name FAMILY "Cyclone IV E"\n')
        qsf.write('set_global_assignment -name DEVICE EP4CE30F23C7\n')
        qsf.write('set_global_assignment -name TOP_LEVEL_ENTITY "{}"\n'.format(projeto))
        qsf.write('set_global_assignment -name ORIGINAL_QUARTUS_VERSION "13.0 SP1"\n')
        qsf.write('set_global_assignment -name LAST_QUARTUS_VERSION "18.1.0 Lite Edition"\n')
        qsf.write('set_global_assignment -name PROJECT_CREATION_TIME_DATE "{}"\n'.format(data.strftime('%H:%M:%S %B %d,%Y')))
        qsf.write('set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files\n')
        qsf.write('set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0\n')
        qsf.write('set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85\n')
        qsf.write('set_global_assignment -name ERROR_CHECK_FREQUENCY_DIVISOR 1\n')
        qsf.write('set_global_assignment -name NOMINAL_CORE_SUPPLY_VOLTAGE 1.2V\n')
        qsf.write('set_global_assignment -name EDA_SIMULATION_TOOL "ModelSim-Altera (VHDL)"\n')
        qsf.write('set_global_assignment -name EDA_OUTPUT_DATA_FORMAT VHDL -section_id eda_simulation\n')

        qsf.write('set_global_assignment -name VHDL_FILE ../src/{}.vhd\n'.format(projeto))
        qsf.write('set_global_assignment -name SDC_FILE {}.sdc\n\n'.format(projeto))

        #qsf.write('set_global_assignment -name SDC_FILE {}.SDC\n'.format(projeto))

        if check_clock.get():
            qsf.write(clock_buffer)
            qsf.write('\n')

        if check_ext_clock.get():
            qsf.write(ext_clock_buffer)
            qsf.write('\n')

        if check_chave.get():
            qsf.write(chave_buffer)
            qsf.write('\n')

        if check_button.get(): #KEY
            qsf.write(button_buffer)
            qsf.write('\n')

        if check_segmentos.get():
            qsf.write(segmentos_buffer)
            qsf.write('\n')

        if check_LED.get():
            qsf.write(led_buffer)
            qsf.write('\n')

        if check_LED_RGB.get():
            qsf.write(led_rgb_buffer)
            qsf.write('\n')

        if check_I2C.get():
            qsf.write(i2c_buffer)
            qsf.write('\n')

        if check_LCD.get():
            qsf.write(lcd_buffer)
            qsf.write('\n')

        if check_VGA.get():
            qsf.write(vga_buffer)
            qsf.write('\n')

        # if check_UART.get():
        #     pass

        # if check_USB.get():
        #     pass

        if check_ADC.get():
            qsf.write(adc_buffer)
            qsf.write('\n')

        if check_DAC.get():
            qsf.write(dac_buffer)
            qsf.write('\n')

        if check_micro_SD.get():
            qsf.write(micro_sd_buffer)
            qsf.write('\n')

        if check_SDRAM_64.get():
            qsf.write(sdram_64_buffer)
            qsf.write('\n')

        if check_Ethernet.get():
            qsf.write(ethernet_buffer)
            qsf.write('\n')

        if check_PMOD.get():
            qsf.write(pmod_buffer)
            qsf.write('\n')

        if check_GPIO.get():
            qsf.write(gpio_buffer)
            qsf.write('\n')

        if check_SA_SB.get():
            qsf.write(sa_sb_buffer)
            qsf.write('\n')


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
    nome_arquivo = '{}.v'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    v = open(nome_arquivo, 'w')
    v.write('module {}(\n'.format(projeto))

    if check_clock.get():
        v.write('\t//////////// CLOCK ////////////\n')
        v.write('\tinput\t\t\t\t\tADC_CLK_10,\n\tinput\t\t\t\t\tMAX10_CLK1_50,\n\tinput\t\t\t\t\tMAX10_CLK2_50\n')
    if check_SDRAM_64.get():
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

    if check_chave.get():
        v.write('\n\t//////////// KEY ////////////\n')
        v.write('\tinput\t\t [1:0]\t\tinput,\n')

    if check_LED.get():
        v.write('\n\t//////////// LED ////////////\n')
        v.write('\toutput\t\t [7:0][4:0]\t\tLEDR,\n')

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
    nome_arquivo = '{}.sdc'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    if check_clock.get():
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
    Button(frame, text="Salvar Configuração", command=get_estados).grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Carregar Configuração", command=set_estados).grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Gerar", command=gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Sair", command=window.destroy).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)


def gerar_rodape(largura, altura, background_color):
    frame_rodape = Frame(window, width=largura, height=altura, bg=background_color)
    frame_rodape.pack(fill=X, side=BOTTOM)
    gerar_botoes_rodape(frame_rodape)


def get_estados():
    estados = {
        'projeto_nome': get_nome_do_projeto(),
        'check_clock': check_clock.get(),
        'check_SDRAM_64': check_SDRAM_64.get(),
        'check_segmentos': check_segmentos.get(),
        'check_chave': check_chave.get(),
        'check_LED': check_LED.get(),
        'check_button': check_button.get(),
        'check_VGA': check_VGA.get(),
        'check_GPIO': check_GPIO.get(),
        'check_LCD': check_LCD.get(),
        'check_Ethernet': check_Ethernet.get(),
        'check_I2C': check_I2C.get(),
        'check_RS232': check_RS232.get(),
        'check_micro_SD': check_micro_SD.get(),
        'check_SDRAM_512': check_SDRAM_512.get(),
        'check_PMOD': check_PMOD.get(),
        'check_flash_64': check_flash_64.get(),
        'check_LED_RGB': check_LED_RGB.get(),
        'check_ADC': check_ADC.get(),
        'check_DAC': check_DAC.get(),
        'check_SA_SB': check_SA_SB.get()
    }

    tipo_do_arquivo = (('text files', '.json'), ('All files', '*.*'))

    arquivo = fd.asksaveasfile(mode='w', filetypes=tipo_do_arquivo, defaultextension='.json')

    if arquivo is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    json.dump(estados, arquivo)


def set_estados():
    with open(get_arquivo('.json')) as f:
        data = json.load(f)

    nome_do_projeto.set(data['projeto_nome'])

    check_clock.set(data['check_clock'])
    check_SDRAM_64.set(data['check_SDRAM_64'])
    check_segmentos.set(data['check_segmentos'])
    check_chave.set(data['check_chave'])
    check_LED.set(data['check_LED'])
    check_button.set(data['check_button'])
    check_VGA.set(data['check_VGA'])
    check_GPIO.set(data['check_GPIO'])
    check_LCD.set(data['check_LCD'])
    check_Ethernet.set(data['check_Ethernet'])
    check_I2C.set(data['check_I2C'])
    check_RS232.set(data['check_RS232'])
    check_micro_SD.set(data['check_micro_SD'])
    check_SDRAM_512.set(data['check_SDRAM_512'])
    check_PMOD.set(data['check_PMOD'])
    check_flash_64.set(data['check_flash_64'])
    check_LED_RGB.set(data['check_LED_RGB'])
    check_ADC.set(data['check_ADC'])
    check_DAC.set(data['check_DAC'])
    check_SA_SB.set(data['check_SA_SB'])


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
criar_selecao('SDRAM 512Mbit', check_SDRAM_512, 1, 7)
criar_selecao('Conector Micro SD', check_micro_SD, 1, 8)
criar_selecao('Serial RS232', check_RS232, 1, 9)
criar_selecao('Sensor de temperatura I²C', check_I2C, 1, 10)
criar_selecao('10/100 Ethernet PHY', check_Ethernet, 1, 11)

criar_selecao('7-Segmentos X 2', check_segmentos, 2, 2)
criar_selecao('Chave X4', check_chave, 2, 3)
criar_selecao('Conector 2x GPIO', check_GPIO, 2, 4)
criar_selecao('SDRAM, 64 MB', check_SDRAM_64, 2, 5)
criar_selecao('SA e SB', check_SA_SB, 2, 6)
criar_selecao('DAC', check_DAC, 2, 7)
criar_selecao('ADC', check_ADC, 2, 8)
criar_selecao('LED RGB', check_LED_RGB, 2, 9)
criar_selecao('FLASH 64Mbit', check_flash_64, 2, 10)
criar_selecao('PMOD x2', check_PMOD, 2, 11)


window.resizable(False, False)
window.mainloop()
