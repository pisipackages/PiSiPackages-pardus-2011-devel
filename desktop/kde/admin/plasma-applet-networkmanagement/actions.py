#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())
WorkDir = "networkmanagement"
NoStrip=["/usr/share/icons"]

def setup():
    kde4.configure("-DDBUS_SYSTEM_POLICY_DIR=/etc/dbus-1/system.d")

def build():
    kde4.make()

def install():
    kde4.install()
