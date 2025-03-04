from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot

cols2read = ["date","time","Column1","Column2"]

#series = read_csv('TempLog/20250217_48h.csv', header=0, parse_dates=[0],usecols=cols2read)#, index_col=0)
series = read_csv('TempLog/20250223.csv', header=0, parse_dates=[0],usecols=cols2read)#, index_col=0)
print(series.head())

print(f"Time loc {series.columns.get_loc("time")}")

#series.groupby(series["time"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)

#pyplot.plot(series.index, series["Column1"])
#pyplot.plot(series.index, series["Column2"])
#pyplot.show()


X = series.index

Y1=series['Column1']
Y2=series['Column2']

fig, ax1 = pyplot.subplots(figsize=(10,6))
ax2 = ax1.twinx()

ax1.plot(X, Y1, 'g', label='Curve.1 name') #plotting on primary Y-axis
ax2.plot(X, Y2, 'm', label='Curve.2 name') #plotting on primary Y-axis

ax1.set_ylim(0, 1048) #Define limit/scale for primary Y-axis
ax2.set_ylim(8, 24) #Define limit/scale for secondary Y-axis

pyplot.show()



# Commented out code for plotting data by year
"""
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
"""
