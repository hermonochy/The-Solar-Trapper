from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot

series = read_csv('2025-02-16.csv', header=0, index_col=0, parse_dates=True) #, squeeze=True)
print(series.head())

pyplot.plot(series[0], series[1])
pyplot.plot(series[0], series[2])
#pyplot.plot(series[0],series[2])
pyplot.show()

"""
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
	years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
"""
