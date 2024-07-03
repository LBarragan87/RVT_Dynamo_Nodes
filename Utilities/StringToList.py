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

import re

#Get Document
doc = DocumentManager.Instance.CurrentDBDocument
######################################################
#Create Functions
def CleanText(text):
    thisStrip = text.strip()
    thisLStrip=thisStrip.lstrip()
    thisMtrip=re.sub(' +', ' ', thisLStrip)
    return thisMtrip
    
def SplitText(text,separator):
    return text.split(separator)

def CleanedList(textoOriginal,separator):
    listaLimpia=[]
    for texto in SplitText(textoOriginal,separator):
        thisCleaned=CleanText(texto)
        listaLimpia.append(thisCleaned)
    return listaLimpia
######################################################
#Inputs
ListaTexto = IN[0]
separator=IN[1]
######################################################
# Start Code
TransactionManager.Instance.EnsureInTransaction(doc)
CleanListaTexto=CleanedList(ListaTexto,separator)
TransactionManager.Instance.TransactionTaskDone()
######################################################
# Output
OUT = CleanListaTexto
