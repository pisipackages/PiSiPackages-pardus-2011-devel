#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

# https://savannah.nongnu.org/bugs/?22368
# https://bugs.gentoo.org/273372
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: Fedora removes it, Suse keeps it, breaks samba build, investigate further
    pisitools.remove("/usr/lib/libunwind*.a")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")
