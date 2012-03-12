#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer", ""))
    shelltools.export("LDFLAGS", get.LDFLAGS())

    autotools.rawConfigure("-prefix /usr \
                            -bindir /usr/bin \
                            -libdir /usr/lib/ocaml \
                            -mandir /usr/share/man \
                            --with-pthread \
                            --tklibs ")

def build():
    autotools.make("-j1 world")
    autotools.make("-j1 opt")
    autotools.make("-j1 opt.opt")
    autotools.make("-C emacs ocamltags")

def install():
    autotools.rawInstall("BINDIR=%(install)s/usr/bin \
                          LIBDIR=%(install)s/usr/lib/ocaml \
                          MANDIR=%(install)s/usr/share/man" \
                          % { "install": get.installDIR()})

    pisitools.dodoc("Changes", "LICENSE", "README", "Upgrading")

    pisitools.insinto("/usr/share/doc/ocaml/otherlibs/labltk","otherlibs/labltk/examples_*")

    autotools.rawInstall("-C emacs \
                        BINDIR=%(install)s/usr/bin \
                        EMACSDIR=%(install)s/usr/share/emacs/site-lisp"
                        % { "install": get.installDIR()})


    # Remove rpaths from stublibs .so files
    shelltools.system("chrpath --delete %s/usr/lib/ocaml/stublibs/*.so" 
                    % get.installDIR())
