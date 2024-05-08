#!/usr/bin/env python


def main():
    my_bytes = [
        0x3B,
        0x65,
        0x21,
        0xA,
        0x38,
        0x0,
        0x36,
        0x1D,
        0xA,
        0x3D,
        0x61,
        0x27,
        0x11,
        0x66,
        0x27,
        0xA,
        0x21,
        0x1D,
        0x61,
        0x3B,
        0xA,
        0x2D,
        0x65,
        0x27,
        0xA,
        0x66,
        0x36,
        0x30,
        0x67,
        0x6C,
        0x64,
        0x6C,
    ]
    pass_bytes = [0 for _ in range(32)]
    for i in range(32):
        # | or
        # & and
        # ^ xor
        # pass_bytes[i] ^ 0x55 - my_bytes[i] = 0
        # xor A B = C
        # A = xor B C
        pass_bytes[i] = my_bytes[i] ^ 0x55
    print(''.join(chr(b) for b in pass_bytes))


if __name__ == "__main__":
    main()
