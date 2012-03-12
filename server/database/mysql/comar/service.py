# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType="server"
serviceDesc = _({"en": "MySQL Database Server",
                 "tr": "MySQL Veritabanı Sunucusu"})

PIDFILE = "/var/run/mysqld/mysqld.pid"

@synchronized
def start():
    startService(command="/usr/sbin/mysqld",
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
