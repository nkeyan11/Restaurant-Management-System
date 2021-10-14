
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import pymysql
staffname = ''
passw = ''
passv=0
def mainlogin():
    global staffname
    global passv
    global passw
    global sdet
    def loginms():
        global staffname
        global passv
        if sdet == ():
            messagebox.showinfo('Showinfo', 'Username is not valid')
        for i in sdet:
            if i[0] == staffname:
                if i[1] == passw:
                    messagebox.showinfo('Showinfo', 'Password authentication succeeded')
                    passv=1
                    win.destroy()
                if i[1] != passw:
                    messagebox.showinfo('Showinfo', 'Password incorrect. Try again')
            if i[0] != staffname:
                messagebox.showinfo('Showinfo', 'Username is not valid')

    def clik():
        global staffname
        global passw
        k1g = str(k1.get())
        p1g = str(p1.get())
        staffname = k1g
        passw = p1g

        def logindb():
            global sdet
            global staffname
            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            cur = dbc.cursor()
            setvar = 'set @usrdet = ' + '"' + staffname + '"'
            cur.execute(setvar)
            cur.execute('select stafname,password from staff where stafname = @usrdet')
            sdet = cur.fetchall()



        logindb()

    win = Tk()
    win.title('Login Page')
    win.geometry('700x450')
    k1 = StringVar()
    p1 = StringVar()
    wint = Entry(win, textvariable=k1,width=30)
    passt = Entry(win, show='*', textvariable=p1,width=30)
    lt = Label(win, text='Username', font='arial 18', bg='black',fg='white')
    lp = Label(win, text='Password', font='arial 18', bg='black',fg='white')
    wint.place(x=400, y=172)
    win.config(bg='black')
    lt.place(x=240, y=165)
    passt.place(x=400, y=207)
    lp.place(x=240, y=200)

    b1 = Button(win, text='Submit',font='arial 15', bg='yellow', command=lambda: [clik(), loginms()])
    b1.place(x=300, y=250)

    win.mainloop()

def restop():
    bt = 1
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []

    tab = Tk()
    tab.title('Select Tables / Takeaway')
    tab.config(bg='deep sky blue')
    tab.geometry('1366x700')
    logl = Label(tab, text='Logged in as ' + staffname, font='bold')

    bg = Image.open("tableselect.jpg")
    bgdine = ImageTk.PhotoImage(bg)
    dinejpg = Label(tab, image=bgdine)
    dinejpg.image = bgdine
    dinejpg.place(x=15, y=50)

    def digital_clock():
        time1 = time.strftime("%I:%M:%S %p")
        date1 = time.strftime("%d,%B,%Y")
        logt.config(text='Date: ' + date1 + ' / Time: ' + time1)
        logt.after(1000, digital_clock)

    logt = Label(tab, font='bold')
    logt.place(x=900, y=0)
    logl.place(x=0, y=0)
    digital_clock()

    def itemmenu1():
        cname1 = 'Walk Inn Customer'
        pno1='NA'
        global l1
        l1 = []
        global item1
        global tabv
        global bt
        bt = 1
        item1 = Toplevel()
        item1.title(tabv)
        item1.geometry('1366x700')
        item1.config(bg='deep sky blue')

        def genbill1():
            global cname1
            global pno1
            k1 = open(blk1, 'a')
            k1.write(f'\n\n\n***** Order closed for {billno1} *******')
            k1.close()


            fbill1 = apy1 + (apy1 * .05)

            bil1.write('\n=======================================================================')
            bil1.write(f'\n\n        Total Amount = {apy1} + 5% GST({apy1 * .05})')
            bil1.write(f'\n\n                Total Amount= {fbill1}')
            bil1.write('\n\n               Thank You! Visit Again!!')
            bil1.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst=(blg1.rstrip('.txt'),staffname,cname1,pno1,time.strftime('%d,%b,%y'),time.strftime('%I:%M:%S %p'),fbill1)
            ins='insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins,lsst)
            dbc.close()

        blk1 = time.strftime("%Y%m%d%I%M%S")
        blk1 = 'k' + blk1 + '.txt'
        k1 = open(blk1, 'a')
        k1.write(f'{tabv}\n')
        k1.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k1.write(f'Order Details for {tabv} : \n')
        k1.close()

        blg1 = time.strftime("%Y%m%d%I%M%S")
        blg1 = blg1 + '.txt'
        bil1 = open(blg1, 'a')
        bil1.write('                  The Lassi Corner \n')
        bil1.write('                      K.K.Nagar \n')
        bil1.write('                  Ph: 9852415687 \n')
        bil1.write(f'                  Staffname: {staffname}  \n       ')
        bil1.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil1.write(f'\n            Bill Number: {billno1}')
        bil1.write(f'\n                     {tabv}\n')
        bil1.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil1.write(f'Order Details for {tabv} : \n')
        bil1.write('\n=======================================================================')
        bil1.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil1.write('\n=======================================================================')

        def hidew1():
            item1.withdraw()

        hideb1 = Button(item1, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew1)
        hideb1.place(x=50, y=610)
        fin1 = Button(item1, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini1(), genbill1()])
        fin1.place(x=800, y=610)

        F1 = LabelFrame(item1, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname1
            global pno1
            cname1 = c_name.get()
            pno1 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno1}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname1}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno1}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm1():
            global apy1
            global bt
            global l1
            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()
            if cb1 != 0:
                k1 = open(blk1, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k1.write(f'\n{it1}\t\t{sb1}')
                bil1.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l1.append(m)
            if cb2 != 0:
                k1 = open(blk1, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k1.write(f'\n{it2}\t{sb2}')
                bil1.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l1.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k1 = open(blk1, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k1.write(f'\n{it3}\t\t{sb3}')
                bil1.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l1.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k1 = open(blk1, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k1.write(f'\n{it4}\t{sb4}')
                bil1.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l1.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k1.write(f'\n{it5}\t\t{sb5}')
                bil1.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l1.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k1.write(f'\n{it6}\t\t{sb6}')
                bil1.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l1.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k1.write(f'\n{it7}\t{sb7}')
                bil1.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l1.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k1.write(f'\n{it8}\t{sb8}')
                bil1.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l1.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k1.write(f'\n{it9}\t{sb9}')
                bil1.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l1.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k1.write(f'\n{it10}\t{sb10}')
                bil1.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l1.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k1.write(f'\n{it11}\t\t{sb11}')
                bil1.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l1.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k1.write(f'\n{it12}\t{sb12}')
                bil1.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l1.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k1.write(f'\n{it13}\t{sb13}')
                bil1.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l1.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k1 = open(blk1, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k1.write(f'\n{it14}\t{sb14}')
                bil1.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l1.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k1 = open(blk1, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k1.write(f'\n{it15}\t{sb15}')
                bil1.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l1.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k1 = open(blk1, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k1.write(f'\n{it16}\t\t{sb16}')
                bil1.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l1.append(m)

            apy1 = sum(l1)
            amtpy = Label(item1, text='Amount Payable: ' + str(apy1) + ' + Tax: ' + str(apy1 + (apy1 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',
                          fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k1.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item1, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item1, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm1)
        btn1.place(x=300, y=610)
        clr = Button(item1, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item1.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(item1, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item1, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item1, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item1, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item1, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item1, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item1, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item1, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item1, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item1, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item1, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item1, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item1, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item1, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item1, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item1, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item1, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item1.mainloop()

    def itemmenu2():
        cname2 = 'Walk Inn Customer'
        pno2='NA'
        global l2
        l2 = []
        global item2
        global tabv
        global bt
        bt = 1
        item2 = Toplevel()
        item2.title(tabv)
        item2.geometry('1366x700')
        item2.config(bg='deep sky blue')

        def genbill2():
            global cname2
            global pno2
            k2 = open(blk2, 'a')
            k2.write(f'\n\n\n***** Order closed for {billno2} *******')
            k2.close()

            fbill2 = apy2 + (apy2 * .05)

            bil2.write('\n=======================================================================')
            bil2.write(f'\n\n        Total Amount = {apy2} + 5% GST({apy2 * .05})')
            bil2.write(f'\n\n                Total Amount= {fbill2}')
            bil2.write('\n\n               Thank You! Visit Again!!')
            bil2.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg2.rstrip('.txt'), staffname, cname2, pno2, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill2)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk2 = time.strftime("%Y%m%d%I%M%S")
        blk2 = 'k' + blk2 + '.txt'
        k2 = open(blk2, 'a')
        k2.write(f'{tabv}\n')
        k2.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k2.write(f'Order Details for {tabv} : \n')
        k2.close()

        blg2 = time.strftime("%Y%m%d%I%M%S")
        blg2 = blg2 + '.txt'
        bil2 = open(blg2, 'a')
        bil2.write('                  The Lassi Corner \n')
        bil2.write('                      K.K.Nagar \n')
        bil2.write('                  Ph: 9852415687 \n')
        bil2.write(f'                  Staffname: {staffname}  \n       ')
        bil2.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil2.write(f'\n            Bill Number: {billno2}')
        bil2.write(f'\n                     {tabv}\n')
        bil2.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil2.write(f'Order Details for {tabv} : \n')
        bil2.write('\n=======================================================================')
        bil2.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil2.write('\n=======================================================================')

        def hidew2():
            item2.withdraw()

        hideb2 = Button(item2, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew2)

        hideb2.place(x=50, y=610)
        fin2 = Button(item2, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini2(), genbill2()])
        fin2.place(x=800, y=610)

        F1 = LabelFrame(item2, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname2
            global pno2
            cname2 = c_name.get()
            pno2 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno2}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname2}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno2}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\tPrice\t\tQTY \tTotal')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm2():
            global bt
            global apy2
            global l2

            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()
            if cb1 != 0:
                k2 = open(blk2, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k2.write(f'\n{it1}\t\t{sb1}')
                bil2.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l2.append(m)
            if cb2 != 0:
                k2 = open(blk2, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k2.write(f'\n{it2}\t{sb2}')
                bil2.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l2.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k2 = open(blk2, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k2.write(f'\n{it3}\t\t{sb3}')
                bil2.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l2.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k2 = open(blk2, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k2.write(f'\n{it4}\t{sb4}')
                bil2.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l2.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k2.write(f'\n{it5}\t\t{sb5}')
                bil2.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l2.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k2.write(f'\n{it6}\t\t{sb6}')
                bil2.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l2.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k2.write(f'\n{it7}\t{sb7}')
                bil2.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l2.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k2.write(f'\n{it8}\t{sb8}')
                bil2.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l2.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k2.write(f'\n{it9}\t{sb9}')
                bil2.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l2.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k2.write(f'\n{it10}\t{sb10}')
                bil2.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l2.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k2.write(f'\n{it11}\t\t{sb11}')
                bil2.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l2.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k2.write(f'\n{it12}\t{sb12}')
                bil2.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l2.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k2.write(f'\n{it13}\t{sb13}')
                bil2.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l2.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k2 = open(blk2, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k2.write(f'\n{it14}\t{sb14}')
                bil2.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l2.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k2 = open(blk2, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k2.write(f'\n{it15}\t{sb15}')
                bil2.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l2.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k2 = open(blk2, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k2.write(f'\n{it16}\t\t{sb16}')
                bil2.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l2.append(m)

            apy2 = sum(l2)
            amtpy = Label(item2, text='Amount Payable: ' + str(apy2) + ' + Tax: ' + str(apy2 + (apy2 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k2.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item2, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item2, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm2)
        btn1.place(x=300, y=610)
        clr = Button(item2, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item2.protocol('WM_DELETE_WINDOW', __CancelCommand)

        itms = Label(item2, text='Items Select', bg='deep sky blue', fg='black', font='arial 18')
        itms.place(x=265, y=100)

        F3 = Frame(item2, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 18', height=2, bg='deep sky blue')
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item2, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item2, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item2, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item2, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item2, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item2, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item2, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item2, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item2, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item2, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item2, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item2, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item2, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item2, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item2, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item2, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item2.mainloop()

    def itemmenu3():
        cname3 = 'Walk Inn Customer'
        pno3='NA'
        global l3
        l3 = []
        global item3
        global tabv
        global bt
        bt = 1
        item3 = Toplevel()
        item3.title(tabv)
        item3.geometry('1366x700')
        item3.config(bg='deep sky blue')

        def genbill3():
            global cname3
            global pno3
            k3 = open(blk3, 'a')
            k3.write(f'\n\n\n***** Order closed for {billno3} *******')
            k3.close()

            fbill3 = apy3 + (apy3 * .05)

            bil3.write('\n=======================================================================')
            bil3.write(f'\n\n        Total Amount = {apy3} + 5% GST({apy3 * .05})')
            bil3.write(f'\n\n                Total Amount= {fbill3}')
            bil3.write('\n\n               Thank You! Visit Again!!')
            bil3.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg3.rstrip('.txt'), staffname, cname3, pno3, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill3)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk3 = time.strftime("%Y%m%d%I%M%S")
        blk3 = 'k' + blk3 + '.txt'
        k3 = open(blk3, 'a')
        k3.write(f'{tabv}\n')
        k3.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k3.write(f'Order Details for {tabv} : \n')
        k3.close()

        blg3 = time.strftime("%Y%m%d%I%M%S")
        blg3 = blg3 + '.txt'
        bil3 = open(blg3, 'a')
        bil3.write('                  The Lassi Corner \n')
        bil3.write('                      K.K.Nagar \n')
        bil3.write('                  Ph: 9852415687 \n')
        bil3.write(f'                  Staffname: {staffname}  \n       ')
        bil3.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil3.write(f'\n            Bill Number: {billno3}')
        bil3.write(f'\n                     {tabv}\n')
        bil3.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil3.write(f'Order Details for {tabv} : \n')
        bil3.write('\n=======================================================================')
        bil3.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil3.write('\n=======================================================================')

        def hidew3():
            item3.withdraw()

        hideb3 = Button(item3, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew3)
        hideb3.place(x=50, y=610)
        fin3 = Button(item3, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini3(), genbill3()])
        fin3.place(x=800, y=610)

        F1 = LabelFrame(item3, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname3
            global pno3
            cname3 = c_name.get()
            pno3 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno3}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname3}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno3}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm3():
            global bt
            global l3
            global apy3

            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()

            if cb1 != 0:
                k3 = open(blk3, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k3.write(f'\n{it1}\t\t{sb1}')
                bil3.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l3.append(m)
            if cb2 != 0:
                k3 = open(blk3, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k3.write(f'\n{it2}\t{sb2}')
                bil3.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l3.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k3 = open(blk3, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k3.write(f'\n{it3}\t\t{sb3}')
                bil3.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l3.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k3 = open(blk3, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k3.write(f'\n{it4}\t{sb4}')
                bil3.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l3.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k3.write(f'\n{it5}\t\t{sb5}')
                bil3.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l3.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k3.write(f'\n{it6}\t\t{sb6}')
                bil3.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l3.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k3.write(f'\n{it7}\t{sb7}')
                bil3.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l3.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k3.write(f'\n{it8}\t{sb8}')
                bil3.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l3.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k3.write(f'\n{it9}\t{sb9}')
                bil3.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l3.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k3.write(f'\n{it10}\t{sb10}')
                bil3.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l3.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k3.write(f'\n{it11}\t\t{sb11}')
                bil3.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l3.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k3.write(f'\n{it12}\t{sb12}')
                bil3.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l3.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k3.write(f'\n{it13}\t{sb13}')
                bil3.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l3.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k3 = open(blk3, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k3.write(f'\n{it14}\t{sb14}')
                bil3.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l3.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k3 = open(blk3, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k3.write(f'\n{it15}\t{sb15}')
                bil3.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l3.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k3 = open(blk3, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k3.write(f'\n{it16}\t\t{sb16}')
                bil3.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l3.append(m)

            apy3 = sum(l3)
            amtpy = Label(item3, text='Amount Payable: ' + str(apy3) + ' + Tax: ' + str(apy3 + (apy3 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k3.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item3, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item3, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm3)
        btn1.place(x=300, y=610)
        clr = Button(item3, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item3.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(item3, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item3, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item3, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item3, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item3, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item3, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item3, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item3, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item3, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item3, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item3, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item3, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item3, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item3, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item3, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item3, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item3, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item3.mainloop()

    def itemmenu4():
        cname4 = 'Walk Inn Customer'
        pno4='NA'
        global l4
        l4 = []
        global item4
        global tabv
        global bt
        bt = 1
        item4 = Toplevel()
        item4.title(tabv)
        item4.geometry('1366x700')
        item4.config(bg='deep sky blue')

        def genbill4():
            global cname4
            global pno4
            k4 = open(blk4, 'a')
            k4.write(f'\n\n\n***** Order closed for {billno4} *******')
            k4.close()

            fbill4 = apy4 + (apy4 * .05)

            bil4.write('\n=======================================================================')
            bil4.write(f'\n\n        Total Amount = {apy4} + 5% GST({apy4 * .05})')
            bil4.write(f'\n\n                Total Amount= {fbill4}')
            bil4.write('\n\n               Thank You! Visit Again!!')
            bil4.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg4.rstrip('.txt'), staffname, cname4, pno4, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill4)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk4 = time.strftime("%Y%m%d%I%M%S")
        blk4 = 'k' + blk4 + '.txt'
        k4 = open(blk4, 'a')
        k4.write(f'{tabv}\n')
        k4.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k4.write(f'Order Details for {tabv} : \n')
        k4.close()

        blg4 = time.strftime("%Y%m%d%I%M%S")
        blg4 = blg4 + '.txt'
        bil4 = open(blg4, 'a')
        bil4.write('                  The Lassi Corner \n')
        bil4.write('                      K.K.Nagar \n')
        bil4.write('                  Ph: 9852415687 \n')
        bil4.write(f'                  Staffname: {staffname}  \n       ')
        bil4.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil4.write(f'\n            Bill Number: {billno4}')
        bil4.write(f'\n                     {tabv}\n')
        bil4.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil4.write(f'Order Details for {tabv} : \n')
        bil4.write('\n=======================================================================')
        bil4.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil4.write('\n=======================================================================')

        def hidew4():
            item4.withdraw()

        hideb4 = Button(item4, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew4)
        hideb4.place(x=50, y=610)
        fin4 = Button(item4, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini4(), genbill4()])
        fin4.place(x=800, y=610)

        F1 = LabelFrame(item4, text='Customer Details', font=('times new rommon', 18),bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname4
            global pno4
            cname4 = c_name.get()
            pno4 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno4}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname4}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno4}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm4():
            global bt
            global l4
            global apy4

            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()

            if cb1 != 0:
                k4 = open(blk4, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k4.write(f'\n{it1}\t\t{sb1}')
                bil4.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l4.append(m)
            if cb2 != 0:
                k4 = open(blk4, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k4.write(f'\n{it2}\t{sb2}')
                bil4.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l4.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k4 = open(blk4, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k4.write(f'\n{it3}\t\t{sb3}')
                bil4.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l4.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k4 = open(blk4, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k4.write(f'\n{it4}\t{sb4}')
                bil4.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l4.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k4.write(f'\n{it5}\t\t{sb5}')
                bil4.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l4.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k4.write(f'\n{it6}\t\t{sb6}')
                bil4.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l4.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k4.write(f'\n{it7}\t{sb7}')
                bil4.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l4.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k4.write(f'\n{it8}\t{sb8}')
                bil4.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l4.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k4.write(f'\n{it9}\t{sb9}')
                bil4.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l4.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k4.write(f'\n{it10}\t{sb10}')
                bil4.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l4.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k4.write(f'\n{it11}\t\t{sb11}')
                bil4.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l4.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k4.write(f'\n{it12}\t{sb12}')
                bil4.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l4.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k4.write(f'\n{it13}\t{sb13}')
                bil4.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l4.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k4 = open(blk4, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k4.write(f'\n{it14}\t{sb14}')
                bil4.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l4.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k4 = open(blk4, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k4.write(f'\n{it15}\t{sb15}')
                bil4.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l4.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k4 = open(blk4, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k4.write(f'\n{it16}\t\t{sb16}')
                bil4.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l4.append(m)

            apy4 = sum(l4)
            amtpy = Label(item4, text='Amount Payable: ' + str(apy4) + ' + Tax: ' + str(apy4 + (apy4 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',
                          fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k4.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item4, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item4, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm4)
        btn1.place(x=300, y=610)
        clr = Button(item4, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item4.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(item4, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item4, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item4, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item4, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item4, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item4, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item4, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item4, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item4, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item4, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item4, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item4, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item4, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item4, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item4, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item4, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item4, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item4.mainloop()

    def itemmenu5():
        cname5 = 'Walk Inn Customer'
        pno5='NA'
        global l5
        l5 = []
        global item5
        global tabv
        global bt
        bt = 1
        item5 = Toplevel()
        item5.title(tabv)
        item5.geometry('1366x700')
        item5.config(bg='deep sky blue')

        def genbill5():
            global cname5
            global pno5
            k5 = open(blk5, 'a')
            k5.write(f'\n\n\n***** Order closed for {billno5} *******')
            k5.close()

            fbill5 = apy5 + (apy5 * .05)

            bil5.write('\n=======================================================================')
            bil5.write(f'\n\n        Total Amount = {apy5} + 5% GST({apy5 * .05})')
            bil5.write(f'\n\n                Total Amount= {fbill5}')
            bil5.write('\n\n               Thank You! Visit Again!!')
            bil5.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg5.rstrip('.txt'), staffname, cname5, pno5, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill5)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk5 = time.strftime("%Y%m%d%I%M%S")
        blk5 = 'k' + blk5 + '.txt'
        k5 = open(blk5, 'a')
        k5.write(f'{tabv}\n')
        k5.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k5.write(f'Order Details for {tabv} : \n')
        k5.close()

        blg5 = time.strftime("%Y%m%d%I%M%S")
        blg5 = blg5 + '.txt'
        bil5 = open(blg5, 'a')
        bil5.write('                  The Lassi Corner \n')
        bil5.write('                      K.K.Nagar \n')
        bil5.write('                  Ph: 9852415687 \n')
        bil5.write(f'                  Staffname: {staffname}  \n       ')
        bil5.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil5.write(f'\n            Bill Number: {billno5}')
        bil5.write(f'\n                     {tabv}\n')
        bil5.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil5.write(f'Order Details for {tabv} : \n')
        bil5.write('\n=======================================================================')
        bil5.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil5.write('\n=======================================================================')

        def hidew5():
            item5.withdraw()

        hideb5 = Button(item5, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew5)
        hideb5.place(x=50, y=610)
        fin5 = Button(item5, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini5(), genbill5()])
        fin5.place(x=800, y=610)

        F1 = LabelFrame(item5, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname5
            global pno5
            cname5 = c_name.get()
            pno5 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno5}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname5}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno5}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm5():
            global bt
            global l5
            global apy5
            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()

            if cb1 != 0:
                k5 = open(blk5, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k5.write(f'\n{it1}\t\t{sb1}')
                bil5.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l5.append(m)
            if cb2 != 0:
                k5 = open(blk5, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k5.write(f'\n{it2}\t{sb2}')
                bil5.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l5.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k5 = open(blk5, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k5.write(f'\n{it3}\t\t{sb3}')
                bil5.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l5.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k5 = open(blk5, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k5.write(f'\n{it4}\t{sb4}')
                bil5.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l5.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k5.write(f'\n{it5}\t\t{sb5}')
                bil5.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l5.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k5.write(f'\n{it6}\t\t{sb6}')
                bil5.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l5.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k5.write(f'\n{it7}\t{sb7}')
                bil5.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l5.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k5.write(f'\n{it8}\t{sb8}')
                bil5.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l5.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k5.write(f'\n{it9}\t{sb9}')
                bil5.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l5.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k5.write(f'\n{it10}\t{sb10}')
                bil5.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l5.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k5.write(f'\n{it11}\t\t{sb11}')
                bil5.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l5.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k5.write(f'\n{it12}\t{sb12}')
                bil5.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l5.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k5.write(f'\n{it13}\t{sb13}')
                bil5.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l5.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k5 = open(blk5, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k5.write(f'\n{it14}\t{sb14}')
                bil5.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l5.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k5 = open(blk5, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k5.write(f'\n{it15}\t{sb15}')
                bil5.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l5.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k5 = open(blk5, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k5.write(f'\n{it16}\t\t{sb16}')
                bil5.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l5.append(m)

            apy5 = sum(l5)
            amtpy = Label(item5, text='Amount Payable: ' + str(apy5) + ' + Tax: ' + str(apy5 + (apy5 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',
                          fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k5.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item5, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item5, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm5)
        btn1.place(x=300, y=610)
        clr = Button(item5, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item5.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(item5, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item5, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item5, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item5, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item5, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item5, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item5, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item5, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item5, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item5, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item5, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item5, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item5, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item5, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item5, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item5, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item5, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item5.mainloop()

    def itemmenu6():
        cname6 = 'Walk Inn Customer'
        pno6='NA'
        global l6
        l6 = []
        global item6
        global tabv
        global bt
        bt = 1
        item6 = Toplevel()
        item6.title(tabv)
        item6.geometry('1366x700')
        item6.config(bg='deep sky blue')

        def genbill6():
            global cname6
            global pno6
            k6 = open(blk6, 'a')
            k6.write(f'\n\n\n***** Order closed for {billno6} *******')
            k6.close()

            fbill6 = apy6 + (apy6 * .05)

            bil6.write('\n=======================================================================')
            bil6.write(f'\n\n        Total Amount = {apy6} + 5% GST({apy6 * .05})')
            bil6.write(f'\n\n                Total Amount= {fbill6}')
            bil6.write('\n\n               Thank You! Visit Again!!')
            bil6.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg6.rstrip('.txt'), staffname, cname6, pno6, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill6)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk6 = time.strftime("%Y%m%d%I%M%S")
        blk6 = 'k' + blk6 + '.txt'
        k6 = open(blk6, 'a')
        k6.write(f'{tabv}\n')
        k6.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k6.write(f'Order Details for {tabv} : \n')
        k6.close()

        blg6 = time.strftime("%Y%m%d%I%M%S")
        blg6 = blg6 + '.txt'
        bil6 = open(blg6, 'a')
        bil6.write('                  The Lassi Corner \n')
        bil6.write('                      K.K.Nagar \n')
        bil6.write('                  Ph: 9852415687 \n')
        bil6.write(f'                  Staffname: {staffname}  \n       ')
        bil6.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil6.write(f'\n            Bill Number: {billno6}')
        bil6.write(f'\n                     {tabv}\n')
        bil6.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil6.write(f'Order Details for {tabv} : \n')
        bil6.write('\n=======================================================================')
        bil6.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil6.write('\n=======================================================================')

        def hidew6():
            item6.withdraw()

        hideb6 = Button(item6, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidew6)
        hideb6.place(x=50, y=610)
        fin6 = Button(item6, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [fini6(), genbill6()])
        fin6.place(x=800, y=610)

        F1 = LabelFrame(item6, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname6
            global pno6
            cname6 = c_name.get()
            pno6 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billno6}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname6}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno6}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm6():
            global bt
            global apy6
            global l6
            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()

            if cb1 != 0:
                k6 = open(blk6, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k6.write(f'\n{it1}\t\t{sb1}')
                bil6.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l6.append(m)
            if cb2 != 0:
                k6 = open(blk6, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k6.write(f'\n{it2}\t{sb2}')
                bil6.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l6.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k6 = open(blk6, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k6.write(f'\n{it3}\t\t{sb3}')
                bil6.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l6.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k6 = open(blk6, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k6.write(f'\n{it4}\t{sb4}')
                bil6.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l6.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k6.write(f'\n{it5}\t\t{sb5}')
                bil6.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l6.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k6.write(f'\n{it6}\t\t{sb6}')
                bil6.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l6.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k6.write(f'\n{it7}\t{sb7}')
                bil6.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l6.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k6.write(f'\n{it8}\t{sb8}')
                bil6.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l6.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k6.write(f'\n{it9}\t{sb9}')
                bil6.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l6.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k6.write(f'\n{it10}\t{sb10}')
                bil6.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l6.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k6.write(f'\n{it11}\t\t{sb11}')
                bil6.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l6.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k6.write(f'\n{it12}\t{sb12}')
                bil6.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l6.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k6.write(f'\n{it13}\t{sb13}')
                bil6.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l6.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k6 = open(blk6, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k6.write(f'\n{it14}\t{sb14}')
                bil6.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l6.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k6 = open(blk6, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k6.write(f'\n{it15}\t{sb15}')
                bil6.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l6.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k6 = open(blk6, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k6.write(f'\n{it16}\t\t{sb16}')
                bil6.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l6.append(m)

            apy6 = sum(l6)
            amtpy = Label(item6, text='Amount Payable: ' + str(apy6) + ' + Tax: ' + str(apy6 + (apy6 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',
                          fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k6.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(item6, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(item6, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm6)
        btn1.place(x=300, y=610)
        clr = Button(item6, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        item6.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(item6, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(item6, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(item6, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(item6, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(item6, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(item6, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(item6, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(item6, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(item6, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(item6, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(item6, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(item6, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(item6, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(item6, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(item6, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(item6, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(item6, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        item6.mainloop()

    def takeaway():
        cname7 = 'Walk Inn Customer'
        pno7='NA'
        global l7
        l7 = []
        global takey
        global tabv
        global bt
        bt = 1
        takey = Toplevel()
        takey.title(tabv)
        takey.geometry('1366x700')
        takey.config(bg='deep sky blue')

        def genbill7():
            global cname7
            global pno7
            k7 = open(blk7, 'a')
            k7.write(f'\n\n\n***** Order closed for {billnot} *******')
            k7.close()

            fbill7 = apy7 + (apy7 * .05)

            bil7.write('\n=======================================================================')
            bil7.write(f'\n\n        Total Amount = {apy7} + 5% GST({apy7 * .05})')
            bil7.write(f'\n\n                Total Amount= {fbill7}')
            bil7.write('\n\n               Thank You! Visit Again!!')
            bil7.close()

            dbc = pymysql.connect(host='localhost', user='root', passwd='', db='restaurant')
            curc = dbc.cursor()
            lsst = (
            blg7.rstrip('.txt'), staffname, cname7, pno7, time.strftime('%d,%b,%y'), time.strftime('%I:%M:%S %p'),
            fbill7)
            ins = 'insert into orderdet values(%s,%s,%s,%s,%s,%s,%s)'
            curc.execute(ins, lsst)
            dbc.close()

        blk7 = time.strftime("%Y%m%d%I%M%S")
        blk7 = 'k' + blk7 + '.txt'
        k7 = open(blk7, 'a')
        k7.write(f'{tabv}\n')
        k7.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        k7.write(f'Order Details for {tabv} : \n')
        k7.close()

        blg7 = time.strftime("%Y%m%d%I%M%S")
        blg7 = blg7 + '.txt'
        bil7 = open(blg7, 'a')
        bil7.write('                  The Lassi Corner \n')
        bil7.write('                      K.K.Nagar \n')
        bil7.write('                  Ph: 9852415687 \n')
        bil7.write(f'                  Staffname: {staffname}  \n       ')
        bil7.write(f'     Date/Time: {time.strftime("%d,%b,%Y / %I:%M:%S %p")}')
        bil7.write(f'\n            Bill Number: {billnot}')
        bil7.write(f'\n                     {tabv}\n')
        bil7.write(f'Order time: {time.strftime("%I:%M:%S %p")}\n')
        bil7.write(f'Order Details for {tabv} : \n')
        bil7.write('\n=======================================================================')
        bil7.write(f'\n  Product\t\t\tPrice\tQTY\t  Total')
        bil7.write('\n=======================================================================')

        def hidewt():
            takey.withdraw()

        hidebt = Button(takey, text='Hide Window', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                        command=hidewt)
        hidebt.place(x=50, y=610)
        fint = Button(takey, text='Finish', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=lambda: [finiwt(), genbill7()])
        fint.place(x=800, y=610)

        F1 = LabelFrame(takey, text='Customer Details', font=('times new rommon', 18), bg='steel blue')
        F1.place(x=0, y=0, relwidth=1)

        c_name = StringVar(value='Walk in Customer')
        c_phone = StringVar(value='NA')

        cname_lbl = Label(F1, text='Customer Name', font=('times new rommon', 18))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone NO', font=('times new rommon', 18))
        cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15', relief=SUNKEN, textvariable=c_phone)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        def basictext():
            global cname7
            global pno7
            cname7 = c_name.get()
            pno7 = c_phone.get()
            textarea.insert(END, f'Bill Number: {billnot}')
            textarea.insert(END, f'\n Customer Name:\t\t{cname7}')
            textarea.insert(END, f'\n Phone Number:\t\t{pno7}')
            textarea.insert(END, f'\n Date / Time: {time.strftime("%d,%B,%Y / %I:%M:%S %p")}\t\t')
            textarea.insert(END, f'\n======================================================')
            textarea.insert(END, f'\n Product\t\t\t Price\t\t QTY \t Total')
            textarea.insert(END, f'\n======================================================\n')
            textarea.configure(font='arial 12 bold')

        def additm7():
            global apy7
            global bt
            global l7
            global takey

            if bt == 1:
                basictext()
                bt = 2

            cb2 = CheckVar2.get()
            cb3 = CheckVar3.get()
            cb4 = CheckVar4.get()
            cb5 = CheckVar5.get()
            cb6 = CheckVar6.get()
            cb7 = CheckVar7.get()
            cb8 = CheckVar8.get()
            cb9 = CheckVar9.get()
            cb10 = CheckVar10.get()
            cb11 = CheckVar11.get()
            cb12 = CheckVar12.get()
            cb13 = CheckVar13.get()
            cb14 = CheckVar14.get()
            cb15 = CheckVar15.get()
            cb16 = CheckVar16.get()
            cb1 = CheckVar1.get()

            if cb1 != 0:
                k7 = open(blk7, 'a')
                sb1 = int(wvar1.get())
                m = cb1 * sb1
                textarea.insert(END, f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t{m}')
                k7.write(f'\n{it1}\t\t{sb1}')
                bil7.write(f'\n{it1}\t\t\t{cb1}\t\t{sb1}\t\t{m}')
                l7.append(m)
            if cb2 != 0:
                k7 = open(blk7, 'a')
                sb2 = int(wvar2.get())
                m = cb2 * sb2
                textarea.insert(END, f'\n{it2}\t\t\t{cb2}\t\t{sb2}\t{m}')
                k7.write(f'\n{it2}\t{sb2}')
                bil7.write(f'\n{it2}\t{cb2}\t\t{sb2}\t\t{m}')
                l7.append(m)
            if cb3 != 0:
                sb3 = int(wvar3.get())
                k7 = open(blk7, 'a')
                m = cb3 * sb3
                textarea.insert(END, f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t{m}')
                k7.write(f'\n{it3}\t\t{sb3}')
                bil7.write(f'\n{it3}\t\t\t{cb3}\t\t{sb3}\t\t{m}')
                l7.append(m)
            if cb4 != 0:
                sb4 = int(wvar4.get())
                k7 = open(blk7, 'a')
                m = cb4 * sb4
                textarea.insert(END, f'\n{it4}\t\t\t{cb4}\t\t{sb4}\t{m}')
                k7.write(f'\n{it4}\t{sb4}')
                bil7.write(f'\n{it4}\t\t{cb4}\t\t{sb4}\t\t{m}')
                l7.append(m)
            if cb5 != 0:
                sb5 = int(wvar5.get())
                m = cb5 * sb5
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t{m}')
                k7.write(f'\n{it5}\t\t{sb5}')
                bil7.write(f'\n{it5}\t\t\t{cb5}\t\t{sb5}\t\t{m}')
                l7.append(m)
            if cb6 != 0:
                sb6 = int(wvar6.get())
                m = cb6 * sb6
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t{m}')
                k7.write(f'\n{it6}\t\t{sb6}')
                bil7.write(f'\n{it6}\t\t\t{cb6}\t\t{sb6}\t\t{m}')
                l7.append(m)
            if cb7 != 0:
                sb7 = int(wvar7.get())
                m = cb7 * sb7
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it7}\t\t\t{cb7}\t\t{sb7}\t{m}')
                k7.write(f'\n{it7}\t{sb7}')
                bil7.write(f'\n{it7}\t\t{cb7}\t\t{sb7}\t\t{m}')
                l7.append(m)
            if cb8 != 0:
                sb8 = int(wvar8.get())
                m = cb8 * sb8
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it8}\t\t\t{cb8}\t\t{sb8}\t{m}')
                k7.write(f'\n{it8}\t{sb8}')
                bil7.write(f'\n{it8}\t\t{cb8}\t\t{sb8}\t\t{m}')
                l7.append(m)
            if cb9 != 0:
                sb9 = int(wvar9.get())
                m = cb9 * sb9
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it9}\t\t\t{cb9}\t\t{sb9}\t{m}')
                k7.write(f'\n{it9}\t{sb9}')
                bil7.write(f'\n{it9}\t\t{cb9}\t\t{sb9}\t\t{m}')
                l7.append(m)
            if cb10 != 0:
                sb10 = int(wvar10.get())
                m = cb10 * sb10
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it10}\t\t\t{cb10}\t\t{sb10}\t{m}')
                k7.write(f'\n{it10}\t{sb10}')
                bil7.write(f'\n{it10}\t\t{cb10}\t\t{sb10}\t\t{m}')
                l7.append(m)
            if cb11 != 0:
                sb11 = int(wvar11.get())
                m = cb11 * sb11
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t{m}')
                k7.write(f'\n{it11}\t\t{sb11}')
                bil7.write(f'\n{it11}\t\t\t{cb11}\t\t{sb11}\t\t{m}')
                l7.append(m)
            if cb12 != 0:
                sb12 = int(wvar12.get())
                m = cb12 * sb12
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it12}\t\t\t{cb12}\t\t{sb12}\t{m}')
                k7.write(f'\n{it12}\t{sb12}')
                bil7.write(f'\n{it12}\t\t{cb12}\t\t{sb12}\t\t{m}')
                l7.append(m)
            if cb13 != 0:
                sb13 = int(wvar13.get())
                m = cb13 * sb13
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it13}\t\t\t{cb13}\t\t{sb13}\t{m}')
                k7.write(f'\n{it13}\t{sb13}')
                bil7.write(f'\n{it13}\t\t{cb13}\t\t{sb13}\t\t{m}')
                l7.append(m)
            if cb14 != 0:
                sb14 = int(wvar14.get())
                m = cb14 * sb14
                k7 = open(blk7, 'a')
                textarea.insert(END, f'\n{it14}\t\t\t{cb14}\t\t{sb14}\t{m}')
                k7.write(f'\n{it14}\t{sb14}')
                bil7.write(f'\n{it14}\t{cb14}\t\t{sb14}\t\t{m}')
                l7.append(m)
            if cb15 != 0:
                sb15 = int(wvar15.get())
                k7 = open(blk7, 'a')
                m = cb15 * sb15
                textarea.insert(END, f'\n{it15}\t\t\t{cb15}\t\t{sb15}\t{m}')
                k7.write(f'\n{it15}\t{sb15}')
                bil7.write(f'\n{it15}\t{cb15}\t\t{sb15}\t\t{m}')
                l7.append(m)
            if cb16 != 0:
                sb16 = int(wvar16.get())
                k7 = open(blk7, 'a')
                m = cb16 * sb16
                textarea.insert(END, f'\n{it16}\t\t\t{cb16}\t\t{sb16}\t{m}')
                k7.write(f'\n{it16}\t\t{sb16}')
                bil7.write(f'\n{it16}\t\t{cb16}\t\t{sb16}\t\t{m}')
                l7.append(m)

            apy7 = sum(l7)
            amtpy = Label(takey, text='Amount Payable: ' + str(apy7) + ' + Tax: ' + str(apy7 + (apy7 * .05)),
                          font=('times new rommon', 18, 'bold',), bg='white',
                          fg='black')
            amtpy.place(x=940, y=610)
            clearall()
            k7.close()

        def clearall():
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            CheckVar6.set(0)
            CheckVar7.set(0)
            CheckVar8.set(0)
            CheckVar9.set(0)
            CheckVar10.set(0)
            CheckVar11.set(0)
            CheckVar12.set(0)
            CheckVar13.set(0)
            CheckVar14.set(0)
            CheckVar15.set(0)
            CheckVar16.set(0)

            wvar1.set('0')
            wvar2.set('0')
            wvar3.set('0')
            wvar4.set('0')
            wvar5.set('0')
            wvar6.set('0')
            wvar7.set('0')
            wvar8.set('0')
            wvar9.set('0')
            wvar10.set('0')
            wvar11.set('0')
            wvar12.set('0')
            wvar13.set('0')
            wvar14.set('0')
            wvar15.set('0')
            wvar16.set('0')

        wvar1 = StringVar()
        wvar2 = StringVar()
        wvar3 = StringVar()
        wvar4 = StringVar()
        wvar5 = StringVar()
        wvar6 = StringVar()
        wvar7 = StringVar()
        wvar8 = StringVar()
        wvar9 = StringVar()
        wvar10 = StringVar()
        wvar11 = StringVar()
        wvar12 = StringVar()
        wvar13 = StringVar()
        wvar14 = StringVar()
        wvar15 = StringVar()
        wvar16 = StringVar()

        w1 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar1)
        w1.place(x=230, y=170)
        w2 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar2)
        w2.place(x=230, y=220)
        w3 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar3)
        w3.place(x=230, y=270)
        w4 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar4)
        w4.place(x=230, y=320)
        w5 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar5)
        w5.place(x=230, y=370)
        w6 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar6)
        w6.place(x=230, y=420)
        w7 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar7)
        w7.place(x=230, y=470)
        w8 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar8)
        w8.place(x=580, y=170)
        w9 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar9)
        w9.place(x=580, y=220)
        w10 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar10)
        w10.place(x=580, y=270)
        w11 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar11)
        w11.place(x=580, y=320)
        w12 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar12)
        w12.place(x=580, y=370)
        w13 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar13)
        w13.place(x=580, y=420)
        w14 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar14)
        w14.place(x=580, y=470)
        w15 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar15)
        w15.place(x=580, y=520)
        w16 = Spinbox(takey, from_=0, to=20, width=5, textvariable=wvar16)
        w16.place(x=230, y=520)

        btn1 = Button(takey, text='Add items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                      command=additm7)
        btn1.place(x=300, y=610)
        clr = Button(takey, text='Clear items', font='arial 15 bold', padx=5, pady=5, bg='snow3', width=10,
                     command=clearall)
        clr.place(x=550, y=610)

        def __CancelCommand(event=None):
            pass

        takey.protocol('WM_DELETE_WINDOW', __CancelCommand)

        F3 = Frame(takey, relief=GROOVE, bd=10)
        F3.place(x=800, y=0, width=560, height=600)
        bill_title = Label(F3, text='Bill Area', font='arial 15 bold', relief=GROOVE, bd=7)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        textarea = Text(F3, yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=textarea.yview)
        textarea.pack(expand=True, fill=BOTH)

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()
        CheckVar8 = IntVar()
        CheckVar9 = IntVar()
        CheckVar10 = IntVar()
        CheckVar11 = IntVar()
        CheckVar12 = IntVar()
        CheckVar13 = IntVar()
        CheckVar14 = IntVar()
        CheckVar15 = IntVar()
        CheckVar16 = IntVar()

        it1 = 'Sweet Lassi'
        C1 = Checkbutton(takey, text=it1, variable=CheckVar1, onvalue=40, height=2, width=20)

        it2 = "Mango Banana Lassi"
        C2 = Checkbutton(takey, text=it2, variable=CheckVar2, onvalue=50, offvalue=0, height=2,
                         width=20)
        it3 = "Fruit Lassi"
        C3 = Checkbutton(takey, text=it3, variable=CheckVar3, onvalue=55, offvalue=0, height=2, width=20)
        it4 = "Dry fruit lassi"
        C4 = Checkbutton(takey, text=it4, variable=CheckVar4, onvalue=60, offvalue=0, height=2, width=20)
        it5 = "Mango Lassi"
        C5 = Checkbutton(takey, text=it5, variable=CheckVar5, onvalue=45, offvalue=0, height=2, width=20)
        it6 = "Mud coffee"
        C6 = Checkbutton(takey, text=it6, variable=CheckVar6, onvalue=70, offvalue=0, height=2, width=20)
        it7 = "Belgian coffee"
        C7 = Checkbutton(takey, text=it7, variable=CheckVar7, onvalue=75, offvalue=0, height=2, width=20)
        it8 = "Ferrero coffee"
        C8 = Checkbutton(takey, text=it8, variable=CheckVar8, onvalue=90, offvalue=0, height=2, width=20)
        it9 = "Mexican brownie"
        C9 = Checkbutton(takey, text=it9, variable=CheckVar9, onvalue=60, offvalue=0, height=2, width=20)
        it10 = "Chocolate fudge"
        C10 = Checkbutton(takey, text=it10, variable=CheckVar10, onvalue=65, offvalue=0, height=2, width=20)
        it11 = "Lava cake"
        C11 = Checkbutton(takey, text=it11, variable=CheckVar11, onvalue=90, offvalue=0, height=2, width=20)
        it12 = "Dryfruit sundae"
        C12 = Checkbutton(takey, text=it12, variable=CheckVar12, onvalue=110, offvalue=0, height=2,
                          width=20)
        it13 = "Nutella Lychees"
        C13 = Checkbutton(takey, text=it13, variable=CheckVar13, onvalue=100, offvalue=0, height=2,
                          width=20)
        it14 = "Butter Scotch fudge"
        C14 = Checkbutton(takey, text=it14, variable=CheckVar14, onvalue=95, offvalue=0, height=2,
                          width=20)
        it15 = "Choco nut sundae"
        C15 = Checkbutton(takey, text=it15, variable=CheckVar15, onvalue=105, offvalue=0, height=2,
                          width=20)
        it16 = "Turkish Coffee"
        C16 = Checkbutton(takey, text=it16, variable=CheckVar16, onvalue=50, offvalue=0, height=2, width=20)

        C1.place(x=50, y=160)
        C2.place(x=50, y=210)
        C3.place(x=50, y=260)
        C4.place(x=50, y=310)
        C5.place(x=50, y=360)
        C6.place(x=50, y=410)
        C7.place(x=50, y=460)
        C8.place(x=400, y=160)
        C9.place(x=400, y=210)
        C10.place(x=400, y=260)
        C11.place(x=400, y=310)
        C12.place(x=400, y=360)
        C13.place(x=400, y=410)
        C14.place(x=400, y=460)
        C15.place(x=400, y=510)
        C16.place(x=50, y=510)

        takey.mainloop()

    def fini1():
        btn1.configure(state=NORMAL)
        btn1.config(bg='yellow')
        item1.destroy()

    def fini2():
        btn2.configure(state=NORMAL)
        btn2.config(bg='yellow')
        item2.destroy()

    def fini3():
        btn3.configure(state=NORMAL)
        btn3.config(bg='yellow')
        item3.destroy()

    def fini4():
        btn4.configure(state=NORMAL)
        btn4.config(bg='yellow')
        item4.destroy()

    def fini5():
        btn5.configure(state=NORMAL)
        btn5.config(bg='yellow')
        item5.destroy()

    def fini6():
        btn6.configure(state=NORMAL)
        btn6.config(bg='yellow')
        item6.destroy()

    def finiwt():
        btn7.configure(state=NORMAL)
        btn7.config(bg='yellow')
        takey.destroy()

    def tab1():
        global billno1
        billno1 = time.strftime("%Y%m%d%I%M%S")
        btn1.config(bg='black')
        global tabv
        tabv = 'Table 1'
        btn1.configure(state=DISABLED)

    def tab2():
        global tabv
        global billno2
        tabv = 'Table 2'
        billno2 = time.strftime("%Y%m%d%I%M%S")
        btn2.config(bg='black')
        btn2.configure(state=DISABLED)

    def tab3():
        global tabv
        global billno3
        billno3 = time.strftime("%Y%m%d%I%M%S")
        tabv = 'Table 3'
        btn3.config(bg='black')
        btn3.configure(state=DISABLED)

    def tab4():
        global tabv
        global billno4
        tabv = 'Table 4'
        billno4 = time.strftime("%Y%m%d%I%M%S")
        btn4.config(bg='black')
        btn4.configure(state=DISABLED)

    def tab5():
        global tabv
        global billno5
        tabv = 'Table 5'
        billno5 = time.strftime("%Y%m%d%I%M%S")
        btn5.config(bg='black')
        btn5.configure(state=DISABLED)

    def tab6():
        global billno6
        global tabv
        tabv = 'Table 6'
        billno6 = time.strftime("%Y%m%d%I%M%S")
        btn6.config(bg='black')
        btn6.configure(state=DISABLED)

    def take():
        global tabv
        global billnot
        tabv = 'Takeaway'
        billnot = time.strftime("%Y%m%d%I%M%S")
        btn7.config(bg='black')
        btn7.configure(state=DISABLED)

    btn1 = Button(text='Table 1', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab1(), itemmenu1()])
    btn1.place(x=300, y=350)

    def doubleclick1(event):
        item1.deiconify()

    def doubleclick2(event):
        item2.deiconify()

    def doubleclick3(event):
        item3.deiconify()

    def doubleclick4(event):
        item4.deiconify()

    def doubleclick5(event):
        item5.deiconify()

    def doubleclick6(event):
        item6.deiconify()

    def doubleclick7(event):
        takey.deiconify()

    def over():
        tab.destroy()
        quit()

    def __CancelCommand(event=None):
        pass

    tab.protocol('WM_DELETE_WINDOW', __CancelCommand)

    btn1.bind('<Double 1>', doubleclick1)
    btn2 = Button(text='Table 2', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab2(), itemmenu2()])
    btn2.place(x=600, y=350)

    btn3 = Button(text='Table 3', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab3(), itemmenu3()])
    btn3.place(x=900, y=350)

    btn4 = Button(text='Table 4', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab4(), itemmenu4()])
    btn4.place(x=300, y=500)

    btn5 = Button(text='Table 5', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab5(), itemmenu5()])
    btn5.place(x=600, y=500)

    btn6 = Button(text='Table 6', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=10,
                  command=lambda: [tab6(), itemmenu6()])
    btn6.place(x=900, y=500)

    btn7 = Button(text='Takeaway', font='arial 15 bold', padx=5, pady=5, bg='yellow', width=50,
                  command=lambda: [take(), takeaway()])
    btn7.place(x=350, y=600)

    btn8 = Button(text='Log Out', padx=5, width=10, command=over)
    btn8.place(x=1280, y=0)

    btn2.bind('<Double 1>', doubleclick2)
    btn3.bind('<Double 1>', doubleclick3)
    btn4.bind('<Double 1>', doubleclick4)
    btn5.bind('<Double 1>', doubleclick5)
    btn6.bind('<Double 1>', doubleclick6)
    btn7.bind('<Double 1>', doubleclick7)
    tab.mainloop()

if __name__ == '__main__':
    mainlogin()
    if passv==1:
        restop()