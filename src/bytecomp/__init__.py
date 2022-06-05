# bytecomp by DeKrypt | https://github.com/dekrypted
# Can be used to compile python objects to bytecode, and generate the bytecode header.
# You can then write it to a .pyc file and use it.

# Example:
# import test
# open('compiled.pyc','wb').write*(test.compile_object(compile(<code>, 'filename', 'exec')))
# The above code will compile a code object to a .pyc file.

import dis, marshal, importlib.util

def generate_header():
    return importlib.util.MAGIC_NUMBER + b'\0'*(16-len(importlib.util.MAGIC_NUMBER))

MAGIC = importlib.util.MAGIC_NUMBER
HEADER = generate_header()

def compile_object(object):
    try:
        bytecode = dis.Bytecode(object).codeobj
    except TypeError:
        raise TypeError("Unsupported object type: %s" % type(object).__name__)
    except Exception:
        raise Exception("An Unknown Error occurred.")
    return generate_header() + marshal.dumps(bytecode)

