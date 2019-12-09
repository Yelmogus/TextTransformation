import pandas as ps
from pandas import ExcelWriter
from pandas import ExcelFile

df = ps.read_excel('TestCasesExamples/find_title tests.xlsx', sheetname='Sheet1')
print("Colum headings:")
print(df.columns)

import sys
sys.path.insert(1, "../src")
import get_title as g_t
import math
for i in df.index:
    print(str(df['Test Input'][i]))
    print("o:'" + g_t.get_title(str(df['Test Input'][i])) + "'")
