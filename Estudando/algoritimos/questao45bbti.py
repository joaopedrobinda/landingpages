import pandas as pd
data = {'x':[1,2,3], 'y':[3, 7, 11], 'z': [False, True, False]}
df = pd.DataFrame(data)
m = df['z'] == False
ef = df[m]
ff = ef[['x','y']]
print(ff)