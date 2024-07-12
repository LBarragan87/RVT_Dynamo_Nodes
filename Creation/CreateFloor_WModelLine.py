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
FloorType = UnwrapElement(IN[0])
Level=UnwrapElement(IN[1])
ListaLineas=UnwrapElement(IN[2])

FloorTypeId=FloorType.Id
LevelId=Level.Id

######################################################
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)

puntos =[]
n=0
lineas=[]
for linea in ListaLineas:
    punto=linea.GeometryCurve.GetEndPoint(0)
    puntos.append(punto)
    if n==0:
        x=5
        print (str(n) + "_" + str(x))
    else:
        x=2
        print (str(n) + "_" + str(x))
        linea=Line.CreateBound(puntos[n-1],puntos[n])
        lineas.append(linea)
    n=n+1

UltimaLinea=Line.CreateBound(puntos[n-1],puntos[0])
lineas.append(UltimaLinea)

thisCurve=CurveLoop.Create(lineas)

CreatingFloor=clr.Autodesk.Revit.DB.Floor.Create(doc,[thisCurve],FloorTypeId,LevelId)

TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output

OUT = CreatingFloor
