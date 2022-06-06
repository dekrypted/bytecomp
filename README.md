# Bytecomp v1.1.0
Utilities for working with bytecode.

**Magic:**
```py
import bytecomp

bytecomp.MAGIC # Returns Magic
```

**PYC Headers:**
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

**Executing Bytecode:**
```py
import bytecomp

code_object = b'U\r\r\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00e\x00d\x00\x83\x01\x01\x00d\x01S\x00)\x02z\x03Hi!N)\x01\xda\x05print\xa9\x00r\x01\x00\x00\x00r\x01\x00\x00\x00\xda\x03idk\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00'
bytecomp.exec_bytecode(code_object)

# Above code executes the bytes-like object (Can have a header or not have a header)
```

**Removing a header from Bytecode:**
```py
import bytecomp

bytecomp.remove_header(b'U\r\r\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00e\x00d\x00\x83\x01\x01\x00d\x01S\x00)\x02z\x03Hi!N)\x01\xda\x05print\xa9\x00r\x01\x00\x00\x00r\x01\x00\x00\x00\xda\x03idk\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00')

# Above code removes the header (First 16 bytes) so you can unmarshal it and execute it
```

**Encrypting Bytecode:**
```py
import bytecomp

code_object = compile("print('This is a test.')",'file','exec')
crypted = bytecomp.crypt_bytecode(code_object)

# Above code returns a string, which can be executed with the code below.
```

**Executing Encrypted Bytecode:**
```py
import bytecomp
bytecomp.exec_crypted('c%0*YdNS#d&&L@bBZH4CS3P4z1MEQT3dCicKq7%Pk+qG5g*A~Sj8%udo+~gnr%V-yQdA2Q$_ll;by)5*l$PgY7p`F~2WbQo_ZgFOG869eT4rP=7Gx$^vjD}ufs6(KfJq*%')

# Above code executes the encrypted code we made earlier.
```

**Bytecomp** is created by DeKrypt. <br>
[Support the project!](https://github.com/dekrypted/bytecomp) Leave a star.
