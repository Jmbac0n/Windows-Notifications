from win10toast import ToastNotifier
from win32api import GetModuleHandle

import os, sys, datetime, requests, json

toaster = ToastNotifier()

os_name = os.name
user = os.getlogin()

today = datetime.datetime.now()
time = (str(today))
log_time = time[0:19]

toaster.show_toast("Logged in:", "OS: " + (os_name) + "\n" + "User: " + (user) + "\n" + (log_time), threaded=True, icon_path=None, duration=5)
