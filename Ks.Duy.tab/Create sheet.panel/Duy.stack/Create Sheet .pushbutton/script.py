
from Autodesk.Revit.UI import UIDocument
from Autodesk.Revit.DB import FilteredElementCollector,BuiltInCategory,Element,Transaction,FamilySymbol,ViewSheet
from Autodesk.Revit.DB import FamilySymbol 
# Get UIDocument
uidoc = __revit__.ActiveUIDocument
# Get Document 
doc = uidoc.Document

import os,xlrd
# retrieve dir path from abspath 
dir_path = os.path.dirname(os.path.abspath(__file__))
# retrieve fullname excel file 
file_loc = os.path.join(dir_path,"Sheet Name.xls")
# retrieve workbook 
workbook = xlrd.open_workbook(file_loc)
# retrieve sheet
sheet = workbook.sheet_by_index(0)
list_number= []
List_name=[]
for s in workbook.sheets():
    #print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)  
        list_number.append(values[0])
        List_name.append(values[1])
list_number.pop(0)
List_name.pop(0)
#----------------------------------------------------------------------------------
# Get collector from FilteredElementCollector
titleblocks = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().OfClass(FamilySymbol)
# Get viewsheet from FilteredElementCollector
viewsheets = FilteredElementCollector(doc).OfClass(ViewSheet)
# Get viewsheets 
LSheetName = []
LSheetNumber = []

for viewsheet in viewsheets:
    LSheetNumber.append(viewsheet.SheetNumber)
    LSheetName.append(viewsheet.Name)
#name of title block
titleblocks_name = "A1 metric"
# get id of TitleBlocks symbol
for titleblock in titleblocks:
    if Element.Name.__get__(titleblock) == titleblocks_name:
        titleblockid = titleblock.Id
i = 0
while List_name[i] in LSheetName:
    i = i + 1
i = 1
while ("P"+ str(i)) in LSheetNumber:
    nb = "P" + str(i+1)
    i = i + 1
k = 0
while list_number[k] in LSheetNumber:
    k = k + 1
 
if all(["P" not in snumber for snumber in LSheetNumber]):
    nb = "P1"
t = Transaction (doc,"Create Sheet")
t.Start()
# create sheet 
sheet = ViewSheet.Create(doc, titleblockid)
#set name of sheet 
sheet.Name = List_name[i]
# set sheet number of sheet 
sheet.SheetNumber = nb

t.Commit()
