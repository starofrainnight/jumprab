# -*- coding: utf-8 -*-


import subprocess
import os.path
from unicodedata import mirrored
import simplejson as json
from typing import List, Dict
from urllib.parse import urlparse
from .jumper import Jumper


class DockerJumper(Jumper):
    TAG = "docker"

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        cfgs = self._cfg[self.TAG]
        mirrors = cfgs.get("registry-mirrors")  # type: List
        if not mirrors:
            return

        daemon_cfg_fpath = "/etc/docker/daemon.json"
        with open(daemon_cfg_fpath) as f:
            daemon_cfgs = json.load(f)

        daemon_cfgs["registry-mirrors"] = mirrors
        with open(daemon_cfg_fpath, "w") as f:
            json.dump(daemon_cfgs, f, indent=2)
