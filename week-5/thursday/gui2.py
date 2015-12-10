from tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()


for i in range(50):
    ox = 10 * i
    w.create_line(0, -10 + ox, 500 - ox, 0, width=0.5, fill='#000000')
    w.create_line(500, 0 + ox, 500 - ox, 500, width=0.5, fill='#000000')
    w.create_line(0, 0 + ox, 0 + ox, 500, width=0.5, fill='#000000')
    w.create_line(500-ox, 0 , 500,  500-ox, width=0.5, fill='#000000')


for i in range(25):
    ox = 10 * i
    #w.create_line(0, 0 + ox, 250 - ox, 0, width=0.5, fill='#ff00f0')
    w.create_line(250, 0 + ox, 250 - ox, 250, width=0.5, fill='#00ff0f')
    #w.create_line(0, 0 + ox, 0 + ox, 250, width=0.5, fill='#ff00f0')
    #w.create_line(250-ox, 0 , 250,  250-ox, width=0.5, fill='#ff00f0')

for i in range(25):
    ox = 10 * i
    w.create_line(250, 240 + ox, 500 - ox, 250, width=0.5, fill='#00ff0f')
    #w.create_line(500, 250 + ox, 500 - ox, 500, width=0.5, fill='#ff00f0')
    #w.create_line(250, 250 + ox, 250 + ox, 500, width=0.5, fill='#ff00f0')
    #w.create_line(500-ox, 250 , 500,  500-ox, width=0.5, fill='#ff00f0')

for i in range(26):
    ox = 10 * i
    #w.create_line(0, 250 + ox, 250 - ox, 250, width=0.5, fill='#ff00f0')
    #w.create_line(250, 250 + ox, 250 - ox, 500, width=0.5, fill='#ff00f0')
    #w.create_line(0, 250 + ox, 0 + ox, 500, width=0.5, fill='#ff00f0')
    w.create_line(250-ox, 250 , 250,  500-ox, width=0.5, fill='#00ff0f')

for i in range(25):
    ox = 10 * i
    #w.create_line(250, 0 + ox, 500 - ox, 0, width=0.5, fill='#ff00f0')
    #w.create_line(500, 0 + ox, 500 - ox, 250, width=0.5, fill='#ff00f0')
    w.create_line(250, 0 + ox, 250 + ox, 250, width=0.5, fill='#00ff0f')
    #w.create_line(250-ox, 0 , 250,  250-ox, width=0.5, fill='#ff00f0')



mainloop()
