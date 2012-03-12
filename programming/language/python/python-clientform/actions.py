#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ClientForm-%s" % get.srcVERSION()

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME()) 

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog.txt", "COPYING.txt", "README.txt")
    pisitools.dohtml("GeneralFAQ.html")
    pisitools.remove("/usr/share/doc/python-clientform/README.html.in")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*") 

