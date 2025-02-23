from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot

series = read_csv('2025-02-16.csv', header=0, parse_dates=[0], index_col=0)
print(series.head())

pyplot.plot(series.index, series['Column1'])
pyplot.plot(series.index, series['Column2'])
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