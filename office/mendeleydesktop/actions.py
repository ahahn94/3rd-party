#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("tar xf mendeleydesktop-%s-linux-x86_64.tar.bz2" % Version)
    shelltools.system("cd mendeleydesktop-%s-linux-x86_64/share/applications/ && mv mendeleydesktop.desktop 'Mendeley Desktop.desktop'" % Version)
    shelltools.system("sed -i 's/mendeleydesktop/Mendeley Destkop/' mendeleydesktop-%s-linux-x86_64/bin/install-mendeley-link-handler.sh" % Version)

def install():
    for component in ["bin", "lib", "share"]:
        pisitools.insinto("/opt/mendeley/", "mendeleydesktop-%s-linux-x86_64/%s" % (Version, component))

    pisitools.dodir("/usr/share/applications")
    pisitools.dosym("/opt/mendeley/bin/mendeleydesktop", "/usr/bin/mendeleydesktop")
    pisitools.dosym("/opt/mendeley/share/applications/Mendeley Desktop.desktop", "/usr/share/applications/Mendeley Desktop.desktop")

    for icon_size in ["16", "22", "32", "48", "64", "128"]:
        pisitools.dodir("/usr/share/icons/hicolor/%sx%s" % (icon_size, icon_size))
        pisitools.dosym("/opt/mendeley/share/icons/hicolor/%sx%s/apps/mendeleydesktop.png" % (icon_size, icon_size),
                        "/usr/share/icons/hicolor/%sx%s/apps/mendeleydesktop.png" % (icon_size, icon_size))
