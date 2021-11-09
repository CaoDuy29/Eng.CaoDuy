import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(r'E:\18. Tool Duy\Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
a = [1,2,5,7,8,9,10,15]
b = [11,12,15,17,18,19,10,17]    
tieude=['Mark', 'locx', 'locy']
row = 0
col = 0

for h in tieude:
    worksheet.write(row, col,     h)
    # worksheet.write(row, col + 1, value_b)
    col += 1
# worksheet.write(row, col + 1, value_b)
# # Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0
# Iterate over the data and write it out row by row.
for value_a in a:
    worksheet.write(row, col,     value_a)
    # worksheet.write(row, col + 1, value_b)
    row += 1

# # # Write a total using a formula.
# # worksheet.write(row, 0, 'Total')
# # worksheet.write(row, 1, '=SUM(B1:B4)')

# # workbook.close()