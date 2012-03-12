#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libfli1-%s" % get.srcVERSION()

def setup():
    cmaketools.configure("-DBUILD_ROOT=%s -DCMAKE_INSTALL_PREFIX=/%s" % (get.installDIR(), get.defaultprefixDIR()))

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("LICENSE.BSD")
