# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf(r"D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Old\physics.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into(r"D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Old\physics.pdf", r"D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Fresh\physics.csv", output_format="csv", pages='all')
print(df)