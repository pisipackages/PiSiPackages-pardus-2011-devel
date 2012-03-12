#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nose-%s" % get.srcVERSION()

examples = "%s/%s/" % (get.docDIR(), get.srcNAME())

def install():
    pisitools.dosed("setup.py", "man/man1", "share/man/man1")

    pythonmodules.install()

    pisitools.dohtml("doc/*")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*")
