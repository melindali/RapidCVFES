#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Copyright, 2023
    Xue Li

    Mesh class contains data structure representing the mesh information
    with Readin method and Write method.
"""


import numpy as np

from vtk.util.numpy_support import vtk_to_numpy
from vtk.util.numpy_support import numpy_to_vtk
import vtk

__author__ = "Xue Li"
__copyright__ = "Copyright 2023, the RapidCVFES project"