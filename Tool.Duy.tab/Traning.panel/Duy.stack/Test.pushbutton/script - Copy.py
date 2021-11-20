from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,Element
from Autodesk.Revit.DB import Parameter,Transaction, UnitUtils,Location, LocationCurve,XYZ,ElementTransformUtils,IndependentTag,DisplayUnitType
from rpw.ui.forms import TextInput
# #Get UIDocument
# uidoc = __revit__.ActiveUIDocument
# #Get Document 
# doc = uidoc.Document
# #Pick Object 


uiapp = commandData.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document
activeView = doc.ActiveView
geomOption = doc.Create.NewGeometryOptions()

pick= uidoc.Selection.PickObject(ObjectType.Element)

eleId_tag = pick.ElementId
ele_tag = doc.GetElement(eleId_tag)


# get layer column: 
layer= ele_tag.get_Geometry(geomOption)
print (layer)


# UIApplication uiapp = commandData.Application;
#             UIDocument uidoc = uiapp.ActiveUIDocument;
#             Document doc = uidoc.Document;
#             Autodesk.Revit.DB.View activeView = doc.ActiveView;
#             Autodesk.Revit.DB.Options geomOption = doc.Create.NewGeometryOptions()




# t= Transaction(doc,"loc")
# t.Start()

# value_log_x= "0"
# description = "Value X "
# valuex = TextInput('Move Tag', value_log_x, description)

# value_log_y= "0"
# description = "Value Y "
# valuey = TextInput('Move Tag', value_log_y, description)
# for i in list_tag:
#     i.TagHeadPosition= i.TagHeadPosition + XYZ(int(valuex)/304.8,int(valuey)/304.8,0)
# t.Commit()