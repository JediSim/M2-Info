#! /usr/bin/env python3

import random
from random import randrange
import datetime
import sys


def miller_rabin(n, a):
    """Miller Rabin primality test for n with witness a"""
    d, s = n-1, 0
    while d % 2 == 0:
        d, s = d//2, s+1
    t = pow(a, d, n)
    if t == 1:
        return True
    while s > 0:
        if t == n - 1:
            return True
        t, s = pow(t, 2, n), s - 1
    return False


def is_prime(n, k=128):
    """full Miller Rabin primality testing for n"""
    if n % 2 == 0:
        return n == 2
    for _ in range(1, k):
        a = randrange(2, n)
        if not miller_rabin(n, a):
            return False
    return True


def new_prime(nb_bits):
    """generate a new prime with ``nb_bits`` bits"""
    while True:
        a = randrange(2**(nb_bits-1), 2**nb_bits)
        if is_prime(a):
            return a


def extended_gcd(a, b):
    """extended euclidean algorithm to compute GCD and Bezout numbers"""
    lastr, r = a, b
    lastx, x, lasty, y = 1, 0, 0, 1
    while r:
        lastr, (quotient, r) = r, divmod(lastr, r)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    assert lastr == lastx * a + lasty * b
    return lastr, lastx, lasty


def inverse_mod(a, m):
    """inverse of a modulo m"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('inverse_mod for {} does not exist'.format(a))
    assert (a * (x % m)) % m == 1
    return x % m


def save_public_key(M, e, expire_date, f=None):
    if f is None:
        f = sys.stdout
    f.write("# public key\n")
    f.write(expire_date.strftime('# this key will expire on the %Y-%m-%d at %H:%M:%S\n'))
    f.write("M = {}\n".format(M))
    f.write("e = {}\n".format(e))


def save_private_key(a, b, d, e, expire_date, f=None):
    if f is None:
        f = sys.stdout
    f.write("# private key\n")
    f.write(expire_date.strftime('# this key will expire on the %Y-%m-%d at %H:%M:%S\n'))
    f.write("a = {}\n".format(a))
    f.write("b = {}\n".format(b))
    f.write("M = {}\n".format(a*b))
    f.write("e = {}\n".format(e))
    f.write("d = {}\n".format(d))


def gen_key():
    # initialize RNG with number of milliseconds since epoch (01-01-1970)
    random.seed(int(1000*datetime.datetime.now().timestamp()))

    n = 512                             # number of bits in modulus
    a = new_prime(n//2)                 # the two prime numbers
    b = new_prime(n//2)                 # ...
    e = 65537                           # public exponent
    d = inverse_mod(e, (a-1)*(b-1))     # private exponent

    # validity of one year
    expire_date = datetime.datetime.now()
    expire_date = expire_date.replace(year=expire_date.year + 1)

    # display public key
    print(">>> showing public key")
    save_public_key(a*b, e, expire_date)
    # save public key to file
    print(">>> saving public key to 'public.key'")
    f = open("public.key", mode="w")
    save_public_key(a*b, e, expire_date, f)

    # save private key to file
    print(">>> saving private key to 'private.key'")
    f = open("private.key", mode="w")
    save_private_key(a, b, d, e, expire_date, f)


if __name__ == "__main__":
    f = open("public.key", mode="r")
    expire_string = f.readline()
    M = int(f.readline().strip()[3:])
    e = int(f.readline().strip()[3:])

    expire_date = datetime.datetime.strptime(expire_string, "%Y-%m-%d at %H:%M:%S\n")
    expire_date = expire_date.replace(year=expire_date.year - 1)
    crack(M, e, int(1000*expire_date.timestamp()))
    gen_key()
