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

WorkDir="fftw-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")

    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-double" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-long-double" % get.srcVERSION())

    autotools.configure("--enable-sse \
                         --enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads \
                         --enable-single")

    # The only difference here is that there is no --enable-float
    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.configure("--enable-sse2 \
                         --enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads")

    # The only difference here is --enable-long-double
    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.configure("--enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads \
                         --enable-long-double")

def check():
    autotools.make("check")

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.make("check")

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.make("check")

def build():
    autotools.make()

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s" % get.srcVERSION())

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO", "CONVENTIONS")
