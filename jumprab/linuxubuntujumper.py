# -*- coding: utf-8 -*-

from typing import Dict
from .jumper import Jumper


class LinuxUbuntuJumper(Jumper):
    TAG = "linux-ubuntu"

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        pass
