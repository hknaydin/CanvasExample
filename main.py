import Tkinter as tk
from Tkconstants import BOTH
from Tkconstants import HORIZONTAL, BOTTOM, X, VERTICAL, Y, BOTH, RIGHT, LEFT, ALL

root = tk.Tk()
root.geometry("800x800+200+200")
root.resizable(width=False, height=False)
root.title('Tkinter Widgets')
count = 100

def on_click():
    global  count
    canvas.create_text(50, count, text="HELLO Ilhan gggggggggggggggggggggggggggggggggggggggggggggggggggg: " + str(count), fill="black", font=('Helvetica 15 bold'))
    count = count + 180
    canvas.create_image((50, count), image=img1, tag="smile")
    height = img1.height()
    print ("image: ", height)
    count = count + height -150
    canvas.config(scrollregion=canvas.bbox(ALL))

    print (count)


img2 = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAACMAAAAjAQMAAAAkFyEaAAAABlBMVEUAAADw0gCjrW2CAAAAI0lEQVQI12NgQAL2////byCFPPihHg9JqmkHGOrxkHj1IgEAZH9nDhQLxPMAAAAASUVORK5CYII=")
img1 = tk.PhotoImage(file="neig.png")



canvas = tk.Canvas(root, bg='white', width=700, height=650)
canvas.place(relx=0.05, rely=0.05)

#canvas.create_image((200, count+100), image=img1, tag="smile")

scrollbar_neighbor = tk.Scrollbar(root)
#canvas.config(yscrollcommand=scrollbar_neighbor.set)
scrollbar_neighbor.place(relx=0.925, rely=0.05, width=20, height=650)
scrollbar_neighbor.config(command=canvas.yview)

scrollbar_message_x = tk.Scrollbar(root, orient=HORIZONTAL)
scrollbar_message_x.place(relx=0.05, rely=0.86, width=700, height=20)
scrollbar_message_x.config(command=canvas.xview)

canvas.config(yscrollcommand=scrollbar_neighbor.set, xscrollcommand=scrollbar_message_x.set)

button = tk.Button(root, text='CHANGE', command=on_click)
button.place(relx=0.45, rely=0.93, width=100, height=40)

canvas.mainloop()
root.mainloop()