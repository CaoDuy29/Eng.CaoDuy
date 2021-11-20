from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,Element,Options
from Autodesk.Revit.DB import Parameter,Transaction, UnitUtils,Location, LocationCurve,XYZ,ElementTransformUtils,IndependentTag,DisplayUnitType
from rpw.ui.forms import TextInput
#Get UIDocument
uidoc = __revit__.ActiveUIDocument
#Get Document 
doc = uidoc.Document
#Pick Object 

pick= uidoc.Selection.PickObject(ObjectType.Element)

eleId_cad = pick.ElementId
ele_cad = doc.GetElement(eleId_cad)

options = Options()
# Get geometry element: 
geometry_element = ele_cad.get_Geometry(options)
print(geometry_element)
for geometry_object in geometry_element:
    print(geometry_object)
    symbol_geometry = geometry_object.GetSymbolGeometry()
    print(symbol_geometry)

# GeometryElement GetSymbolGeometry()
# # SymbolGeometry
    




