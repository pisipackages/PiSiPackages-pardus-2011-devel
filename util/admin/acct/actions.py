#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "acct-6.4-pre1"

def setup():
    autotools.configure("--enable-linux-multiformat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/log/account")

    pisitools.remove("/usr/bin/last")
    pisitools.remove("/usr/share/man/man1/last.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "TODO", "COPYING", "NEWS", "README")
