#!/usr/bin/env python

import re
from icecream import ic
from struct import pack

pat = re.compile(r"x\[(\d)\]\s*==\s*(\d+)")


def main():
    with open("./VaultDoor7.java", "r") as f:
        content = f.read()
    res = re.findall(pat, content)
    ic(res)

    for _, i in res:
        ic(pack("<l", int(i)))

    r = list(pack(">l", int(i)) for _, i in res)
    ic(r)
    rr = b"".join(r).decode()
    ic(rr)


if __name__ == "__main__":
    main()
