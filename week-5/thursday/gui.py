from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=300)
w.pack()

for j in range(4):
    for i in range(4):
        ox = 40 * i
        oj = 40 * j
        w.create_rectangle(0 + ox, 0 + oj, 20 + ox, 20 + oj, fill='#000000')
        w.create_rectangle(20 + ox, 20 + oj, 40 +ox, 40 + oj, fill='#000000')

for j in range(4):
   for i in range(4):
       ox = i*40
       oy = j * 40
       w.create_rectangle(0+ox,0+oy,20+ox,20+oy, fill="#ff0000 ")
       w.create_rectangle(20+ox,20+oy,40+ox,40+oy, fill="#ff0000 ")


mainloop()

#w.create_rectangle(0, 0, 400, 300, fill='#ffffff')
#w.create_rectangle(0, 0, 20, 20, fill='#ff0000')
#w.create_rectangle(20, 20, 40, 40, fill='#ff0000')
#w.create_rectangle(40, 0, 60, 20, fill='#ff0000')
#w.create_rectangle(60, 20, 80, 40, fill='#ff0000')

#w.create_rectangle(0, 40, 20, 60, fill='#ff0000')
#w.create_rectangle(40, 40, 40, 40, fill='#ff0000')
#w.create_rectangle(40, 40, 60, 60, fill='#ff0000')
#w.create_rectangle(60, 20, 80, 40, fill='#ff0000')

#w.create_rectangle(20, 60, 40, 80, fill='#ff0000')
#w.create_rectangle(60, 60, 80, 80, fill='#ff0000')
#w.create_rectangle(40, 40, 60, 60, fill='#ff0000')
#w.create_rectangle(60, 20, 80, 40, fill='#ff0000')

mainloop()
