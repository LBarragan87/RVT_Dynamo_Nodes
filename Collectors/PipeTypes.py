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
# Start Code
PipeTypes = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeCurves).WhereElementIsElementType().ToElements()
#clr.Autodesk.Revit.DB.Plumbing.Pipe.Create(doc)
######################################################
# Output
OUT = PipeTypes
