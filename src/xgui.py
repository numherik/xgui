#! /usr/bin/env python3

#
#
# XLABS GUI
# Toby J. van den Herik, 2025
#
#

# Imports
import sys
from xgui_func.vars import get_sensor_info
from xgui_func.monitor import run_monitor



# Argument management
args = sys.argv[1:]

if (len(args) != 1) or not any(arg in [""] for arg in args):
    print("\n--- XGUI -- HELP ---------------------------")
    print(" XGUI takes only the following lone arguments:")
    print()
    print("  get-serials")
    print("  monitor")
    print()
    print("---------------------------------------------")
    print()

if "get-serials" in args:

    get_sensor_info()

elif "monitor" in args:

    run_monitor()