
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory,Element
from Autodesk.Revit.DB import Parameter,Transaction, Location, UnitUtils, DisplayUnitType
import csv
#Get UIDocument
uidoc = __revit__.ActiveUIDocument
#Get Document 
doc = uidoc.Document

#Create Filter foundation
filter_foundation = ElementCategoryFilter(BuiltInCategory.OST_StructuralFoundation)
# Get all  foundation in project
foundation = FilteredElementCollector(doc).WherePasses (filter_foundation).WhereElementIsNotElementType().ToElements()
# Get value pile 
list_mark=[]
list_locx=[]
list_locy=[]
for i in foundation:          
    parameter_mark = i.LookupParameter("Mark").AsString()
    point_Units_X = UnitUtils.ConvertFromInternalUnits(i.Location.Point.X, DisplayUnitType.DUT_METERS)
    point_Units_Y = UnitUtils.ConvertFromInternalUnits(i.Location.Point.Y, DisplayUnitType.DUT_METERS)
    list_mark.append(parameter_mark)
    list_locx.append(point_Units_X)
    list_locy.append(point_Units_Y)

# writer csv -------------------------->  
header = ['Mark', 'Loc_x', 'Loc_y']
with open(r'E:\18. Tool Duy\Excel pile.csv','w') as f:
    writer = csv.writer(f, lineterminator ='\n')
    writer.writerow(header)
    for i,j,k in zip(list_mark,list_locx,list_locy):
        writer.writerow([i]+[j]+[k])

print("ok")
    




