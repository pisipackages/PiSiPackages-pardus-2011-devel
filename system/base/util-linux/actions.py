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

WorkDir="util-linux-ng-%s" % get.srcVERSION().replace("_","-")

def setup():
    shelltools.export("CFLAGS", "%s -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    shelltools.export("SUID_CFLAGS", "-fpie")
    shelltools.export("SUID_LDFLAGS", "-pie")
    shelltools.export("AUTOPOINT", "/bin/true")

    options = "--bindir=/bin \
               --sbindir=/sbin \
               --disable-login-utils \
               --disable-use-tty-group \
               --disable-makeinstall-chown \
               --disable-rpath \
               --disable-static \
               --disable-wall"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --bindir=/emul32/bin \
                     --sbindir=/emul32/sbin \
                     --libdir=/usr/lib32 \
                     --without-ncurses \
                     --disable-partx \
                     --disable-raw \
                     --disable-write \
                     --disable-libblkid \
                     --disable-mount \
                     --disable-fsck \
                     --disable-libmount \
                     --without-audit"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    else:
        options += " --enable-partx \
                     --enable-raw \
                     --enable-write \
                     --with-audit"


    autotools.autoreconf("-fi")
    autotools.configure(options)

    # Extra fedora switches:
    # --enable-login-utils will enable some utilities we ship in shadow
    # --enable-kill will enable the kill utility we ship in coreutils

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.domove("/emul32/lib32/libuuid.so", "/usr/lib32")
        pisitools.domove("/emul32/lib32/pkgconfig/uuid.pc", "/usr/lib32/pkgconfig")
        pisitools.removeDir("/emul32")

    pisitools.dodoc("AUTHORS", "COPYING", "DEPRECATED", "README*", "TODO", "docs/*")
    pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "example.files")
