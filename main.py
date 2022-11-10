#importanto bibliotecas
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
#cores

cor1 = '#12171c'
cor2 = '#1b1c21'
cor3 = '#f5f6f7' #branco
cor4 = '#cf9913' #laranja


#inicio / start
janela = Tk()
janela.title('CALCULADORA DE IDADE')
janela.geometry('310x400+400+200')


frame_tela = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg = cor1)
frame_tela.grid(row=0, column=0)

#corpo é onde será atribuido os botões
frame_corpo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg = cor2)
frame_corpo.grid(row=1, column=0)


#conteudo do frame tela

tela_calc_cima = Label(frame_tela, text = 'Calculadora', width = 25, height = 1, pady = 3, relief = FLAT, anchor = 'center', font = ('Helvética 15 bold'), bg = cor1, fg = cor3 )
tela_calc_cima.place(x=0, y = 20)

tela_calc_baixo = Label(frame_tela, text = 'DE IDADE', width = 15, height = 1, pady = 3, relief = FLAT, anchor = 'center', font = ('Helvética 25 bold'), bg = cor1, fg = cor3 )
tela_calc_baixo.place(x=0, y = 60)



#conteudo do frame corpo

data_inicial = Label(frame_corpo, text = 'Data Inicial', width = 13, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 12 bold'), bg = cor2, fg = cor3)
data_inicial.place(x=0, y=20)

calendario_1 = DateEntry(frame_corpo, width = 13, bg = cor3, fg = cor4, borderwidth = 2,locale = 'pt_BR', data_patter= 'dd-mm-y', y = 2022, tooltipbackground = cor2, foreground = cor3)
calendario_1.place(x=143, y = 20)

data_nascimento = Label(frame_corpo, text = 'Nascimento', width = 13, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 12 bold'), bg = cor2, fg = cor3)
data_nascimento.place(x=0, y = 60)

calendario_2 = DateEntry(frame_corpo, width = 13, bg = cor3, fg = cor4, borderwidth = 2,locale = 'pt_BR', data_patter= 'dd-mm-y', y = 2022)
calendario_2.place(x=143, y = 60)


ano = Label(frame_corpo, text = '22', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 25 bold'), bg = cor2, fg = cor3)
ano.place(x=0, y=110)

ano_t = Label(frame_corpo, text = 'anos', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 15 bold'), bg = cor2, fg = cor3)
ano_t.place(x=19, y=150)

mes = Label(frame_corpo, text = '22', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 25 bold'), bg = cor2, fg = cor3)
mes.place(x=95, y=110)

mes_t = Label(frame_corpo, text = 'meses', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 15 bold'), bg = cor2, fg = cor3)
mes_t.place(x=114, y=150)

dia = Label(frame_corpo, text = '22', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 25 bold'), bg = cor2, fg = cor3)
dia.place(x=190, y=110)

dia_t = Label(frame_corpo, text = 'dias', width = 5, height = 1,  pady = 3, relief = FLAT, font = ('Helvética 15 bold'), bg = cor2, fg = cor3)
dia_t.place(x=210, y=150)




janela.mainloop()
