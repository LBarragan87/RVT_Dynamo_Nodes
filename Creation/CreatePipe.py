import System
import clr

#import DSCoreNodes
clr.AddReference('DSCoreNodes')
from DSCore import *

#Import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import RevitNodes
clr.AddReference("RevitNodes")
from Revit import *

# Import Revit elements
from Revit.Elements import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Plumbing import *
# Import DocumentManager
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Get Document
doc = DocumentManager.Instance.CurrentDBDocument
######################################################
#Create Functions
def ElementsToList(Input):
    newList=[]
    try:
        TextListCount=List.Count(Input)
        newList=Input
    except:
        newList.append(Input)
    return newList
    
def MtoFt(M):
    return M/12/0.0254
    
def PointToXYZ(ProtogeometryPoint):
    XFromInsertionPoint=MtoFt(Autodesk.DesignScript.Geometry.Point.get_X(ProtogeometryPoint))
    YFromInsertionPoint=MtoFt(Autodesk.DesignScript.Geometry.Point.get_Y(ProtogeometryPoint))
    ZFromInsertionPoint=MtoFt(Autodesk.DesignScript.Geometry.Point.get_Z(ProtogeometryPoint))
    return XYZ(XFromInsertionPoint,YFromInsertionPoint,ZFromInsertionPoint)
######################################################
#Inputs
PipeSystem = UnwrapElement(IN[0]) #Select Elements to move
PipeType=UnwrapElement(IN[1])
Level = UnwrapElement(IN[2])
#Input List Conversion

######################################################
# Start Code
PipeSystemId = ElementId(PipeSystem)
PypeTypeId=ElementId(PipeType[0])
LevelId=ElementId(Level)

TransactionManager.Instance.EnsureInTransaction(doc)

newPipe=Pipe.Create(doc,PipeSystemId,PypeTypeId,LevelId,XYZ(0,0,0),XYZ(10,0,0))
    
TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = newPipe
