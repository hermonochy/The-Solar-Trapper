import pandas as pd
import numpy as np
from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

cols2read = ["date","time","Column1","Column2"]

closingTimeData = read_csv("closingTimes.txt", usecols=[0], names=["datetime"], parse_dates=[0])
print(closingTimeData)
closingTimeArray = closingTimeData["datetime"]

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

x_anim, y1_anim, y2_anim = [], [], []

fig, ax1 = pyplot.subplots(figsize=(10,6))
ax2 = ax1.twinx()

ln1, = ax1.plot(X, Y1, 'g', label='Light intensity')
ln2, = ax2.plot(X, Y2, 'm', label='Temperature')

ax1.set_ylabel("Light Level: sunny if < 15")
ax2.set_ylabel("Temperature [Celcius]")


def init():
    ax1.set_ylim(0, 1048)
    ax2.set_ylim(8, 24)
    #pyplot.gca().legend(('Y1','Y2'))
    ax1.legend(loc='lower right')
    ax2.legend(loc='upper right')


    return ln1, ln2,

def update(nextTimeIndex):
    x_anim.append(X[nextTimeIndex])
    y1_anim.append(Y1[nextTimeIndex])
    y2_anim.append(Y2[nextTimeIndex])


    for idx, closetime in enumerate(closingTimeArray):
        currentPlotTime = X[nextTimeIndex].timestamp()
        if abs(closetime.timestamp()-currentPlotTime) < 500:
            ax1.axvline(x=closetime, linestyle='--', color='red', label="closing times")
    """
    if nextTimeIndex>80000:
        for idx, closetime in enumerate(closingTimeArray):
            if idx == 0:
                ax1.axvline(x=closetime, linestyle='--', color='red', label="closing times")
            else:
                ax1.axvline(x=closetime, linestyle='--', color='red')
    """


    ln1.set_data(x_anim,y1_anim)
    ln2.set_data(x_anim,y2_anim)
    return ln1, ln2,

anim = FuncAnimation(fig, update, frames=np.linspace(0,len(X)-1,1000, dtype=int), init_func=init, blit=False, interval=0.1)    



# pyplot.axvline(pd.to_datetime(closingTimeData["datetime"])[0], color = 'r', label = "Curtain Closing Time")
# for datetime in pd.to_datetime(closingTimeData["datetime"]):
#     pyplot.axvline(datetime, color = 'r')
# pyplot.legend(loc='upper left')


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
