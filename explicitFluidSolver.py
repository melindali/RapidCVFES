#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Copyright, 2023
    Xue Li

    Explicit fluid solver on GPUs.
"""


from mesh import FluidMesh


__author__ = "Xue Li"
__copyright__ = "Copyright 2023, the RapidCVFES project"



class ExplicitFluidSolver:
    """ Solving incompressible N-S equations 
        using explicit time integration on GPUs"""
    def __init__(self, mesh):
        
        self.mesh = mesh


    def solve(self):
        print("Start solving")
        