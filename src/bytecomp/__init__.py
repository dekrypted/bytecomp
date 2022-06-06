# bytecomp by DeKrypt | https://github.com/dekrypted
# Can be used to compile python objects to bytecode, and generate the bytecode header.
# Can also be used to execute bytecode and remove headers.

import dis
import marshal
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

            
