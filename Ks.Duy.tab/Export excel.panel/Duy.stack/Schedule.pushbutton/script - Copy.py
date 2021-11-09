from xlsxwriter.workbook import Workbook
from Autodesk.Revit.DB import FilteredElementCollector,Transaction,ViewSchedule,ViewScheduleExportOptions,ExportTextQualifier

from Autodesk.Revit.UI import TaskDialog
import os
import os.path as op
from pyrevit import revit
import xlsxwriter
from rpw.ui.forms import select_file
# filepath = select_file('Revit Model(*.rvt)|*rvt', 'Select RVT File', multiple=True)
# list=(filepath)
for filename in list:     
    doc = __revit__.Application.OpenDocumentFile(filename)
    cl = FilteredElementCollector(doc)
    filename_no_ext = doc.Title
    collection = cl.OfClass((ViewSchedule))  
    folder = filename.replace(".rvt","")
    os.makedirs(folder)
    #file = filename_no_ext   
    opt = ViewScheduleExportOptions()
    #TextQualifier = ExportTextQualifier.DoubleQuote
    #opt.FieldDelimiter = " "
    #FieldDelimiter = ","
    for vs in collection:
      tmvs=vs.Name.Replace( '/', '_' )
      sheetname = vs.Name.Substring(0,10)
      tmsheetname=sheetname.Replace( '/', '_' )
      workbook = xlsxwriter.Workbook(tmvs)
      worksheet = workbook.add_worksheet(tmsheetname)
      vs.Export(folder, tmvs +'.csv', opt)
      exported = op.join(folder, tmvs+'.csv')
      
TaskDialog.Show ("EXPORT SCHEDULE", "OK")
