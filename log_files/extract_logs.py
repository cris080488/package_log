import os
from datetime import datetime, timedelta, time

ip = 'www.google.com'

log = open('ping_log.txt', 'a')
pings = os.system('ping -i 1 -c 4 -n {} > ping_{}.txt'.format(ip, datetime.now().strftime('%d-%m-%Y_%H:%M')))


