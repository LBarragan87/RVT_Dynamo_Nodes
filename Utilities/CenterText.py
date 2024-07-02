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
texto = UnwrapElement(IN[0])

# Incluya el código debajo de esta línea
TransactionManager.Instance.EnsureInTransaction(doc)
newCoord= XYZ(0,0,0)
X=texto.set_Coord(newCoord)
TransactionManager.Instance.TransactionTaskDone()
# Asigne la salida a la variable OUT.
OUT = texto
