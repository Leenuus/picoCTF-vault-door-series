#!/usr/bin/env python

from base64 import b64decode

s = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
)


def urldecode(s: str) -> str:
    """
    A dirty way to do urldecode
    """
    s1 = s.replace("%%", "%")
    s2 = s1.replace("%", r"\x")
    s3 = eval(f'"{s2}"')
    return s3


def main():
    print(urldecode(b64decode(s).decode()))


if __name__ == "__main__":
    main()
