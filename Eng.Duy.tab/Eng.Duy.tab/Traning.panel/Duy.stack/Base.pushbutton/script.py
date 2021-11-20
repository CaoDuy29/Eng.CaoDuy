__doc__ = 'python for revit api'
__author__ = 'pyan.vn'
from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import Element
#Get UIDocument
uidoc = __revit__.ActiveUIDocument

#Get Document 
doc = uidoc.Document

#Pick Object 
Pick= uidoc.Selection.PickObject(ObjectType.Element)
print(Pick)

#Retrieve Elenment
eleid = Pick.ElementId
ele = doc.GetElement(eleid)
print(ele)
print(eleid)
#Get Element Type 
# elementtype = doc.GetElement(ele.GetTypeId())

# # Display element Id,Category name, Instance name,FamilySymbol name, Family Name
# print ("ID of element is :",eleid.ToString(),"Category is:",ele.Category.Name,"Instance name is:" ,ele.Name,"FamilySymbol is:",Element.Name.__get__(elementtype),"FamilyName is:",elementtype.FamilyName)

