#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.install()
    pisitools.dodoc("ChangeLog", "README*")
