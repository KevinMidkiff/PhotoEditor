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
        return self._img

    def reset(self):
        """
        Reset back to the origonal image
        """
        self._img = self.origonal

    def undo(self):
        """
        Undo the last filter
        """
        self._img = self._prev_img

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
        self._img = img_filter.filter(self._img)
