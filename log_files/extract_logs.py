import os
from datetime import datetime, timedelta, time

def send_ping(ip):
    pings = os.system('ping -i 1 -c 2 -n {} > ping_{}.txt'.format(ip, datetime.now().strftime('%d-%m-%Y_%H:%M')))
    return('ping_{}.txt'.format(ip, datetime.now().strftime('%d-%m-%Y %H:%M')))

send_ping('www.google.com')