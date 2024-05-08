#!/usr/bin/env python


def main():
    buffer = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"
    passwd = ["" for _ in range(32)]

    i = 0
    while i < 8:
        passwd[i] = buffer[i]
        i += 1

    while i < 16:
        passwd[23 - i] = buffer[i]
        i += 1

    while i < 32:
        passwd[46 - i] = buffer[i]
        i += 2

    i = 31
    while i >= 17:
        passwd[i] = buffer[i]
        i -= 2

    print("".join(passwd))


if __name__ == "__main__":
    main()
