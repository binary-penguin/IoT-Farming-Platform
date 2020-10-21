from PIL import Image, ImageTk
import tkinter as tk


class BkgrFrame(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        self.pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(self.pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def add(self, widget, x, y, justify):
        self.canvas.create_window(x, y, anchor=tk.NW, window=widget, justify = justify)
        return widget




# Put some tkinter widgets in the BkgrFrame.
button1 = bkrgframe.add(tk.Button(root, text="Start"), 10, 10)
button2 = bkrgframe.add(tk.Button(root, text="Continue"), 50, 10)

root.mainloop()