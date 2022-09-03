# -*- coding: utf-8 -*-

"""Main module."""

from typing import Dict, Any
from . import jumpers

class JumpRab(object):
    def __init__(self, cfg):
        self._cfg = cfg # type: Dict[Any]

    def run(self):
        for key, value in self._cfg.items():
            if key not in jumpers:
                continue

            jumper = jumpers[key](self._cfg)
            jumper.run()



