#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pyvorbis-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.system("./config_unix.py")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")

    shelltools.chmod("test/*", 0644)
    pisitools.insinto(examples, "test/*")

