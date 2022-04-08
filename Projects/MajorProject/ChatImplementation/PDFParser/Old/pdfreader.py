from tika import parser
import json

raw=parser.from_file(r'D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Old\physics.pdf')
#print(raw['content'])

with open(r'D:\Python\Projects\MajorProject\ChatImplementation\PDFParser\Old\text.txt','w',encoding='utf-8') as f:
    for val in raw.items():
         f.write(str(val))

# for val in raw.items():
#     print(str(val))