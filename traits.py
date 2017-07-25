from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from traitlets import *

import six
from collections import OrderedDict, namedtuple

import re
import warnings
import inspect
import numpy as np
import matplotlib
import matplotlib.cbook as cbook
from matplotlib.cbook import mplDeprecation
from matplotlib import docstring, rcParams
from .transforms import (Bbox, IdentityTransform, TransformedBbox,
                         TransformedPatchPath, TransformedPath, Transform)
from .path import Path
from functools import wraps
from contextlib import contextmanager


class TraitProxy(TraitType):

    def __init__(self, trait):
        self.__trait = trait

    def instance_init(self, obj):
        self.__trait.instance_init(obj)

    def class_init(self, cls, name):
        self.__trait.class_init(cls, name)

    def set(self, obj, val):
        self.__trait.set(obj, val)

    def get(self, obj, cls):
        return self.__trait.get(obj, cls)

    def __getattr__(self, name):
        return getattr(self.__trait, name)

class Perishable(TraitProxy):

    def set(self, obj, val):
        super(Perishable, self).set(obj, val)
        obj.stale = True

class TransformTrait(TraitType):

    default_value = None

    def validate(self, obj, val):
        """
        Return the :class:`~matplotlib.transforms.Transform`
        instance used by this artist.

        if self._transform is None:
            self._transform = IdentityTransform()
        elif (not isinstance(self._transform, Transform)
              and hasattr(self._transform, '_as_mpl_transform')):
            self._transform = self._transform._as_mpl_transform(self.axes)
        return self._transform
        """

    # def __init__(self, trait):
    #     self.__trait = trait
    #
    # def instance_init(self, obj):
    #     self.__trait.instance_init(obj)
    #
    # def class_init(self, cls, name):
    #     self.__trait.class_init(cls, name)
    #
    # def set(self, obj, val):
    #     self.__trait.set(obj, val)
    #
    # def get(self, obj, cls):
    #     return self.__trait.get(obj, cls)
    #
    # def __getattr__(self, name):
    #     return getattr(self.__trait, name)


# class ClipPathTrait(TraitType):
#
#     def __init__(self, trait):
#         #not sure if this going to work: needs testing
#         self.__trait = trait
#         pass
#
#     # def instance_init(self, obj):
#     #     pass
#     #
#     # def class_init(self, cls, name):
#     #     pass
#
#     def set(self, obj, val):
#
#         pass
#
#     def get(self, obj, cls):
#         return self.__trait.get(obj, cls)
#         pass
#
#     def __getattr__(self, name):
#         return getattr(self.__trait, name)
