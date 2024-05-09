#!/usr/bin/env python

from icecream import ic

"""
password_bit ->  switch_bit -> switch_bit -> password_bit

So when scramble a two char passwd, it does:
```
char1:
1st switch_bit --> 2nd switch_bit .. 8th switch_bit
-->
char2:
1st switch_bit --> 2nd switch_bit .. 8th switch_bit
```

So the reverse of scramble should be like:
```
char2:
8th switch_bit --> 7th switch_bit .. 1st switch_bit
-->
char1:
8th switch_bit --> 7th switch_bit .. 1st switch_bit
```

note that we don't swap chars, so this is fine to do:
```
char1:
8th switch_bit --> 7th switch_bit .. 1st switch_bit
-->
char2:
8th switch_bit --> 7th switch_bit .. 1st switch_bit
```
"""


def switch_bit(num, p1, p2):
    if not isinstance(num, int):
        n = ord(num)
    else:
        n = num
    m1 = 1 << p1
    m2 = 1 << p2
    b1 = n & m1
    b2 = n & m2
    rest = n & ~(m1 | m2)
    s = p2 - p1
    res = b1 << s | (b2 >> s) | rest
    return res


def scramble(s: str):
    for i in range(len(s)):
        c = s[i]

        # 2 3 6 7 0 1 4 5
        c = switch_bit(c, 6, 7)
        # 2 3 6 7 0 1 5 4
        c = switch_bit(c, 2, 5)
        # 2 3 1 7 0 6 5 4
        c = switch_bit(c, 3, 4)
        # 2 3 1 0 7 6 5 4
        c = switch_bit(c, 0, 1)
        # 3 2 1 0 7 6 5 4
        c = switch_bit(c, 4, 7)
        # 3 2 1 0 4 6 5
        c = switch_bit(c, 5, 6)
        # 3 2 1 0
        c = switch_bit(c, 0, 3)
        # 0 2 1
        c = switch_bit(c, 1, 2)
        # 0 1 2 3 4 5 6 7
        s[i] = c
    return s


def main():
    buf = [
        0xF4,
        0xC0,
        0x97,
        0xF0,
        0x77,
        0x97,
        0xC0,
        0xE4,
        0xF0,
        0x77,
        0xA4,
        0xD0,
        0xC5,
        0x77,
        0xF4,
        0x86,
        0xD0,
        0xA5,
        0x45,
        0x96,
        0x27,
        0xB5,
        0x77,
        0xD2,
        0xD0,
        0xB4,
        0xE1,
        0xC1,
        0xE0,
        0xD0,
        0xD0,
        0xE0,
    ]
    res = scramble(buf)
    ic(res)
    r = "".join(chr(a) for a in res)
    ic(r)

    pass


if __name__ == "__main__":
    main()
