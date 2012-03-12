#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("dstat")

    pisitools.insinto("/usr/share/dstat", "plugins/*.py")

    pisitools.doman("docs/dstat.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "TODO", "examples/mstat.py", "examples/read.py")
