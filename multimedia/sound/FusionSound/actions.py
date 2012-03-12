#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "core/FusionSound.git/"
KeepSpecial = ["libtool"]

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.rename("/usr/bin/fsdump", "FusionSound-dump")
    pisitools.remove("/usr/lib/*.la")

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("AUTHORS")
