from tika import parser
import json

raw=parser.from_file('ScienceTextBook.pdf')
#print(raw['content'])

with open('text.txt','w') as f:
    for val in raw.items():
         f.write(str(val))

# for val in raw.items():
#     print(str(val))