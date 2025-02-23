from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from matplotlib.dates import bytespdate2num

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


datafile = "2025-02-16.csv" #cbook.get_sample_data('msft.csv', asfileobj=False)
print('loading', datafile)

dates, closes = np.loadtxt(datafile, delimiter=',',
                           #converters={0: bytespdate2num('%d-%b-%y')},
                           converters={0: bytespdate2num('%d-%m-%Y')},
                           skiprows=1, usecols=(0, 2), unpack=True)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(dates, closes, '-')
fig.autofmt_xdate()
plt.show()
