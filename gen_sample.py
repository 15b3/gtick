import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from src.gtick import JDayHourFormatter

np.random.seed(12)
max_ft = 78
ft = np.array([i for i in range(1, max_ft + 1)])
y = np.random.normal(size=max_ft) + 0.2 * ft

# sample a
bt = np.datetime64("2023-03-21T00:00")
vt = bt + ft.astype("timedelta64[h]")
fig, axes = plt.subplots(figsize=(6.4*2, 2.4))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.30, top=0.85)

axes.set_title("sample_a")
axes.plot(vt, y)
axes.xaxis.set_major_locator(mdates.HourLocator(byhour=[i for i in range(0, 24, 3)]))
axes.xaxis.set_major_formatter(JDayHourFormatter())
plt.savefig("png/sample_a.png")


# sample b
bt = np.datetime64("2022-12-30T06:00")
vt = bt + ft.astype("timedelta64[h]")
fig, axes = plt.subplots(figsize=(6.4*2, 2.4))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.30, top=0.85)

axes.set_title("sample_b")
axes.plot(vt, y)
axes.xaxis.set_major_locator(mdates.HourLocator(byhour=[i for i in range(0, 24, 3)]))
axes.xaxis.set_major_formatter(JDayHourFormatter())
plt.savefig("png/sample_b.png")

# sample c
bt = np.datetime64("2023-03-30T21:00")
vt = bt + ft.astype("timedelta64[h]")
fig, axes = plt.subplots(figsize=(6.4*2, 2.4))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.30, top=0.85)

axes.set_title("sample_c: start_pos=1")
axes.plot(vt, y)
axes.xaxis.set_major_locator(mdates.HourLocator(byhour=[i for i in range(0, 24, 3)]))
axes.xaxis.set_major_formatter(JDayHourFormatter(start_pos=1))
plt.savefig("png/sample_c.png")

# sample d
bt = np.datetime64("2023-03-30T21:00")
vt = bt + ft.astype("timedelta64[h]")
fig, axes = plt.subplots(figsize=(6.4*2, 2.4))
fig.subplots_adjust(left=0.05, right=0.98, bottom=0.30, top=0.85)

axes.set_title("sample_d: ji=True, year=False")
axes.plot(vt, y)
axes.xaxis.set_major_locator(mdates.HourLocator(byhour=[i for i in range(0, 24, 3)]))
axes.xaxis.set_major_formatter(JDayHourFormatter(start_pos=1, ji=True, year=False))
plt.savefig("png/sample_d.png")
