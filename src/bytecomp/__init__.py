# bytecomp by DeKrypt | https://github.com/dekrypted
# Can be used to compile python objects to bytecode, and generate the bytecode header.
# You can then write it to a .pyc file and use it.

# Example:
# import test
# open('compiled.pyc','wb').write*(test.compile_object(compile(<code>, 'filename', 'exec')))
# The above code will compile a code object to a .pyc file.

import dis
import marshal
from importlib.util import MAGIC_NUMBER as MAGIC


def generate_header():
    return MAGIC + b'\0'*(16-len(MAGIC))


def compile_object(object: object) -> bytes:
    try:
        bytecode = dis.Bytecode(object).codeobj
    except TypeError:
        raise TypeError("Unsupported object type: %s" % type(object).__name__)
    except Exception:
        raise Exception("An Unknown Error occurred.")
    return generate_header() + marshal.dumps(bytecode)


if __name__ == "__main__":
    pass
