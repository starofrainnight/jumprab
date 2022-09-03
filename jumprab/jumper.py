# -*- coding: utf-8 -*-

from typing import Dict, Any


class Jumper(object):
    def __init__(self, cfg):
        # type: (Dict) -> None

        self._cfg = cfg

    def run(self):
        raise NotImplementedError()
