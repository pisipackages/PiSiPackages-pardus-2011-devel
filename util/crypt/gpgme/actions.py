#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--includedir=/usr/include/gpgme \
                         --with-gpg=/usr/bin/gpg2 \
                         --with-pth=yes \
                         --with-gpgsm=/usr/bin/gpgsm")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/libexec")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
