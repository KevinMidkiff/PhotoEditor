from Tkinter import *
import PIL

from photo_editor.image import Image


def main():
    master = Tk()

    master.geometry('{}x{}'.format(750, 500))

    img = Image('C:\\_Data\\Pictures\\christmas_present_pictures\\MidkiffP.jpg')

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
    photo = PIL.ImageTk.PhotoImage(image=pil_image)

    cont_lbl = Label(content_pane, image=photo)  # text='Content Pane')
    content_pane.add(cont_lbl)

    mainloop()


if __name__ == '__main__':
    main()
