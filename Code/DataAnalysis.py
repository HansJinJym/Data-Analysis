#usage 
#python "C:\Users\Hans Jin\Desktop\PaperProject\DataAnalysis.py"

import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as pl

datapath = r'C:\Users\Hans Jin\Desktop\PaperProject\data.csv'
newpath = r'C:\Users\Hans Jin\output=0.csv'
df = pd.read_csv(datapath)
#print(df)
print(df.describe())
#print(df.sort_values(by='attr1'))
sns.lmplot("attr3","output",df, scatter_kws={"marker": ".", "color": "slategray"}, line_kws={"linewidth": 1, "color": "indianred"}).savefig('OutputToAbs')

#print(df[df.output==0])
#print(df[df.output==1])

#out0 = open('output=0','a',newline='')
#csv_write0 = csv.writer(out0,dialect='excel')
#csv_write0.write(df[df.output==0])
#out0.close()
print("over")
