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
ListaEtiquetas = UnwrapElement(IN[0])

#Start Code
TransactionManager.Instance.EnsureInTransaction(doc)

ListaIds=[]

for etiqueta in ListaEtiquetas:
    Numeracion=1
    ElementIds=etiqueta.GetTaggedElementIds()
    ListaIds.append(ElementIds)
    ListaDepuradaIds=[]
    ListaElementos=[]
    for Elemento in ListaIds:
        for subElemento in Elemento:
            x=subElemento.get_HostElementId()
            ModelElement=doc.GetElement(x)
            parametro=ModelElement.LookupParameter("RUTA").Set("RUTA-" + str(Numeracion))
            ListaElementos.append(ModelElement)
            ListaDepuradaIds.append(x)
        Numeracion=Numeracion+1

TransactionManager.Instance.TransactionTaskDone()
#End Code

#Output
OUT = ListaEtiquetas
