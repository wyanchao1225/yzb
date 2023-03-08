import pandas as pd
frame = pd.read_excel('1.xlsx',header=None)
print(frame.values[:,0])
