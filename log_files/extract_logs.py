import os
from datetime import datetime, timedelta, time

def send_ping(interval:int, count:int, host:str) -> str:
    '''

    :param interval:
    :param count:
    :param host:
    :return: name of saved file
    '''
    pings = os.system('ping -i {} -c {} -n {} > ping_{}.txt'.format(interval,
                                                                    count,
                                                                    host,
                                                                    datetime.now().strftime('%d-%m-%Y_%H:%M')))

    return('ping_{}.txt'.format(datetime.now().strftime('%d-%m-%Y %H:%M')))
