#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_ENABLE_SHARED=YES")

def build():
    cmaketools.make()

    shelltools.cd("scripts/python")
    pythonmodules.compile()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("scripts/python")
    pythonmodules.install()
    shelltools.cd("../..")

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "THANKS")
