import pandas as ps
from pandas import ExcelWriter
from pandas import ExcelFile

df = ps.read_excel('TestCasesExamples/find_title tests.xlsx', sheetname='Sheet1')
print("Colum headings:")
print(df.columns)

import sys
sys.path.insert(1, "../src")
import strip_input as s_i
import math

#script tag case
print(s_i.strip_input("<script> this text is within script tags </script> <p>this isn't.</p>"))
#no space case
print(s_i.strip_input("<p>this spaces please</p><p>don't this isn't.</p>"))
#comment case
print(s_i.strip_input("<p>this spaces please</p><!--This a comment! --><p>don't this isn't.</p>"))
#none case
print(s_i.strip_input(""))

#for i in df.index:
#    print(str(df['Test Input'][i]))
#    print("o:'" + g_t.get_title(str(df['Test Input'][i])) + "'")
