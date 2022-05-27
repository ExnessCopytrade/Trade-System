# Indicator.py

from abc import ABCMeta, abstractmethod

class Indicator(object):
    """
    Indicator is an abstract base class providing an interface for
    all subsequent (inherited) indicator objects.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def (self):
        """

        """
        raise NotImplementedError("Should implement ()")
