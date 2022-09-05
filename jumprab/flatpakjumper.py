# -*- coding: utf-8 -*-


import subprocess
import os.path
from typing import List, Dict
from urllib.parse import urlparse
from .jumper import Jumper


class FlatpakJumper(Jumper):
    TAG = "flatpak"

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        cfgs = self._cfg[self.TAG]
        remotes = cfgs.get("remotes")  # type: Dict
        if not remotes:
            return

        for name, url in remotes.items():
            subprocess.run(
                [
                    "flatpak",
                    "remote-add",
                    "--if-not-exists",
                    name,
                    os.path.join(url, "flathub.flatpakrepo"),
                ]
            )

            subprocess.run(
                ["flatpak", "remote-modify", name, "--url=%s" % url]
            )
