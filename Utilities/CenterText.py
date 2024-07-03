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

# Import DocumentManager
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Get Document
doc = DocumentManager.Instance.CurrentDBDocument
######################################################################################
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
######################################################################################
#Inputs
TextList = UnwrapElement(IN[0]) #Select Elements to move
InsertionPoint = UnwrapElement(IN[1]) #Specify new coordinates of Insertion Point (Coordinates on METERS)

#Input List Conversion
convertedTextList=ElementsToList(TextList)

######################################################################################
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)

newCoord= PointToXYZ(InsertionPoint)

CoordList=[]
for textNote in convertedTextList:
    thisCoord=textNote.set_Coord(newCoord)
    CoordList.append(InsertionPoint)
    
TransactionManager.Instance.TransactionTaskDone()
######################################################################################
# Output
OUT = zip(convertedTextList,CoordList)
