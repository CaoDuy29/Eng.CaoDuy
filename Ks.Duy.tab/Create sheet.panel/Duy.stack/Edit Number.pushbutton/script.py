#pylint: disable=W0703,E0401,C0103,C0111
from pyrevit import coreutils
from pyrevit import revit, DB
from pyrevit import forms
from pyrevit import script
import re

__doc__ = 'Increases the sheet number of the selected sheets by one. '\
          'The sheet name change will be printed if logging is set '\
          'to Verbose in pyRevit settings.'


logger = script.get_logger()

selection = revit.get_selection()

selected_sheets = forms.select_sheets(title='Select Sheets')
if not selected_sheets:
    script.exit()

sorted_sheet_list = sorted(selected_sheets, key=lambda x: x.SheetNumber)

with revit.TransactionGroup('Shift Sheets'):
    for sheet in sorted_sheet_list:
        with revit.Transaction('Shift Single Sheet'):
            try:
                cur_sheet_num = sheet.SheetNumber
                sheetnum_p = sheet.Parameter[DB.BuiltInParameter.SHEET_NUMBER]
                sheetnum_p.Set(cur_sheet_num + "ZZZ")
            except Exception as shift_err:
                logger.error(shift_err)
            revit.doc.Regenerate()
nnumber = 1
with revit.TransactionGroup('Shift Sheets'):
    for sheet in sorted_sheet_list:
        with revit.Transaction('Shift Single Sheet'):
            try:
                # get current number  sheet 
                cur_sheet_num = sheet.SheetNumber
                sheetnum_p = sheet.Parameter[DB.BuiltInParameter.SHEET_NUMBER]
    
                # return name substr to replace 
                partern = "(\d+)(\D+)$"
                res = re.search(partern,cur_sheet_num).group()
                if nnumber in range(0,10):
                    snnumber = "12010" + str(nnumber)

                # Return new number sheet 
                new_sheet_num = cur_sheet_num.replace(res,str(snnumber))

                # set to sheet number 
                sheetnum_p.Set(new_sheet_num)
            except Exception as shift_err:
                logger.error(shift_err)
            revit.doc.Regenerate()
            nnumber = nnumber + 1 