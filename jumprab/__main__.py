#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for jumprab."""

import os
import sys
import yaml
import click
from .jumprab import JumpRab


@click.command()
@click.option("-c", "--config", required=True)
def main(config):
    """JumpRab, a developer's mirrors & proxies batch settings program."""

    # This script must be run as root!
    if not os.geteuid() == 0:
        sys.exit("This script must be run as root!")

    with open(config, "r") as f:
        cfg = yaml.load(f, yaml.FullLoader)

    # Parse the pip settings
    jumprab = JumpRab(cfg)
    jumprab.run()


if __name__ == "__main__":
    main()
