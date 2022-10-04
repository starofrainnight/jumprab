# -*- coding: utf-8 -*-

import re
import os
import os.path
import shutil
import click
from typing import Dict, List

from jumprab import util
from .jumper import Jumper


class FlutterJumper(Jumper):
    TAG = "flutter"
    _MARKER_BEGIN = "# FLUTTER_JUMPER_CONFIG_BEGIN"
    _MARKER_END = "# FLUTTER_JUMPER_CONFIG_END"

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        cfgs = self._cfg[self.TAG]
        pub_url = cfgs.get("pub-url")
        storage_url = cfgs.get("storage-url")

        if "SUDO_USER" in os.environ:
            user = os.environ["SUDO_USER"]
            home = "/home/%s" % user
        else:
            user = os.environ["USER"]
            home = os.path.expanduser("~")

        rc_file = os.path.join(home, ".bashrc")

        with open(rc_file, "r") as f:
            content = f.read()

        expr = "%s.*%s" % (self._MARKER_BEGIN, self._MARKER_END)
        repl = list()
        repl.append("")
        repl.append(self._MARKER_BEGIN)
        repl.append("export PUB_HOSTED_URL=%s" % pub_url)
        repl.append("export FLUTTER_STORAGE_BASE_URL=%s" % storage_url)
        repl.append(self._MARKER_END)
        repl.append("")
        repl = "\n".join(repl)

        if self._MARKER_BEGIN in content:
            replaced = re.sub(
                expr, repl, content.strip().strip("\n"), 0, re.DOTALL
            )
        else:
            replaced = content.strip() + repl

        old_rc_file = rc_file + ".old"
        util.file_clone(rc_file, old_rc_file)

        with open(os.path.expanduser(rc_file), "w") as f:
            f.write(replaced)
