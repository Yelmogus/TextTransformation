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

failed = 0
for i in df.index:
    result = g_t.get_title(str(df['Test Input'][i]))
    out = str(df['Expected Output'][i])
    if out == 'nan':
        out = ''
    if out != result:
        failed += 1
        print("Test " + str(i) + " failed")
        print(str(df['Test Input'][i]))
        print("unexpected result:'" + result + "'")
        print("expected:'" + str(df['Expected Output'][i]) + "'")
print("Passed " + str(i-failed) + " tests out of " + str(i))
