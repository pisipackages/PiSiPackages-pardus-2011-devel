#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

    for i in ["predump", "prenav","preslurp"]:
        pisitools.dosed("eg/%s" % i, "usr/local/bin/perl", "usr/bin/perl")

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    pisitools.dodoc("Changes", "README")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "eg")

