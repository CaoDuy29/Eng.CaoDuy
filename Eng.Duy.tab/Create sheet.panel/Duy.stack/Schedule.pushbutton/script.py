
from xlsxwriter.workbook import Workbook
from Autodesk.Revit.DB import FilteredElementCollector,Transaction,ViewSchedule,ViewScheduleExportOptions,ExportTextQualifier

from Autodesk.Revit.UI import TaskDialog
import os
import os.path as op
from pyrevit import revit
from pyrevit import forms
from pyrevit import script
from rpw.ui.forms import select_folder

#Get UIDocument
uidoc = __revit__.ActiveUIDocument 
#Get Document 
doc = uidoc.Document 
opt = ViewScheduleExportOptions()
# filter selection schedule
logger = script.get_logger()

selection = revit.get_selection()
folder = select_folder()
selected_Schedule = forms.select_schedules(title='Select Schedule')
if not selected_Schedule:
    script.exit()
sorted_Schedule = sorted(selected_Schedule, key=lambda x: x.Name)
if sorted_Schedule:
  cl = FilteredElementCollector(doc) # FilteredElementCollector
  collection = cl.OfClass((ViewSchedule)) # filename_no_ext = doc.Title
  for i in sorted_Schedule:
    tmvs=i.Name.Replace( '/',None)
    i.Export(folder, tmvs +'.csv', opt)
    exported = op.join(folder, tmvs+'.csv')
