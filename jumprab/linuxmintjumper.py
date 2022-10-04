# -*- coding: utf-8 -*-

import click
import invoke
import os.path
from typing import List, Dict
from urllib.parse import urlparse
from .jumper import Jumper


class LinuxMintJumper(Jumper):
    TAG = "linux-mint"
    ubuntu_code_dict = {
        "vanessa": "jammy",
        "una": "focal",
        "uma": "focal",
        "ulyssa": "focal",
        "ulyana": "focal",
        "tricia": "bionic",
        "tina": "bionic",
        "tessa": "bionic",
        "tara": "bionic",
        "elsie": "bullseye",
    }

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        cfgs = self._cfg[self.TAG]
        url = cfgs.get("url")  # type: str
        if not url:
            return

        try:
            ubuntu_url = self._cfg["linux-ubuntu"]["url"]
        except KeyError:
            click.echo("No 'linux-ubuntu/url' item found!")
            return

        c = invoke.Context()
        distributor_id = (
            c.run("lsb_release -i").stdout.split(":")[1].strip().lower()
        )
        if "linuxmint" not in distributor_id:
            return

        code_name = (
            c.run("lsb_release -c").stdout.split(":")[1].strip().lower()
        )

        content_expr = """
{package_type} {mint_url} {mint_code_name} main upstream import backport
{package_type} {ubuntu_url} {ubuntu_code_name} main restricted universe multiverse
{package_type} {ubuntu_url} {ubuntu_code_name}-updates main restricted universe multiverse
{package_type} {ubuntu_url} {ubuntu_code_name}-backports main restricted universe multiverse
{package_type} {ubuntu_url} {ubuntu_code_name}-security main restricted universe multiverse
"""

        content_args = {
            "mint_url": url,
            "mint_code_name": code_name,
            "ubuntu_url": ubuntu_url,
            "ubuntu_code_name": self.ubuntu_code_dict.get(code_name),
        }

        pkg_source_list = content_expr.format(
            package_type="deb", **content_args
        )

        src_source_list = content_expr.format(
            package_type="deb-src", **content_args
        )

        pkg_source_list_fpath = (
            "/etc/apt/sources.list.d/official-package-repositories.list"
        )

        src_source_list_fpath = (
            "/etc/apt/sources.list.d/official-source-repositories.list"
        )

        with open(pkg_source_list_fpath, "w") as f:
            f.write(pkg_source_list)

        if os.path.exists(src_source_list_fpath):
            with open(src_source_list_fpath, "w") as f:
                f.write(src_source_list)
