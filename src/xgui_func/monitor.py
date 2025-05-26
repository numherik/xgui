#
# The main plotter part
# Toby J. van den Herik, 2025
#

# imports
# from xgui_func.vars import xlabs_sensor_information
# import serial
# from matplotlib import pyplot as plt


# # Figure 1 - the main gui
# fig_main = plt.figure()

# ax_dt = plt.subplot2grid((4,4), (0,0), rowspan = 2, colspan = 2)
# ax_st = plt.subplot2grid((4,4), (0,2), rowspan = 2, colspan = 2)
# ax_at = plt.subplot2grid((4,4), (2,0), rowspan = 2, colspan = 2)
# ax_dp_heaters = plt.subplot2grid((4,4), (2,2), rowspan = 1, colspan = 2)
# # ax_dp_water = plt.subplot2grid((4,4), (2,3), rowspan = 1, colspan = 2)

# fig_secondary = plt.figure()
# ax_at = plt.subplot2grid((4,4), (2,0), rowspan = 2, colspan = 2)

# plt.show()

import matplotlib.pyplot as plt
import time
import random

plt.ion()  # Enable interactive mode

fig1, ax1 = plt.subplots()
ax1.set_title('Figure 1')
line1, = ax1.plot([], [])

fig2, ax2 = plt.subplots()
ax2.set_title('Figure 2')
line2, = ax2.plot([], [])

x_data1, y_data1 = [], []
x_data2, y_data2 = [], []

for i in range(100):
    x_data1.append(i)
    y_data1.append(random.randint(0, 100))
    
    x_data2.append(i)
    y_data2.append(random.randint(50, 150))
    
    line1.set_xdata(x_data1)
    line1.set_ydata(y_data1)
    ax1.relim()
    ax1.autoscale_view()
    fig1.canvas.draw()
    fig1.canvas.flush_events()
    
    line2.set_xdata(x_data2)
    line2.set_ydata(y_data2)
    ax2.relim()
    ax2.autoscale_view()
    fig2.canvas.draw()
    fig2.canvas.flush_events()
    
    time.sleep(0.1)