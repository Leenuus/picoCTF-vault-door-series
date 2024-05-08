#!/usr/bin/env python

import re
from icecream import ic
from operator import itemgetter

pat = re.compile(r"\s*password\.charAt\((\d+)\)\s*==\s*'(.)'")


def main():
    with open("./VaultDoor1.java", "r") as f:
        content = f.read()

    ms = re.findall(pat, content)
    ic(ms)
    rs = sorted(((int(a), b) for a, b in ms), key=itemgetter(0))
    ic(rs)
    res = "".join(c for _, c in rs)
    ic(res)


if __name__ == "__main__":
    main()
