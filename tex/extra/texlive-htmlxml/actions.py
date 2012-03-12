# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from distutils.dir_util import copy_tree

WorkDir = "%s" % get.srcNAME()

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls('.'):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["tlpkg"]:
        shelltools.unlinkDir(folder)

def install():
    pisitools.dodir("/usr/share")

    wanteddirs = []
    for file_ in shelltools.ls('.'):
        if shelltools.isDirectory(file_) and not "texmf" in file_:
            wanteddirs.append(file_)

    for folder in wanteddirs:
        pisitools.insinto("/usr/share/texmf-dist", folder)

    if shelltools.can_access_directory("texmf-dist"):
        # Recursively copy on directory on top of another, overwrite duplicate files too
        copy_tree("texmf-dist", "%s/usr/share/texmf-dist" % get.installDIR())

    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)

    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/ht.sh" ,"/usr/bin/ht")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/htcontext.sh" ,"/usr/bin/htcontext")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/htlatex.sh" ,"/usr/bin/htlatex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/htmex.sh" ,"/usr/bin/htmex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/httex.sh" ,"/usr/bin/httex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/httexi.sh" ,"/usr/bin/httexi")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/htxelatex.sh" ,"/usr/bin/htxelatex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/htxetex.sh" ,"/usr/bin/htxetex")
    pisitools.dosym("/usr/share/texmf-dist/scripts/tex4ht/mk4ht.pl" ,"/usr/bin/mk4ht")
