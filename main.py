from tkinter import *
from math import pow, sqrt


class Window:

    def __init__(self, width, height, title='MyWindow', resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.equation_label = StringVar()
        self.equation_label.set(value='0')
        self.nums = ''

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):

        l1 = Label(self.root, textvariable=self.equation_label, font=('consolas', 15), bg='white', width=24, height=2)
        l1.pack()

        frame = Frame(self.root)
        frame.pack()

        Button(frame, text=7, height=4, width=9, command=lambda: self.button_press(7)).grid(column=0, row=1)
        Button(frame, text=8, height=4, width=9, command=lambda: self.button_press(8)).grid(column=1, row=1)
        Button(frame, text=9, height=4, width=9, command=lambda: self.button_press(9)).grid(column=2, row=1)
        Button(frame, text=4, height=4, width=9, command=lambda: self.button_press(4)).grid(column=0, row=2)
        Button(frame, text=5, height=4, width=9, command=lambda: self.button_press(5)).grid(column=1, row=2)
        Button(frame, text=6, height=4, width=9, command=lambda: self.button_press(6)).grid(column=2, row=2)
        Button(frame, text=1, height=4, width=9, command=lambda: self.button_press(1)).grid(column=0, row=3)
        Button(frame, text=2, height=4, width=9, command=lambda: self.button_press(2)).grid(column=1, row=3)
        Button(frame, text=3, height=4, width=9, command=lambda: self.button_press(3)).grid(column=2, row=3)
        Button(frame, text='.', height=4, width=9, command=lambda: self.button_press('.')).grid(column=2, row=4)
        Button(frame, text='+', height=4, width=9, command=lambda: self.button_press('+')).grid(column=3, row=0)
        Button(frame, text='-', height=4, width=9, command=lambda: self.button_press('-')).grid(column=3, row=1)
        Button(frame, text='*', height=4, width=9, command=lambda: self.button_press('*')).grid(column=3, row=2)
        Button(frame, text='/', height=4, width=9, command=lambda: self.button_press('/')).grid(column=3, row=3)
        Button(frame, text=0, height=4, width=9, command=lambda: self.button_press(0)).grid(column=1, row=4)
        Button(frame, text='C', height=4, width=9, command=self.clear).grid(column=0, row=4)
        Button(frame, text='=', height=4, width=9, command=self.result).grid(column=3, row=4)
        Button(frame, text='^2', height=4, width=9, command=self.double).grid(column=2, row=0)
        Button(frame, text='√', height=4, width=9, command=self.sqroot).grid(column=1, row=0)
        Button(frame, text='1/x', height=4, width=9, command=self.div_by_x).grid(column=0, row=0)

    def button_press(self, num):
        self.equation_label.set(value=num)
        self.nums += self.equation_label.get()
        self.equation_label.set(value=self.nums)

    def clear(self):
        self.nums = ''
        self.equation_label.set(value='0')

    def result(self):
        evals = self.equation_label.get()
        try:
            final_eval = eval(evals)
            self.equation_label.set(value=final_eval)
            self.nums = str(final_eval)
        except SyntaxError:
            self.equation_label.set(value='Ошибка ввода')
            self.nums = ''
        except ZeroDivisionError:
            self.equation_label.set(value='На ноль делить нельзя')
            self.nums = ''

    def double(self):
        self.equation_label.set(value=str(pow(float(self.nums), 2)))
        self.nums = str(pow(float(self.nums), 2))

    def sqroot(self):
        if float(self.nums) >= 0:
            self.equation_label.set(value=str(sqrt(float(self.nums))))
            self.nums = str(sqrt(float(self.nums)))
        else:
            self.equation_label.set(value='Число меньше 0')
            self.nums = ''

    def div_by_x(self):
        if float(self.nums) != 0:
            self.equation_label.set(value=str(1/float(self.nums)))
            self.nums = str(1/float(self.nums))
        else:
            self.equation_label.set(value='На ноль делить нельзя')
            self.nums = ''


if __name__ == '__main__':
    window = Window(300, 400, 'Calculator', (False, False))
    window.run()