#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", get.LDFLAGS())

    autotools.configure("--enable-gpl \
                         --enable-shared \
                         --enable-shared-pp \
                         --enable-pp \
                         --enable-motion-est \
                         --avformat-vdpau \
                         --avformat-swscale")

    # Enable bindings
    shelltools.echo("%s/src/swig/config.mak" % get.curDIR(), "SUBDIRS = perl python")

def build():
    autotools.make()
    autotools.make("-C src/swig")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We should manually install the bindings :(
    pisitools.insinto("/usr/lib/%s/site-packages/" % get.curPYTHON(), "src/swig/python/mlt.py")
    pisitools.dolib("src/swig/python/_mlt.so", "/usr/lib/%s/site-packages/" % get.curPYTHON())

    pisitools.insinto("/usr/lib/perl5/vendor_perl/%s/" % get.curPERL(), "src/swig/perl/blib/lib/mlt.pm")
    pisitools.dolib("src/swig/perl/blib/arch/auto/mlt/mlt.so", "/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi/auto/mlt/" % get.curPERL())

    pisitools.dodoc("ChangeLog", "COPYING", "GPL", "README")
