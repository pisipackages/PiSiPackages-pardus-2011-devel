#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mmm-mode-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-emacs \
                         --with-lispdir=/usr/share/emacs/site-lisp/mmm-mode")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doinfo("*.info*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
