import xlrd

loc=('D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Old\data.xlsx')
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)

Dict={}
for i in range(0,sheet.nrows):
    Dict[sheet.cell_value(i,0)]=sheet.cell_value(i,1)

llc=input()

if llc in Dict:
    print(Dict[llc])