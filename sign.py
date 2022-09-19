from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256


def sign(m):
    curve1 = curve.secp256k1
    keysTuple = fastecdsa.keys.gen_keypair(curve1)
    # generate public key
    # Your code here
    public_key = keysTuple[1]  # public_key = Q = dG

    d = keysTuple[0]  # d = secret key

    # generate signature
    # Your code here

    (r, s) = fastecdsa.ecdsa.sign(m, d, curve1, sha256, false)

    assert isinstance(public_key, point.Point)
    assert isinstance(r, int)
    assert isinstance(s, int)
    return (public_key, [r, s])


