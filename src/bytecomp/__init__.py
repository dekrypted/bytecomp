# bytecomp by DeKrypt | https://github.com/dekrypted
# Can be used to compile python objects to bytecode, and generate the bytecode header.
# Can also be used to execute bytecode or remove headers.
# Also can be used to encrypt bytecode, as a sort of obfuscation.

import dis
import marshal
import base64
import zlib
import random
from importlib.util import MAGIC_NUMBER as MAGIC


def generate_header():
    return MAGIC + b'\0'*(16-len(MAGIC))

HEADER = generate_header()

def compile_object(object: object) -> bytes:
    try:
        bytecode = dis.Bytecode(object).codeobj
    except TypeError:
        raise TypeError("Unsupported object type: %s" % type(object).__name__)
    except Exception:
        raise Exception("An Unknown Error occurred.")
    return HEADER + marshal.dumps(bytecode)

def remove_header(bytecode):
    try:
        marshal.loads(bytecode)
        return bytecode
    except ValueError:
        try:
            marshal.loads(bytecode[16:])
            return bytecode[16:]
        except ValueError:
            raise ValueError('Bad/Invalid Bytecode!')

def exec_bytecode(bytecode):
    if type(bytecode).__name__ == 'code':
        exec(bytecode)
        return
    if type(bytecode).__name__ != 'bytes':
        raise TypeError('Object is not a bytes-like object!')
    exec(marshal.loads(remove_header(bytecode)))

def crypt_bytecode(bytecode):
    if type(bytecode).__name__ == 'code':
        bytecode = marshal.dumps(bytecode)
    if type(bytecode).__name__ != 'bytes':
        raise TypeError('Object is not a bytes-like object!')
    bytecode = remove_header(bytecode)
    value = random.randrange(5,15)
    bytecode = bytes([value])+bytes([random.randrange(1,255) for _ in range(value-1)]) + bytecode
    bytecode = bytes([x^5 for x in bytecode])
    bytecode = base64.b85encode(zlib.compress(bytecode)).decode()
    return bytecode

def exec_crypted(crypted):
    try:
        crypted = base64.b85decode(crypted.encode())
        crypted = zlib.decompress(crypted)
        crypted = bytes([x^5 for x in crypted])
        buffer = int(crypted[0])
        crypted = crypted[buffer:]
        exec(marshal.loads(crypted))
    except Exception:
        raise ValueError('Invalid Type/Content!')
    
    
    
