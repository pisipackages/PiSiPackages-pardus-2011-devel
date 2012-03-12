#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --bindir=/bin \
                         --sbindir=/sbin \
                         --enable-pam-module-dir=/lib/security \
                         --enable-initscript-install")

def build():
    autotools.make("V=1")

# 2 sets of tests fail under sandbox
"""
def check():
    pisitools.dosed("tests/runlibcgrouptest.sh", "^DEBUG=false.*$", "DEBUG=true")
    autotools.make("check DEBUG=true")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/cgroup")

    pisitools.insinto("/etc", "samples/cgconfig.conf")
    pisitools.insinto("/etc", "samples/cgrules.conf")
    pisitools.insinto("/etc/conf.d", "samples/cgred.conf", "cgred")
    pisitools.insinto("/etc/conf.d", "samples/cgconfig.sysconfig", "cgconfig")

    pisitools.dodoc("COPYING", "README*")
