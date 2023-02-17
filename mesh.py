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


class FluidMesh:
    """Default fluid mesh use tetrahedron elements."""
    nElmNodes = 4
    
    def __init__(self, config):
        
        self.readMesh(config.fMeshName)


    def readMesh(self, fMeshName):
        # initialize reader
        reader = vtk.vtkXMLPolyDataReader() if fMeshName.endswith('vtp') \
            else vtk.vtkXMLUnstructuredGridReader()
        reader.SetFileName(fMeshName)
        reader.Update()

        polyDataModel = reader.GetOutput()

        # Read the nodes and coordinates.
        nNodes = polyDataModel.GetNumberOfPoints() # _nNodes
        nodes = np.copy(vtk_to_numpy(polyDataModel.GetPoints().GetData())) # _nodes
        nodes = nodes.astype(float)
        # Read the elements.
        nElements = polyDataModel.GetNumberOfCells()
        elementNodeIds = np.zeros((nElements, FluidMesh.nElmNodes), dtype=np.int64)
        for i in range(nElements):
            vtkCell = polyDataModel.GetCell(i)
            for j in range(FluidMesh.nElmNodes):
                elementNodeIds[i,j] = vtkCell.GetPointId(j)
        # Read the global node ids to match between different meshes.
        glbNodeIds = vtk_to_numpy(polyDataModel.GetPointData().GetArray('GlobalNodeID'))
        glbElementIds = vtk_to_numpy(polyDataModel.GetCellData().GetArray('GlobalElementID'))

        # Setup the instance variables.
        self.nNodes = nNodes
        self.nodes = nodes
        self.nElements = nElements
        self.elementNodeIds = elementNodeIds
        self.glbNodeIds = glbNodeIds
        self.glbElementIds = glbElementIds

        print("Read mesh successfully, {0} nodes, {1} elements".format(nNodes, nElements))



