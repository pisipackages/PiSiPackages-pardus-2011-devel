#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s USE_CAP=yes" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("lddtree.sh")
