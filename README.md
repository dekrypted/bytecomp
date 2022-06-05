# bytecomp
Utilities for working with bytecode.

**Magic:**
```py
import bytecomp

bytecomp.MAGIC # Returns Magic
```

**Pyc Headers:**
```py
import bytecomp

bytecomp.HEADER # Returns .pyc Header
bytecomp.generate_header() # Also returns a .pyc header
```
**Compiling Bytecode:**
```py
import bytecomp

code_object = compile("""print('Hello!')""",'file','exec')
pyc = open('compiled.pyc','wb')
pyc.write(bytecomp.compile_object(code_object))
pyc.close()

# Above code generates a working .pyc file from a code object.
```
