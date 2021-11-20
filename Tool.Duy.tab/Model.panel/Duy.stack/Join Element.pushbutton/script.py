
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,Element
from Autodesk.Revit.DB import Parameter,Transaction, Location, UnitUtils, DisplayUnitType

#Get UIDocument
uidoc = __revit__.ActiveUIDocument
#Get Document 
doc = uidoc.Document

#Create Filter foundation
filter_foundation = ElementCategoryFilter(BuiltInCategory.OST_StructuralFoundation)
# Get all  foundation in project
foundation = FilteredElementCollector(doc).WherePasses (filter_foundation).WhereElementIsNotElementType().ToElements()
for i in foundation:          
    parameter_mark = i.LookupParameter("Mark").AsString()
    parameter_Filter = i.LookupParameter("Filter_Element").AsString()
    point_Units_X = UnitUtils.ConvertFromInternalUnits(i.Location.Point.X, DisplayUnitType.DUT_METERS)
    point_Units_Y = UnitUtils.ConvertFromInternalUnits(i.Location.Point.Y, DisplayUnitType.DUT_METERS)
    point = (point_Units_X, point_Units_Y)
    # print(parameter_mark)
    # print(point)
    Loc_x = i.LookupParameter("Loc_x")
    Loc_y = i.LookupParameter("Loc_y")
    # print(type(Location_X))
    t = Transaction (doc,"Set Location")
    t.Start()
#Set Parameter value 
    Loc_x.Set(str(point_Units_X))
    Loc_y.Set(str(point_Units_Y))
    t.Commit()
   



