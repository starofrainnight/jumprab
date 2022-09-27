# -*- coding: utf-8 -*-

"""Main module."""

import click
from typing import Dict, Any
from . import jumpers, get_jumper_map


class JumpRab(object):
    def __init__(self, cfg):
        self._cfg = cfg  # type: Dict[Any]

    def run(self):
        jumper_map = get_jumper_map()

        for key, value in self._cfg.items():
            jumper_class = jumper_map.get(key)
            if not jumper_class:
                continue

            click.echo("Jumping %s ..." % key)

            jumper = jumper_class(self._cfg)
            jumper.run()
