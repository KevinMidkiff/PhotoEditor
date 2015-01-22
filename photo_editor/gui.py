import os
from Tkinter import *
from tkFileDialog import *
import tkMessageBox as tkMb
import PIL.Image
import PIL.ImageTk

from photo_editor.image import Image
from photo_editor import filters


class GUI(object):
    """
    GUI Class
    """
    def __init__(self):
        """
        GUI Constructor
        """
        self.master = Tk()

        self.master.wm_title('Photo Editor')

        self.img = None
        self.pil_image = None
        self.photo = None
        self.showing = None

        self.master.geometry('{}x{}'.format(850, 500))

        # Adding in the file menu
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Open Image', command=self.select_picture)
        self.filemenu.add_command(label='Save Image', command=self.save_image)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit') # Add Command
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        # Adding edit menu
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label='Undo', command=self.undo)
        self.editmenu.add_command(label='Reset', command=self.reset)
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)

        self.master.config(menu=self.menubar)
        # ------

        self.actions_pane = PanedWindow(self.master)
        self.actions_pane.pack(fill=BOTH, expand=1)

        # init filter select
        self.filter_select_pane = PanedWindow(self.actions_pane, orient=VERTICAL)
        self.actions_pane.add(self.filter_select_pane)


        self.var = StringVar(self.master)
        self.var.trace_variable('w', self.select_filter)

        opts_frame = Frame(self.filter_select_pane)
        opts_frame.pack()

        self.filter_select_pane.add(opts_frame)

        self.filter_params_pane = PanedWindow(self.filter_select_pane)
        self.filter_select_pane.add(self.filter_params_pane)

        self.opts_vals = {
            'Gaussian Filter': filters.GaussianFilter(self.filter_params_pane, self.apply_filter),
            'Box Filter': filters.BoxFilter(self.filter_params_pane, self.apply_filter),
            'Median Filter': filters.MedianFilter(self.filter_params_pane, self.apply_filter),
            'Canny Edge Detector': filters.CannyEdgeDetector(self.filter_params_pane, self.apply_filter),
            'Bilateral Filter': filters.BilateralFilter(self.filter_params_pane, self.apply_filter),
            'Non-Local Means Filter': filters.NonLocalMeansColor(self.filter_params_pane, self.apply_filter),
            'Sobel Filter': filters.SobelFilter(self.filter_params_pane, self.apply_filter),
            'Laplacian Filter': filters.LaplacianFilter(self.filter_params_pane, self.apply_filter)}

        self.opts = OptionMenu(opts_frame, self.var, *self.opts_vals.keys())
        self.opts.pack()

        self.var.set(self.opts_vals.keys()[0])

        self.content_pane = PanedWindow(self.actions_pane, orient=VERTICAL)
        self.actions_pane.add(self.content_pane)

        self.cont_lbl = Label(self.content_pane, text='No image selected')# image=self.photo)
        self.cont_lbl.place(x=0, y=0, width=750, height=750)
        self.cont_lbl.grid()
        self.content_pane.add(self.cont_lbl)

    def main(self):
        self.master.mainloop()

    def select_filter(self, *args):
        if self.showing is not None:
            self.opts_vals[self.showing].tk_hide()

        self.showing = self.var.get()
        self.reset()
        self.opts_vals[self.var.get()].tk_show()

    def select_picture(self):
        filename = askopenfilename(parent=self.master)

        if filename != '':
            if os.path.exists(filename):
                self.img = Image(filename)
                self.update_picture()
            else:
                tkMb.showinfo('ERROR', '"{0}" does not exist'.format(filename))

    def update_picture(self):
        self.pil_image = PIL.Image.fromarray(self.img.image)
        self.photo = PIL.ImageTk.PhotoImage(image=self.pil_image)
        self.cont_lbl.configure(text='', image=self.photo)

    def save_image(self):
        outfilename = asksaveasfilename(parent=self.master)
        self.img.save(outfilename)

    def apply_filter(self, img_filter):
        if self.img is not None:
            self.img.apply_filter(img_filter)
            self.update_picture()

    def undo(self):
        if self.img is not None:
            self.img.undo()
            self.update_picture()

    def reset(self):
        if self.img is not None:
            self.img.reset()
            self.update_picture()


if __name__ == '__main__':
    main()
