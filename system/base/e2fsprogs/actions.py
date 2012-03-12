#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--enable-elf-shlibs \
                            --disable-e2initrd-helper \
                            --disable-libblkid \
                            --disable-libuuid \
                            --disable-fsck \
                            --disable-uuidd")

def build():
    autotools.make()

def check():
    # remove sandbox violating test
    shelltools.unlinkDir("%s/e2fsprogs-%s/tests/f_ext_journal/" % (get.workDIR(), get.srcVERSION()))
    autotools.make("check")

def install():
    autotools.rawInstall("install install-libs LDCONFIG=/bin/true \
                          DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % get.installDIR())

    # Unneeded stuff
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("README", "RELEASE-NOTES")
