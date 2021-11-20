from Autodesk.Revit.DB import (Transaction, FilteredElementCollector,
                                Element, View, ElementId, FamilyInstance, 
                                FillPatternElement, Color, OverrideGraphicSettings)
from Autodesk.Revit.UI import UIDocument, Selection
from Autodesk.Revit.UI.Selection.Selection import PickObject 
from Autodesk.Revit.UI.Selection import ObjectType
import random  

# Get UIDocument
uidoc = __revit__.ActiveUIDocument

# Get Document 
doc = uidoc.Document

# Get the active view of the current document
view = doc.ActiveView

# Create  FamilyInstance FilteredElementCollector 
filter_collector = FilteredElementCollector(doc).OfClass(FamilyInstance)

# Definition to convert elementtype to id_string type
def id_sym(ele):
    ele_typeId = ele.GetTypeId()
    return ele_typeId.ToString()

# Remove duplicated element type id
lkey_ids = set(map(id_sym,filter_collector))

# print(lkey_ids)

# Dict from FilteredElementCollector; id: key of elementtype; value: family instace 
dicta = {}
for key_id in lkey_ids:
    dicta[key_id] = [ele for ele in filter_collector if ele.GetTypeId().ToString() == key_id]

# Set Fill Pattern
name_pattern = "<Solid fill>"

# Create FillPatternElement FilteredElementCollector 
patterns = FilteredElementCollector(doc).OfClass(FillPatternElement)

t = Transaction(doc,"Change elements's color")
t.Start()

for pattern in patterns:
    if pattern.Name == name_pattern:
        solidPatternId = pattern.Id

for keyid in list(dicta.keys()):
    # Set Color Random
    color_ele = Color(random.randint(0,256),random.randint(0,256),random.randint(0,256))

    for element in dicta[keyid]:
        # Settings to override display of elements in a view.
        override = OverrideGraphicSettings()

        # Sets the projection surface fill color
        override.SetSurfaceForegroundPatternColor(color_ele)

        # Sets the projection surface fill pattern
        override.SetSurfaceForegroundPatternId(solidPatternId)

        # Sets graphic overrides for an element in the view.
        view.SetElementOverrides(element.Id, override)

t.Commit()

   



