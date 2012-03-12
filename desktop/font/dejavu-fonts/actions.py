#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/BİLGEM-UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make("full-ttf")

def check():
    autotools.make("check")

def install():
    pisitools.insinto("/usr/share/fonts/dejavu", "build/*.ttf")

    # Create symlinks for fontconfig files
    for conf in shelltools.ls("fontconfig"):
        pisitools.insinto("/etc/fonts/conf.avail", "fontconfig/%s" % conf)
        pisitools.dosym("/etc/fonts/conf.avail/%s" % conf, "/etc/fonts/conf.d/%s" % conf)


    pisitools.dosym("/usr/share/fonts/dejavu" , "/etc/X11/fontpath.d/dejavu")

    pisitools.dodoc("AUTHORS", "LICENSE", "NEWS", "README")
