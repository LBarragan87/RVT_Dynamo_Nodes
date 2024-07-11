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
TipoMuro=UnwrapElement(IN[0])
IdMuro=TipoMuro.Id
Nivel=UnwrapElement(IN[1])
IdNivel=Nivel.Id
Altura=MtoFt(UnwrapElement(IN[2]))
Offset=MtoFt(UnwrapElement(IN[3]))
Flip=UnwrapElement(IN[4])
Estructural=UnwrapElement(IN[5])
TopNivel=UnwrapElement(IN[6])
IdTopNivel=TopNivel.Id
#Input List Conversion

######################################################
# Start Code


TransactionManager.Instance.EnsureInTransaction(doc)
inicio = XYZ(MtoFt(0),MtoFt(0),MtoFt(0))
fin=XYZ(MtoFt(0),MtoFt(20),MtoFt(0))
linea=Line.CreateBound(inicio,fin)
newWall=Wall.Create(doc,linea,IdMuro,IdNivel,Altura,Offset,Flip,Estructural)
parameterTop=newWall.get_Parameter(BuiltInParameter.WALL_HEIGHT_TYPE)
top=parameterTop.Set(IdTopNivel)
TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = newWall
