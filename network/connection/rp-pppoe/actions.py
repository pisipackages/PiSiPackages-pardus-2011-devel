#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=\"%s\" docdir=/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))

    # Install symnlinks for easier usage
    for f in ["connect", "relay", "server", "setup", "sniff", "start", "status", "stop"]:
        pisitools.dosym("pppoe-%s" % f, "/usr/sbin/adsl-%s" % f)
