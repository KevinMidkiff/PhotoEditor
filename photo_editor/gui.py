from Tkinter import *
import PIL

from photo_editor.image import Image


def main():
    master = Tk()

    master.geometry('{}x{}'.format(850, 500))

    # img = Image('opencv_orig_filter.jpg')
    img = Image('space-wallpapers-11.jpg')

    # init actions pane
    actions_pane = PanedWindow(master)
    actions_pane.pack(fill=BOTH, expand=1)
    # act_lbl = Label(actions_pane, text='Actions Pane')
    # actions_pane.add(act_lbl)

    # init filter select
    filter_select_pane = PanedWindow(actions_pane, orient=VERTICAL)
    actions_pane.add(filter_select_pane)


    opts_vals = ['Gaussian Filter', 'Box Filter']
    var = StringVar(master)
    var.set(opts_vals[0])
    opts = OptionMenu(filter_select_pane, var, *opts_vals) 
    opts.pack()

    filter_select_pane.add(opts)

    filter_params_pane = PanedWindow(filter_select_pane)
    filter_select_pane.add(filter_params_pane)
    tmp_lbl = Label(filter_params_pane, text='Actions Pane')
    filter_params_pane.add(tmp_lbl)


    # init content pane
    content_pane = PanedWindow(actions_pane, orient=VERTICAL)
    actions_pane.add(content_pane)

    # Loading image
    pil_image = PIL.Image.fromarray(img.image)
    pil_image.thumbnail((650, 500), PIL.Image.ANTIALIAS)

    photo = PIL.ImageTk.PhotoImage(image=pil_image)

    cont_lbl = Label(content_pane, image=photo)  # text='Content Pane')
    cont_lbl.place(x=0, y=0, width=750, height=750)
    cont_lbl.image = photo
    cont_lbl.grid()

    content_pane.add(cont_lbl)

    master.mainloop()


if __name__ == '__main__':
    main()
