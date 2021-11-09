
from xlsxwriter.workbook import Workbook
from Autodesk.Revit.DB import FilteredElementCollector,Transaction,ViewSchedule,ViewScheduleExportOptions,ExportTextQualifier

from Autodesk.Revit.UI import TaskDialog
import os
import os.path as op
from pyrevit import revit
import xlsxwriter
from rpw.ui.forms import select_folder

#Get UIDocument
uidoc = __revit__.ActiveUIDocument 
#Get Document 
doc = uidoc.Document
# FilteredElementCollector
cl = FilteredElementCollector(doc)
filename_no_ext = doc.Title
collection = cl.OfClass((ViewSchedule)) 
#file = filename_no_ext   
opt = ViewScheduleExportOptions()

folder = select_folder()
# os.chdir("E:\\")  
# folder= os.mkdir("Test")
# # os.makedirs(folder)
 
for i in collection:
  tmvs=i.Name.Replace( '/',None)
  # sheetname = i.Name.Substring(0,10)
  # tmsheetname=sheetname.Replace( '/', '_' )
  # workbook = xlsxwriter.Workbook(tmvs)
  # worksheet = workbook.add_worksheet(tmsheetname)
  print(tmvs)
  i.Export(folder, tmvs +'.csv', opt)
  exported = op.join(folder, tmvs+'.csv')
