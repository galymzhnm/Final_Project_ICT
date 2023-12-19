from tkinter import *
import math

window = Tk()
window.title('calculator')
window.geometry('270x370+700+100')
window.configure(bg='purple')


def delete_last():
    current_text = e.get()
    if current_text:
        e.delete(len(current_text) - 1, END)


def input_e(symbol):
    e.insert(END, symbol)


def clear():
    e.delete(0, END)


def count_result():
    txt = e.get()
    result = 0
    if '+' in txt:
        sd_txt = txt.split('+')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        result = a1 + a2
    if '%' in txt:
        sd_txt = txt.split('%')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        result = a1 % a2
    if '-' in txt:
        sd_txt = txt.split('-')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        result = a1 - a2
    if '*' in txt:
        sd_txt = txt.split('*')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        result = a1 * a2
    if '/' in txt:
        sd_txt = txt.split('/')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        if a2 == 0:
            result = 'error'
        else:
            result = a1 / a2
    if '^' in txt:
        sd_txt = txt.split('^')
        a1 = float(sd_txt[0])
        a2 = float(sd_txt[1])
        result = a1 ** a2
    if '√' in txt:
        sd_txt = txt.split('√')
        a1 = float(sd_txt[1])
        result = math.sqrt(a1)
    if 'sin' in txt:
        sd_txt = txt.split('sin')
        a1 = float(sd_txt[1])
        result = math.sin(a1)
    if 'cos' in txt:
        sd_txt = txt.split('cos')
        a1 = float(sd_txt[1])
        result = math.cos(a1)

    clear()
    e.insert(0, result)


e = Entry(window, width=16, font=('', 20))
e.place(x=10, y=50)
# M means 'CE=Clean Entry'
btnM = Button(window, bg='blue', fg='white', text='CE', command=clear)
btnM.place(x=10, y=90, width=50, height=50)
# S means '/'
btnS = Button(window, bg='violet', fg='white', text='/', command=lambda: input_e('/'))
btnS.place(x=60, y=90, width=50, height=50)
# K means '%'
btnK = Button(window, bg='green', fg='white', text='%', command=lambda: input_e('%'))
btnK.place(x=110, y=90, width=50, height=50)
# J means '-'
btnJ = Button(window, bg='red', fg='white', text='-', command=lambda: input_e('-'))
btnJ.place(x=160, y=90, width=50, height=50)
# U means '√'
btnU = Button(window, bg='orange', fg='white', text='√', command=lambda: input_e('√'))
btnU.place(x=210, y=90, width=45, height=50)
btn1 = Button(window, bg='blue', fg='white', text='1', command=lambda: input_e('1'))
btn1.place(x=10, y=140, width=50, height=50)
btn2 = Button(window, bg='violet', fg='white', text='2', command=lambda: input_e('2'))
btn2.place(x=60, y=140, width=50, height=50)
btn3 = Button(window, bg='green', fg='white', text='3', command=lambda: input_e('3'))
btn3.place(x=110, y=140, width=50, height=50)
# N means '+'
btnN = Button(window, bg='red', fg='white', text='+', command=lambda: input_e('+'))
btnN.place(x=160, y=140, width=50, height=50)
# X means 'sin'
btnX = Button(window, bg='orange', fg='white', text='sin', command=lambda: input_e('sin'))
btnX.place(x=210, y=140, width=45, height=50)
btn4 = Button(window, bg='blue', fg='white', text='4', command=lambda: input_e('4'))
btn4.place(x=10, y=190, width=50, height=50)
btn5 = Button(window, bg='violet', fg='white', text='5', command=lambda: input_e('5'))
btn5.place(x=60, y=190, width=50, height=50)
btn6 = Button(window, bg='green', fg='white', text='6', command=lambda: input_e('6'))
btn6.place(x=110, y=190, width=50, height=50)
# I means '*'
btnI = Button(window, bg='red', fg='white', text='*', command=lambda: input_e('*'))
btnI.place(x=160, y=190, width=50, height=50)
#H means 'возведение в степень'
btnH =  Button(window, bg='orange', fg='white', text = '^', command = lambda : input_e('^'))
btnH.place(x = 210, y = 190, width = 45, height = 50)
#B means 'cos'
btnB =  Button(window, bg='orange', fg='white', text = 'cos', command = lambda : input_e('cos'))
btnB.place(x = 210, y = 240, width = 45, height = 50)
btn7 =  Button(window, bg='blue', fg='white', text = '7', command = lambda : input_e('7'))
btn7.place(x = 10, y = 240, width = 50, height = 50)
btn8 =  Button(window, bg='violet', fg='white', text = '8', command = lambda : input_e('8'))
btn8.place(x = 60, y = 240, width = 50, height = 50)
btn9 =  Button(window, bg='green', fg='white', text = '9', command = lambda : input_e('9'))
btn9.place(x = 110, y = 240, width = 50, height = 50)
#P means '='
btnP =  Button(window, bg='red', fg='white', text = '=', command = count_result)
btnP.place(x = 160, y = 240, width = 50, height = 50)
btn0 =  Button(window, bg='blue', fg='white', text = '0', command = lambda : input_e('0'))
btn0.place(x = 10, y = 290, width = 50, height = 50)
btn00 =  Button(window, bg='violet', fg='white', text = '00', command = lambda : input_e('00'))
btn00.place(x = 60, y = 290, width = 50, height = 50)
#O means ','
btnO =  Button(window, bg='green', fg='white', text = '.', command = lambda : input_e('.'))
btnO.place(x = 110, y = 290, width = 50, height = 50)
#Q means '000'
btnQ =  Button(window, bg='red', fg='white', text = '000', command = lambda : input_e('000'))
btnQ.place(x = 160, y = 290, width = 50, height = 50)
#Y means 'del'
btnY =  Button(window, bg='orange', fg='white', text = 'del', command=delete_last)
btnY.place(x = 210, y = 290, width = 45, height = 50)

window.mainloop()