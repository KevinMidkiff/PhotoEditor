"""
Image Module
"""
import cv2
import os

from .exceptions import ImageNotExist, ImageAlreadyExists


class Image(object):
    """
    Image Class
    """
    def __init__(self, filename):
        """
        Image class constructor

        Throws an ImageNotExist exception if the given file does not exist.

        Parameters:
            filename - Filename of the image to load
        """
        if not os.path.exists(filename):
            raise ImageNotExist('Image "{0}" does not exist'.format(filename))

        self.filename = filename
        self._img = cv2.imread(filename)
        self._orig_img = self._img
        self._prev_img = self._img
        self.cvt_flag = cv2.COLOR_BGR2RGBA
        self.show_normal = False
        self.prev_show_normal = False

    @property
    def origonal(self):
        """
        The origonal image that was read in
        """
        return self._orig_img

    @property
    def image(self):
        """
        The current image
        """
        if self.show_normal:
            return self._img
        else:
            return cv2.cvtColor(self._img, self.cvt_flag)

    def reset(self):
        """
        Reset back to the origonal image
        """
        self._img = self.origonal
        self.show_normal = False

    def undo(self):
        """
        Undo the last filter
        """
        self._img = self._prev_img
        self.show_normal = self.prev_show_normal

    def save(self, filename, overwrite=False):
        """
        Save the image with all filters

        If overwrite is set to False, then an ImageAlreadyExists exception
        will be thrown if the given filename already exists.

        Parameters:
            filename  - Name of the file to save the image as
            overwrite - (Optional) Flag for whether or not to overwrite the
                        file if it already exists.  By default this is set to
                        NOT overwrite the file.
        """
        if os.path.exists(filename) and not overwrite:
            raise ImageAlreadyExists(
                'Image "{0}" already exists'.format(filename))
        cv2.imwrite(filename, self._img)

    def apply_filter(self, img_filter):
        """
        Apply the given filter to the image.

        Parameters:
            img_filter - A filter of type BaseFilter
        """
        self._prev_img = self._img
        self.prev_show_normal = self.show_normal

        try:
            self.show_normal = img_filter.show_normal
            self._img = img_filter.filter(self._orig_img)

            if img_filter.set_to_origonal:
                self.reset()
        except AssertionError:
            if img_filter.set_to_origonal:
                self.reset()
            else:
                self.undo()
