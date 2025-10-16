from tkinter import*

w = Canvas(Tk(), width=900, height=400)
w.pack()

collarpallet = ["#ff0000","#00ff00","#0000ff","#ffff00","#00ffff","#000000"]
for i in range(100):
    x = i * 9
    line = 400
    
    if i % 3 == 0:
        line = 200

    w.create_line(x, 0, x, line, fill=collarpallet[i%6])

mainloop()