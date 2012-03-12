#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pp-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.rename("/usr/bin/ppserver.py", "ppserver")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples/")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/example.config")
    pisitools.doman("doc/ppserver.1")
