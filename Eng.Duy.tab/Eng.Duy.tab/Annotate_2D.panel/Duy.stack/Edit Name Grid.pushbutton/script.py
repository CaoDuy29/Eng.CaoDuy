from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,Element
from Autodesk.Revit.DB.Parameter import Set
from Autodesk.Revit.DB import Parameter,Transaction, Location, LocationCurve,XYZ
from rpw.ui.forms import TextInput
#Get UIDocument
uidoc = __revit__.ActiveUIDocument
#Get Document 
doc = uidoc.Document
#Pick Object 
picks= uidoc.Selection.PickObjects(ObjectType.Element)

list_grid= []
for pick in picks:
  eleId_grid = pick.ElementId
  ele_grid = doc.GetElement(eleId_grid)
  if ele_grid.Category.Name== "Grids":
  	list_grid.append(ele_grid)
  
list_endpoint_grid=[]
for grid in list_grid:
  endpoint_grid= grid.Curve.GetEndPoint(0).X
  list_endpoint_grid.append(endpoint_grid)
 
list_endpoint_grid_sorted= sorted(list_endpoint_grid) 
# print(list_endpoint_grid_sorted)
 
list_parameter_name_grid= []
for i in list_endpoint_grid_sorted:
    for j in list_grid:
        if j.Curve.GetEndPoint(0).X == i:
            list_parameter_name_grid.append(j) 
            
# Get transaction 
t= Transaction(doc,"Name")
t.Start()
name_grid= "A"
description = "Choose Text"
value = TextInput('Gird', name_grid, description)
total_list_parameter_name_grid=len(list_endpoint_grid_sorted)
for i in range(total_list_parameter_name_grid):
    parameter_mark= list_parameter_name_grid[i].LookupParameter("Name")
    parameter_mark.Set(value + str(i+1))
t.Commit()






  