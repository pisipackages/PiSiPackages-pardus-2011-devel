# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

arch = get.ARCH().replace("i686", "x86")
version = get.srcVERSION()
driver = "nvidia96"
libdir = "/usr/lib/%s" % driver
datadir = "/usr/share/%s" % driver

def setup():
    shelltools.system("sh NVIDIA-Linux-%s-%s-pkg0.run -x --target tmp" % (arch, version))
    shelltools.move("tmp/*", ".")

    shelltools.system("patch -p0 < no-smbus.patch")

    # Our libc is TLS enabled so use TLS library
    shelltools.unlink("usr/lib/*-tls.so*")
    shelltools.move("usr/lib/tls/*", "usr/lib")
    shelltools.unlinkDir("usr/lib/tls")

    shelltools.echo("ld.so.conf", libdir)
    shelltools.echo("XvMCConfig", "%s/libXvMCNVIDIA.so" % libdir)

def build():
    shelltools.export("SYSSRC", "/lib/modules/%s/build" % KDIR)
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.insinto("/lib/modules/%s/extra/nvidia" % KDIR, "usr/src/nv/nvidia.ko", "%s.ko" % driver)

    # Libraries and X modules
    pisitools.insinto(libdir, "usr/X11R6/lib/*")
    pisitools.insinto(libdir, "usr/lib/*")

    # Symlinks
    pisitools.dosym("libGL.so.%s" % version, "%s/libGL.so.1.2" % libdir)
    pisitools.dosym("libGLcore.so.%s" % version, "%s/libGLcore.so.1" % libdir)

    pisitools.dosym("libXvMCNVIDIA.so.%s" % version, "%s/libXvMCNVIDIA.so.1" % libdir)
    pisitools.dosym("libXvMCNVIDIA.so.1", "%s/libXvMCNVIDIA.so" % libdir)

    pisitools.dosym("libnvidia-cfg.so.%s" % version, "%s/libnvidia-cfg.so.1" % libdir)
    pisitools.dosym("libnvidia-tls.so.%s" % version, "%s/libnvidia-tls.so.1" % libdir)

    pisitools.dosym("libglx.so.%s" % version, "%s/modules/extensions/libglx.so" % libdir)

    # Remove static libraries
    pisitools.remove("%s/*.a" % libdir)

    pisitools.insinto(datadir, "ld.so.conf")
    pisitools.insinto(datadir, "XvMCConfig")

    # Documentation
    docdir = "xorg-video-%s" % driver
    pisitools.dodoc("LICENSE", destDir=docdir)
    pisitools.dodoc("usr/share/doc/[!h]*", destDir=docdir)
    pisitools.dohtml("usr/share/doc/html/*", destDir=docdir)
