import pandas as pd
from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot


cols2read = ["date","time","Column1","Column2"]

#series = read_csv('TempLog/20250217_48h.csv', header=0, parse_dates=[0],usecols=cols2read)#, index_col=0)
series = read_csv('20250223.csv', header=0, parse_dates=[0],usecols=cols2read)  #, index_col=0)
print(series.head())

#series["pandasdatetime"] = series["date"].astype(str)+series["time"].astype(str) # Doesn't plot!
series["pandasdatetime"]=pd.to_datetime([str(date) + ' ' + str(time) for date,time in zip(series["date"],series["time"])])
print(series.head())

print(f"Time loc {series.columns.get_loc("time")}")

#series.groupby(series["time"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)

#pyplot.plot(series.index, series["Column1"])
#pyplot.plot(series.index, series["Column2"])
#pyplot.show()

X = series["pandasdatetime"] #series.index

Y1=series['Column1']
Y2=series['Column2']


fig, ax1 = pyplot.subplots(figsize=(10,6))
ax2 = ax1.twinx()

ax1.plot(X, Y1, 'g', label='Light intensity')
ax2.plot(X, Y2, 'm', label='Temperature')

ax1.set_ylabel("Light Level: sunny if < 15")
ax2.set_ylabel("Temperature [Celcius]")

ax1.set_ylim(0, 1048)
ax2.set_ylim(8, 24)
#pyplot.gca().legend(('Y1','Y2'))
ax1.legend(loc='best')
ax2.legend(loc='best')

pyplot.axvline(pd.to_datetime("2025-02-24 22:58:53"), color = 'r', label = "Curtain Closing Time")
pyplot.legend()

pyplot.title("Sensor Data Log and Curtain Closing Inference")

pyplot.show()

"""
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
"""
