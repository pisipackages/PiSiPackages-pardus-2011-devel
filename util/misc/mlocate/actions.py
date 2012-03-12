#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--localstatedir=/%s/lib \
                         --disable-rpath" % get.localstateDIR())

def build():
    autotools.make("groupname=slocate")

def install():
    autotools.rawInstall("DESTDIR=%s groupname=slocate" % get.installDIR())

    pisitools.dodoc("AUTHORS","COPYING", "NEWS", "README", "doc/mlocate.cron.example")
