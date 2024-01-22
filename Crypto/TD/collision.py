#!/usr/bin/env python3

import hashlib
import sys

N = 5


def show_hex(bs):
    print("0x", end="")
    for b in bs:
        print(f"{b:02x}", end="")
    print()


def H(bs):
    return hashlib.md5(bytearray(str(bs), encoding="ASCII")).digest()[0:N]
    # return hashlib.md5(bs).digest()[0:N]


def collision(s):
    s = 0
    all_s = {s}
    all_h = {H(s)}
    while True:
        s = s+1  # on fait une modification de s
        h = H(s)
        assert s not in all_s
        if h in all_h:
            break  # on a trouvÃ© une collision
        all_s.add(s)
        all_h.add(h)
    for t in all_s:
        if h == H(t):
            print(f"collision: {s} / {t} aprÃ¨s {len(all_h)} empreintes calculÃ©es")
            return s, t
    else:
        assert False


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} INIT")
        sys.exit(1)

    s = int(sys.argv[1])
    # s = sys.argv[1].encode()
    bs1, bs2 = collision(s)

    assert H(bs1) == H(bs2)

    print(f"'{bs1}' / '{bs2}' => ", end="")
    show_hex(H(bs2))
