# -*- coding: utf-8 -*-


import subprocess
from typing import List, Dict
from urllib.parse import urlparse
from .jumper import Jumper


class PipJumper(Jumper):
    TAG = "pip"

    def __init__(self, cfg):
        # type: (Dict) -> None

        super().__init__(cfg)

    def run(self):
        cfgs = self._cfg[self.TAG]
        urls = cfgs.get("index-urls")  # type: List[str]
        if not urls:
            return

        # Collect all hostnames
        hostnames = []
        fixed_urls = []
        for url in urls:
            # Some pip server can't be access if does not have suffix "/" at
            # the end
            if url.endswith("/"):
                fixed_urls.append(url)
            else:
                fixed_urls.append(url + "/")

            parsed = urlparse(url)
            hostnames.append(parsed.hostname)

        urls = fixed_urls

        main_url = urls[0]
        extra_urls = urls[1:]

        subprocess.run(
            ["pip", "config", "-qqq", "set", "global.index-url", main_url]
        )
        subprocess.run(
            [
                "pip",
                "config",
                "-qqq",
                "set",
                "global.trusted-host",
                "\n".join(hostnames),
            ]
        )

        if extra_urls:
            subprocess.run(
                [
                    "pip",
                    "config",
                    "-qqq",
                    "set",
                    "global.extra-index-url",
                    "\n".join(extra_urls),
                ]
            )
        else:
            # Keep quiet to unset that option
            subprocess.run(
                ["pip", "config", "-qqq", "unset", "global.extra-index-url"]
            )
