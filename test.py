import tkinter as tk

root = tk.Tk()
root.geometry("1920x1080")
root.title(u'Full Screen to windows screen')
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda events: root.attributes('-fullscreen', False))
root.mainloop()