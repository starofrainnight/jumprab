#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for jumprab."""

import yaml
import click
from .jumprab import JumpRab


@click.command()
@click.option("-c", "--config", required=True)
def main(config):
    """JumpRab, a developer's mirrors & proxies batch settings program."""
    with open(config, "r") as f:
        cfg = yaml.load(f, yaml.FullLoader)

    # Parse the pip settings
    jumprab = JumpRab(cfg)
    jumprab.run()


if __name__ == "__main__":
    main()
