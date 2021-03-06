Tkinter


from tkinter import *


def help_(text=None, title=None):
    if not text:
        text = ''
    if not title:
        title = 'Помощь'
    txt = str(title) + '\n' + str(text)+"""\n\n\nЗаполнение значений: 
    Suburb - регион (обязательно)
    Rooms - кол-во комнат (обязательно)
    Type - тип (обязательно)
    Distance - дистанция (обязательно)
    Postcode - индекс (обязательно)
    Bathroom - кол-во ванных (обязательно)
    BuildingArea - площадь (не обязательно)
    YearBuilt - год постройки  (не обязательно)
    Без обязательных полей, программа не выведет предсказание
    """
    hlp = Tk()
    hlp.title(title)
    hlp.geometry("500x300")
    lab = Label(hlp, text=txt)
    lab.place(x=50, y=50)
    hlp.mainloop()


def pressed():
    cols = ['Suburb', 'Rooms', 'Type', 'Distance', 'Postcode', 'Bathroom', 'BuildingArea', 'YearBuilt']
    try:
        try:
            e7 = float(ent7.get())
        except:
            e7 = np.nan
        try:
            e8 = int(ent8.get())
        except:
            e8 = np.nan
        arr = [ent1.get(), 
               int(ent2.get()), 
               ent3.get(), 
               float(ent4.get()), 
               int(ent5.get()), 
               int(ent6.get()),
               e7, 
               e8]
    except:
        help_(text='Некорректный ввод', title='Ошибка')
        return 0
    arr = pd.DataFrame([arr], columns=cols)
    arr = pipe.transform(arr)
    pred = model.predict(arr)
    labx1.config(text=': {}'.format(pred))


root = Tk()
root.title('GUI 1.3')
root.geometry("800x600")


lab1 = Label(text='Suburb')
lab1.place(x=50, y=30)
lab2 = Label(text='Rooms')
lab2.place(x=200, y=30)
lab3 = Label(text='Type')
lab3.place(x=350, y=30)
lab4 = Label(text='Distance')
lab4.place(x=500, y=30)

lab1 = Label(text='Postcode')
lab1.place(x=50, y=120)
lab2 = Label(text='Bathroom')
lab2.place(x=200, y=120)
lab3 = Label(text='BuildingArea')
lab3.place(x=350, y=120)
lab4 = Label(text='YearBuilt')
lab4.place(x=500, y=120)


ent1 = Entry(width=20)
ent1.place(x=50, y=50)
ent2 = Entry(width=20)
ent2.place(x=200, y=50)
ent3 = Entry(width=20)
ent3.place(x=350, y=50)
ent4 = Entry(width=20)
ent4.place(x=500, y=50)

ent5 = Entry(width=20)
ent5.place(x=50, y=150)
ent6 = Entry(width=20)
ent6.place(x=200, y=150)
ent7 = Entry(width=20)
ent7.place(x=350, y=150)
ent8 = Entry(width=20)
ent8.place(x=500, y=150)



but = Button(command=help_, text='Помощь')
but.place(x=0, y=0)

but = Button(command=pressed, text='Предсказать значение')
but.place(x=50, y=300)
labx1 = Label(text=': ')
labx1.place(x=200, y=300)


root.mainloop()
