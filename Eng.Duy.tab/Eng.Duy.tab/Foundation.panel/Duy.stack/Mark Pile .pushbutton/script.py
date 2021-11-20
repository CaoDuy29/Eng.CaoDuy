
from Autodesk.Revit.DB import FilteredElementCollector,ElementCategoryFilter,BuiltInCategory
from Autodesk.Revit.DB import Element, FamilySymbol, Definition
from Autodesk.Revit.DB import Parameter,Transaction, Location
from Autodesk.Revit.DB.Parameter import Set
#Get UIDocument
uidoc = __revit__.ActiveUIDocument
#Get Document 
doc = uidoc.Document

#Create Filter foundation
filter_foundation = ElementCategoryFilter(BuiltInCategory.OST_StructuralFoundation)
# Get all  foundation in project
foundation = FilteredElementCollector(doc).WherePasses (filter_foundation).WhereElementIsNotElementType().ToElements()

#list_point
list_pointX = []
for i in foundation:          
    pointX= (i.Location.Point.X)
    list_pointX.append(pointX)
list_pointX= list(set(list_pointX))
list_pointX =sorted(list_pointX)

list_foundaiton= []
for i in list_pointX:
    for j in foundation:
        if j.Location.Point.X == i:
            list_foundaiton.append(j)
            # print(range(len(list_foundaiton)))
# Get transaction 
t= Transaction(doc,"name Mark")
t.Start()

total_foundation = len(list_foundaiton)

for i in range(total_foundation):
    parameter_mark= list_foundaiton[i].LookupParameter("Mark")
    parameter_Filter = list_foundaiton[i].LookupParameter("Filter_Element").AsString()
    if parameter_Filter == "Pile_1":
        parameter_mark.Set("P" + str(i+1))
   

# print(parameter_mark.Definition.Name)
# print(parameter_Filter.AsString())
t.Commit()
