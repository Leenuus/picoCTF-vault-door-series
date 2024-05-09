#!/usr/bin/env python

import re
from icecream import ic
from struct import pack

# extract all relevant number from the source code
pat = re.compile(r"x\[(\d)\]\s*==\s*(\d+)")


def main():
    with open("./VaultDoor7.java", "r") as f:
        content = f.read()
    res = re.findall(pat, content)
    ic(res)

    # NOTE: pack this integer to a 32bit(4 byte) big endian bytes string
    r = list(pack(">l", int(i)) for _, i in res)
    ic(r)
    rr = b"".join(r).decode()
    ic(rr)


if __name__ == "__main__":
    main()
