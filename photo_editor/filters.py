"""
Filters Module
"""
import cv2
from Tkinter import *

from .exceptions import BadFilterParams

class BaseFilter(object):
    """
    Base filter class
    """
    def __init__(self, tk_master, apply_func):
        """
        BaseFilter constructor

        Parameters to be set by subclasses
        """
        self.apply_func = lambda *args, **kwargs: apply_func(self)
        self.frame = Frame(tk_master)
        self.show_normal = False

    def filter(self, img):
        """
        Apply the filter to the given image.

        Parameters:
            img - The value returned by cv2.imread()
        """
        raise NotImplemented('filter() is unimplemented')

    def tk_show(self):
        """
        Show parameter options on the GUI
        """
        self.frame.pack()

    def tk_hide(self):
        """
        Remove from GUI
        """
        self.frame.pack_forget()


class BoxFilter(BaseFilter):
    """
    Box Filter Class
    """
    def __init__(self, tk_master, apply_func):
        """
        BoxFilter constructor
        """
        super(BoxFilter, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._ksize = Scale(self.frame, from_=1, to=15, label='Kernal Size', orient=HORIZONTAL,
                            command=self.apply_func)
        self._ksize.pack()

    @property
    def ksize(self):
        return self._ksize.get()

    @property
    def set_to_origonal(self):
        """
        Property to tell whether, given the parameters to the filter to set
        the image back to the original image.
        """
        return self.ksize == 1

    def filter(self, img):
        assert self.ksize % 2
        return cv2.boxFilter(img, -1, (self.ksize, self.ksize))


class GaussianFilter(BaseFilter):
    """
    GaussianFilter Class
    """
    def __init__(self, tk_master, apply_func):
        """
        GaussianFilter constructor
        """
        super(GaussianFilter, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._sigma = Scale(self.frame, from_=1, to=5, label='Sigma', orient=HORIZONTAL,
                            command=self.apply_func)
        self._sigma.pack()
        self._ksize = Scale(self.frame, from_=1, to=15, label='Kernal Size', orient=HORIZONTAL,
                            command=self.apply_func)
        self._ksize.pack()

    @property
    def ksize(self):
        return self._ksize.get()

    @property
    def sigma(self):
        return self._sigma.get()

    @property
    def set_to_origonal(self):
        """
        Property to tell whether, given the parameters to the filter to set
        the image back to the original image.
        """
        return self.ksize == 1

    def filter(self, img):
        assert self.ksize % 2
        return cv2.GaussianBlur(img, (self.ksize, self.ksize), self.sigma)


class MedianFilter(BaseFilter):
    """
    MedianFilter Class
    """
    def __init__(self, tk_master, apply_func):
        """
        MedianFilter constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(MedianFilter, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._ksize = Scale(self.frame, from_=1, to=50, label='Kernal Size', orient=HORIZONTAL,
                            command=self.apply_func)
        self._ksize.pack()

    @property
    def ksize(self):
        return self._ksize.get()

    @property
    def set_to_origonal(self):
        """
        Property to tell whether, given the parameters to the filter to set
        the image back to the original image.
        """
        return self.ksize == 1

    def filter(self, img):
        assert self.ksize % 2
        return cv2.medianBlur(img, self.ksize)


class BilateralFilter(BaseFilter):
    """
    BilateralFilter Class
    """
    def __init__(self, tk_master, apply_func):
        """
        BilateralFilter constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(BilateralFilter, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._sigma_color = Scale(self.frame, from_=1, to=75, label='Sigma Color', orient=HORIZONTAL)
        self._sigma_color.pack()
        self._sigma_space = Scale(self.frame, from_=1, to=75, label='Sigma Space', orient=HORIZONTAL)
        self._sigma_space.pack()
        self._apply_btn = Button(self.frame, text='Apply', command=self.apply_func)
        self._apply_btn.pack()

    @property
    def sigma_color(self):
        return self._sigma_color.get()

    @property
    def sigma_space(self):
        return self._sigma_space.get()

    @property
    def set_to_origonal(self):
        return self.sigma_color == 1 and self.sigma_space == 1

    def filter(self, img):
        return cv2.bilateralFilter(img, -1, self.sigma_color, self.sigma_space)


class CannyEdgeDetector(BaseFilter):
    """
    CannyEdgeDetector Class
    """
    def __init__(self, tk_master, apply_func):
        """
        CannyEdgeDetector constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(CannyEdgeDetector, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._thresh_1 = Scale(self.frame, from_=1, to=200, label='Threshold #1', orient=HORIZONTAL,
                               command=self.apply_func)
        self._thresh_1.pack()
        self._thresh_2 = Scale(self.frame, from_=1, to=200, label='Threshold #2', orient=HORIZONTAL,
                            command=self.apply_func)
        self._thresh_2.pack()
        self.show_normal = True

    @property
    def threshold_1(self):
        return self._thresh_1.get()

    @property
    def threshold_2(self):
        return self._thresh_2.get()

    @property
    def set_to_origonal(self):
        return self.threshold_1 ==1 and self.threshold_2 == 1

    def filter(self, img):
        return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), self.threshold_1, self.threshold_2)


class NonLocalMeansColor(BaseFilter):
    """
    NonLocalMeansColor Class
    """
    def __init__(self, tk_master, apply_func):
        """
        NonLocalMeansColor constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(NonLocalMeansColor, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._l = Scale(self.frame, from_=1, to=10, label='Luminance', orient=HORIZONTAL)
        self._l.pack()
        self._apply_btn = Button(self.frame, text='Apply', command=self.apply_func)
        self._apply_btn.pack()

    @property
    def luminance(self):
        return self._l.get()

    @property
    def set_to_origonal(self):
        return self.luminance == 1

    def filter(self, img):
        return cv2.fastNlMeansDenoisingColored(img, h=self.luminance, hColor=self.luminance)


class SobelFilter(BaseFilter):
    def __init__(self, tk_master, apply_func):
        super(SobelFilter, self).__init__(tk_master, apply_func)

        # Adding GUI parameters
        self._dx = Scale(self.frame, from_=1, to=4, label='dx', orient=HORIZONTAL,
                         command=self.apply_func)
        self._dx.pack()
        self._dy = Scale(self.frame, from_=1, to=4, label='dy', orient=HORIZONTAL,
                         command=self.apply_func)
        self._dy.pack()
        self._ksize = Scale(self.frame, from_=1, to=7, label='Kernel Size', orient=HORIZONTAL,
                         command=self.apply_func)
        self._ksize.pack()
        self.show_normal = True

    @property
    def dx(self):
        return self._dx.get()

    @property
    def dy(self):
        return self._dy.get()

    @property
    def ksize(self):
        return self._ksize.get()

    @property
    def set_to_origonal(self):
        return self.dy == 1 and self.dx == 1 and self.ksize == 1

    def filter(self, img):
        assert self.ksize % 2
        return cv2.Sobel(img, -1, dx=self.dx, dy=self.dy, ksize=self.ksize)


class LaplacianFilter(BaseFilter):
    def __init__(self, tk_master, apply_func):
        super(LaplacianFilter, self).__init__(tk_master, apply_func)
        self.show_normal = True

        self._ksize = Scale(self.frame, from_=1, to=15, label='Kernel Size', orient=HORIZONTAL,
                         command=self.apply_func)
        self._ksize.pack()

    @property
    def ksize(self):
        return self._ksize.get()

    @property
    def set_to_origonal(self):
        return self.ksize == 1

    def filter(self, img):
        assert self.ksize % 2
        return cv2.Laplacian(img, -1, ksize=self.ksize)
