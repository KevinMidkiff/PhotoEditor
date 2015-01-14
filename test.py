from photo_editor.filters import BoxFilter, GaussianFilter
from photo_editor.image import Image as PEImg
import numpy as np
from matplotlib import pyplot as plt

import Tkinter as Tk
from PIL import ImageTk, Image

from photo_editor import gui


def main():
    """
    Main Function
    """
    # img_name = 'space-wallpapers-11.jpg'
    img_name = 'opencv_orig_filter.jpg'
    img1 = PEImg(img_name)
    img2 = PEImg(img_name)
    bfilter = BoxFilter(ddepth=-1, ksize=(5, 5))
    gfilter = GaussianFilter((5,5), 5)
    img1.apply_filter(bfilter)
    img2.apply_filter(gfilter)
    # img = cv2.imread(img_name)
    # result = cv2.boxFilter(img, -1, (5, 5))
    # cv2.imwrite('opencv_box_filer.jpg', result)
    # print type(result)

    # plt.subplot(120),plt.imshow(img1.origonal),plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(121),plt.imshow(img1.image),plt.title('Box Filter')
    # plt.subplot(122),plt.imshow(img2.image),plt.title('Gaussian Filter')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    root = Tk.Tk()
    pil_image = Image.fromarray(img2.origonal)
    pil_image.thumbnail((750, 750), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image=pil_image)
    label = Tk.Label(root, image=photo)
    label.place(x=0, y=0, width=750, height=750)
    label.image = photo
    label.grid()
    # canvas = Tk.Canvas(root, width=750, height=750)
    # canvas.pack()
    # imagesprite = canvas.create_image(400, 400, image=image)
    root.mainloop()


def test_main():
    root = Tk.Tk()
    root.geometry('750x750')
    canvas = Tk.Canvas(root, width=750, height=750)
    canvas.pack()
    pilImage = Image.open('space-wallpapers-11.jpg')
    pilImage.thumbnail((750, 750), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(400, 400, image=image)
    root.mainloop()

if __name__ == '__main__':
    # main()  
    gui.main()
    # test_main()
