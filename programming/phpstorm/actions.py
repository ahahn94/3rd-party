#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "261.22158.283"

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm", "/usr/bin/phpstorm")
