# to install pip, format: py -m pip install module name
import camelcase

c = camelcase.CamelCase()

txt='hello word'

print(c.hump(txt))
