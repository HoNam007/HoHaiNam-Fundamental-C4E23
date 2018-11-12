import pyexcel
from collections import OrderedDict

#2 Prepare data
data= [
    OrderedDict({
        "Name": "Nam",
        "Age": 24,
    }),
    OrderedDict({
        "Name": "Quan",
        "Age": "28"
    }),
]

# List comprehension
#3 Save flie using save_as()
pyexcel.save_as(records=data, dest_file_name="sample.xls")