#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Copyright, 2023
    Xue Li

    Main file of the RapidCVFES project.
"""

from config import Config
from mesh import FluidMesh
from explicitFluidSolver import ExplicitFluidSolver

__author__ = "Xue Li"
__copyright__ = "Copyright 2023, the RapidCVFES project"


def main():
    # Initialize the configuration.
    config = Config()
    # Readin the mesh.
    fluidMesh = FluidMesh(config)
    # Start the calculating.
    fluidSolver = ExplicitFluidSolver(fluidMesh)
    fluidSolver.solve()


if __name__ == '__main__':
    main()