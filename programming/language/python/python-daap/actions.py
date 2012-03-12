#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PythonDaap-%s" % get.srcVERSION()

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto(examples, "examples/*")

    pisitools.dodoc("CHANGELOG", "LICENSE", "README")
