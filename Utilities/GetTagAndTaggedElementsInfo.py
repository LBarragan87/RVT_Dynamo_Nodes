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

#Inputs
etiquetas = UnwrapElement(IN[0])

# Incluya el código debajo de esta línea
ListaIds=[]
TagNameList=[]
TagIdList=[]
for etiqueta in etiquetas:
    thisName=etiqueta.Name
    thisTagId=etiqueta.Id
    thisId = etiqueta.GetTaggedElementIds()
    ListaIds.append(thisId)
    TagIdList.append(thisTagId)
    TagNameList.append(thisName)

FlattenedListaIds=List.Flatten(ListaIds)
TaggedElementsName=[]
TaggedElementIds=[]
for elemento in FlattenedListaIds:
    getElement=doc.GetElement(elemento.HostElementId).Name
    ElementId=doc.GetElement(elemento.HostElementId)
    TaggedElementsName.append(getElement)
    #thisElementId=getElement.Id
    TaggedElementIds.append(ElementId)
# Asigne la salida a la variable OUT.
OUT = [TagIdList,TagNameList,TaggedElementIds,TaggedElementsName]
