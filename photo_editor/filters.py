"""
Filters Module
"""
import cv2

from .exceptions import BadFilterParams

class BaseFilter(object):
    """
    Base filter class
    """
    def __init__(self, *args, **kwargs):
        """
        BaseFilter constructor

        Parameters to be set by subclasses
        """
        # raise NotImplemented('The BaseFilter class is unimplemented')
        self.args = args
        self.kwargs = kwargs
        self.filter_func = None

    def filter(self, img):
        """
        Apply the filter to the given image.

        If the parameters to pass to the filter method given to the 
        constructor were incorrect, then a BadFilterParams exception
        will be thrown

        Parameters:
            img - The value returned by cv2.imread()
        """
        try:
            return self.filter_func(img, *self.args, **self.kwargs)
        except TypeError as e:
            raise BadFilterParams(
                'Bad parameters passed to filter\n' + e.message)



class BoxFilter(BaseFilter):
    """
    Box Filter Class
    """
    def __init__(self, *args, **kwargs):
        """
        BoxFilter constructor

        See documentation for cv2.boxFilter for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(BoxFilter, self).__init__(*args, **kwargs)
        self.filter_func = cv2.boxFilter


class GaussianFilter(BaseFilter):
    """
    GaussianFilter Class
    """
    def __init__(self, *args, **kwargs):
        """
        GaussianFilter constructor

        See documentation for cv2.GaussianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(GaussianFilter, self).__init__(*args, **kwargs)
        self.filter_func = cv2.GaussianBlur


class MedianFilter(BaseFilter):
    """
    MedianFilter Class
    """
    def __init__(self, *args, **kwargs):
        """
        MedianFilter constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(MedianFilter, self).__init__(*args, **kwargs)
        self.filter_func = cv2.medianBlur


class BilateralFilter(BaseFilter):
    """
    BilateralFilter Class
    """
    def __init__(self, *args, **kwargs):
        """
        BilateralFilter constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(BilateralFilter, self).__init__(*args, **kwargs)
        self.filter_func = cv2.bilateralFilter


class CannyEdgeDetector(BaseFilter):
    """
    CannyEdgeDetector Class
    """
    def __init__(self, *args, **kwargs):
        """
        CannyEdgeDetector constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(CannyEdgeDetector, self).__init__(*args, **kwargs)
        self.filter_func = cv2.Canny


class NonLocalMeans(BaseFilter):
    """
    NonLocalMeans Class
    """
    def __init__(self, *args, **kwargs):
        """
        NonLocalMeans constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(NonLocalMeans, self).__init__(*args, **kwargs)
        self.filter_func = cv2.fastNlMeansDenoising


class NonLocalMeansColor(BaseFilter):
    """
    NonLocalMeansColor Class
    """
    def __init__(self, *args, **kwargs):
        """
        NonLocalMeansColor constructor

        See documentation for cv2.medianBlur for parameters.

        DO NOT PASS THE "img" PARAMETER TO THE CONSTRUCTOR.
        """
        super(NonLocalMeansColor, self).__init__(*args, **kwargs)
        self.filter_func = cv2.fastNlMeansDenoisingColored
