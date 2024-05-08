#!/usr/bin/env python

from base64 import b64decode

s = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
)


def urldecode(s: str | bytes) -> str:
    """
    In fact, ascii characters are not encoded in standard urlencode
    """
    if isinstance(s, bytes):
        s = s.decode()
    s2 = s.replace("%", "")
    return bytearray.fromhex(s2).decode()


def main():
    print(urldecode(b64decode(s)))
    print(urldecode(b64decode(s).decode()))


if __name__ == "__main__":
    main()
