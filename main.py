import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

import numpy as np

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

t = np.linspace(0, 1)
y = np.sin(10*t)

lines = a.plot(t, y)

def animate(i):
    lines[0].set_data (t, np.sin(10*t + i/10))

class Window(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")
        self.master.configure(bg = "white")
        self.pack(fill=tk.BOTH, expand=1)

        quit_button = tk.Button(self, text = "Quit", command = self.client_exit)

        quit_button.place(x = 0, y = 0)

        #f = Figure(figsize=(5,5), dpi=100)
        #a = f.add_subplot(111)
        #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])



        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




    def client_exit(self):
        exit()

root = tk.Tk()

root["bg"] = "white"

root.geometry("400x300")

app = Window(root)

anim = FuncAnimation(f, animate, interval = 20)

root.mainloop()
