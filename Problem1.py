import pandas as pd
cars = pd.read_csv('cars.csv')
flrows = cars.loc[[0,1,2,3,4,27,28,29,30,31]]

print (flrows)